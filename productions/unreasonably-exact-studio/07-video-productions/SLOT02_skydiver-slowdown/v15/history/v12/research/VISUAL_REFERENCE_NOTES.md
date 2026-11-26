# Visual reference notes — skydiver-slowdown v12

Principles only. No competitor characters, drawings, layouts or jokes are to be copied (xkcd audit rule K23, `CODEX_INDEPENDENT_REVIEW.md` K23). Source abbreviations:
- **DIR** = `~/Downloads/HumanCraft_FINAL_Claude_Animation_Director.md`
- **V2** = `~/Downloads/HumanCraft_Video_Studio_V2_Complete.md`
- **XF/** = `~/Documents/YIOS-local-audits/2026-11-23-xkcd-what-if-complete-forensics/`
- **CX** = `~/Documents/YIOS-local-audits/2026-11-23-codex-independent-xkcd-review/CODEX_INDEPENDENT_REVIEW.md`

Evidence caveat: the xkcd figures are one-coder, self-reviewed measurements (mostly stills; one video viewed frame by frame). Treat them as calibration points, not laws.

Frames viewed for this note: `XF/phase7c_frames/sheet1.jpg`, `sheet4.jpg` (portrait Shorts frames), `XF/ct_scan_pilot_9VG0yqq_PHM/sheet_02.jpg` (a scene build and a zoom-dissolve transition).

## 1. Combining separate illustrations into one scene
- **Each scene is a few independent layers on an empty ground (figure, prop, label, divider, symbol), not one flattened picture.** XF/`08_ORIGINAL_ASSET_RECIPES.md` §1. For us: skydiver rig, cloud planes, ground plane, arrow set, dial, graph = separate draw calls with their own transforms.
- **Make the composite physically consistent:** same light direction, scale logic, haze, edge softness, shadow side, line weight. DIR §6 Step 6 ("Composite and finish"); V2 §14. One stroke-width parameter for all linework (the reference ran about 6 px at a 1080 px short side; XF/`06_STYLE_ANALYSIS_PHASE62.md` Results).
- **Real layering shows differential motion and correct occlusion;** if every layer moves together it is a flat Ken Burns move, which is fine only if labelled as such. DIR §6 "The decisive 2.5D test". Our cloud layers must move at different rates and pass in front of and behind the diver.
- **Put depth near/mid/far deliberately and link all layer motion to one virtual camera.** DIR §6 Step 4. Do not let the camera move past the edge of painted coverage (V2 §13, last paragraph).
- **Add parallax/2.5D only where the idea needs it** (here it does: sense of falling speed comes from layer speed). XF/`08_ORIGINAL_ASSET_RECIPES.md` §2 method table.
- **A portrait frame is a recomposition, not a crop:** stack elements vertically, art in a band with plain space above/below. XF/`07c_SCIENCE_VISUAL_PASS_SHORTS.md` §3.2; seen in `phase7c_frames/sheet1.jpg` (full-height ruler with an arrow; tall objects run vertically).

## 2. Progressive diagram build-up
- **Build the diagram stepwise; reveal each value when it is spoken; hold for comprehension; then cut to the outcome.** DIR §13 recipe C "Science diagram with clarity".
- **A scene is assembled object by object, then held.** XF/`ct_scan_pilot_9VG0yqq_PHM/visual_ct_scan_report.md` §3 ("a kitchen scene built object by object", "a temperature axis built label by label"). Visible in `sheet_02.jpg`: the prop appears in the otherwise unchanged frame.
- **Shapes may pop on whole in one frame; lines (arrows, flows) grow over about 4-9 frames; labels appear whole or type on about one character per frame.** Same report §3 "What the changes are". Use trim-path growth for force arrows and streamlines, pops for nouns, typing for short labels.
- **Put the number on the drawing at the moment it is said, often in a different representation from the speech** (e.g. spoken "twice as fast" shown as two labelled arrows). XF/`07_SCIENCE_VISUAL_PASS.md` §3.1 and §5; about half of spoken quantities were on screen at that instant (`07c_...` §2).
- **Decide deliberately when NOT to show the number:** huge or abstract quantities are often carried by context. `07_SCIENCE_VISUAL_PASS.md` §3.4.
- **Comparison rides on layout:** side-by-side states, a scaled axis with objects placed on it, a labelled bracket. `07_SCIENCE_VISUAL_PASS.md` §3.2-3.3. For us: drag arrow vs weight arrow, same anchor, lengths to scale.
- **Arrows must have true mathematical meaning; reject enormous arrows that imply false scale.** DIR §13 C; DIR §17 E #91 ("Scientific arrows/vectors ... avoid exaggerated effect without scale annotation"). Mark schematic where not to scale (XF/`08_...` §3.4).
- **One diagram should reconfigure into the next related one rather than be replaced.** DIR §17 E #94 "Infographic layout morph"; #85 "Trim paths/write-on ... plot routes, vectors".

## 3. Camera moves that link ideas
- **Every camera move needs a reason:** approach a detail, reveal scale, track a subject, go macro-to-micro, reframe emphasis. No continuous zoom or oscillation by default. DIR §7 "Camera direction checklist"; V2 §13 table.
- **"Compare values": lock the camera and animate one variable at a time.** V2 §13 table row. Use this for the force-balance moment and the graph read-out.
- **Treat transitions as relationships between ideas:** match cut on shape, movement handoff in one direction, foreground-object wipe, hard cut for a reversal or punchline. DIR §8 "Editing and transition grammar". Avoid flash/glitch/shake/spin defaults (same section).
- **Reference practice: map pans/zooms with motion blur, a continuous scale-down through nested drawings, and diagram transitions with a short blurred smear** were confirmed in frame sequences. XF/`13_FINAL_REPORT.md` §D "Motion grammar". `sheet_02.jpg` shows an 8-frame zoom-dissolve from one scene into the next.
- **Plan the exit of each shot so the next transition makes sense** ("narrative exits"). V2 §12.
- **Keep screen direction and geography readable across cuts** (falling is always screen-down, or deliberately not). DIR §8 "Editorial continuity gates".

## 4. Negative space
- **Large empty ground is the norm:** median share of empty 48 px cells 0.66 (long) and 0.77 (Shorts); ink only about 3-6 % of the frame. XF/`06_STYLE_ANALYSIS_PHASE62.md` Results table; CX K12. For a 1080x1920 sky this argues for one subject cluster plus air.
- **Negative space is also a tension tool:** "slow move, negative space, static shot". V2 §13 table "Create tension".
- **Open with comfortable negative space and a slow authored push.** V2 §21 Example A, 00:00-00:04 row (principle only).
- **One accent colour, used sparingly, marks the thing that matters** (the reference used red on about a third of frames, at most about 3 % of pixels: arrows, key numerals, rings). XF/`06_STYLE_ANALYSIS_PHASE62.md` "What the viewing added"; `07_...` §3.5. Choose our own accent; reserve it for the drag arrow / key number.
- **Keep text off the subject and inside safe zones.** DIR §4 "Caption design rules"; DIR §8 continuity gates.

## 5. Keeping simple drawings alive
- **Alive does not mean constantly moving.** In the frame-by-frame reference video about 93 % of frames were holds and no hidden idle animation was found; life came from a new visual event roughly every 2.1 s (about 22 per minute). XF/`ct_scan_pilot_9VG0yqq_PHM/ALL_FRAMES_VIEW_REPORT.md` ("no hidden idle animation"); `visual_ct_scan_report.md` §3; XF/`06_PACING_CORRECTION.md` point 4. Target an event cadence, not ambient wiggle.
- **When it moves, it moves on ones** (every frame inside a change), then stops. `visual_ct_scan_report.md` §3 "Time structure".
- **Small rare surprises reward attention** (a tiny element appearing in a corner during a hold). `ALL_FRAMES_VIEW_REPORT.md` item 1.
- **One primary action plus restrained, physically caused secondary response** (sleeve trails, shadow follows, distant haze moves slowly). DIR §6 Step 5. Clothing and hair react to acceleration and wind, not wave continuously (DIR §7 "Rigged-character checklist"); V2 §12 "Follow-through ... not random constant wiggle".
- **"Motion can be understated": a well-composed held still at the right moment beats an unmotivated fly-through.** DIR §7.
- **Alternate high / medium / low energy beats instead of animating every sentence.** DIR §5 "Visual-density rhythm".
- **Timing from spoken stress and mass, per-action curves (spring, hold, stepped), not one easing preset.** V2 §12; DIR §7 "Motion principles" (timing and spacing, slow in/out matched to material).

## 6. Humour from the physical situation
- **Humour is a layer over a self-contained reasoning chain:** dry deadpan, absurd bureaucracy, an imagined objection, a running gag; the physics survives if the joke is cut. XF/`05_MASTER_SCRIPT_PLAYBOOK.md` (tone paragraph); XF/`05_CROSS_VIDEO_SYNTHESIS.md` §2 ("comic frame is often dropped in the Short cut, the physics chain is kept").
- **End on a button (reframe, deadpan advice, callback), never a summary or CTA.** `05_CROSS_VIDEO_SYNTHESIS.md` §2 last paragraph.
- **Exaggerate a gesture only while its physical meaning stays defensible.** DIR §7 "Exaggeration with limits". A joke must not imply a wrong force or speed.
- **Give a gag enough screen time to read; one gag readable at phone size beats three.** lemo-opuscar DIRECTOR §3/§7 (see LIBRARY_REVIEW); consistent with DIR §5 "every shot must earn its length".
- **Small annotation jokes live in the labels** (footnote-style asides next to a diagram) — observed in `phase7c_frames/sheet4.jpg`; adopt the device, write our own text.

## 7. Minimal on-screen text
- **Labels, not sentences:** short capitalised labels on the drawing, units attached to the arrow; equations only when they are the point. XF/`06_STYLE_ANALYSIS_PHASE62.md` "What the viewing added"; `07_...` §3.1.
- **Highlight only meaningful words; separate captions from deliberate kinetic type; respect reading time.** DIR §4 "Caption design rules".
- **Kinetic type for emphasised nouns and contrasts only, never every word.** DIR §17 E #77, #80 (avoid per-character animation that makes words unreadable).
- **No glow/blur on small essential labels.** V2 §12 "Motion blur".

## 8. Motion that steers attention
- **Define, per beat: what new idea, and where the eye should go first, before choosing any effect.** DIR §5 steps 1-2 ("Never pick an effect first").
- **Anticipation before a reveal** (a short hold or spacing change before the important graphic appears). DIR §7 "Anticipation"; V2 §12.
- **Only one thing changes at a time during an explanation** (locked camera, one variable). V2 §13 "Compare values".
- **Visual events cluster on speech clause starts** (machine association above chance). CX K17; XF/`13_FINAL_REPORT.md` §D "Narration alignment". Land each reveal on its keyword.
- **The accent colour and line growth are the pointer:** the eye follows the growing stroke and the single coloured element. `06_STYLE_ANALYSIS_PHASE62.md`; `ct_scan` report §3 (line write-ons).

## Production checklist derived from the above
1. Each beat: meaning, first eye target, one changing variable, cue word (DIR §5).
2. Every quantity: label / axis / side-by-side / scale reference, or a deliberate "not shown" (`07_...` §5).
3. Event roughly every 2 s; holds allowed but given a slow camera creep (see LIBRARY_REVIEW technique 2).
4. Arrows to scale or marked schematic; accent colour on one element per frame.
5. At least one shot-to-shot link built from the content (graph line, dial, cloud edge) rather than a fade (DIR §8).
