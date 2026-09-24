# Master Video Forensic Reconstruction Report

## Executive finding

The reference is a 14:03.68 landscape narration video built from **253 distinct full-frame editorial illustrations**, not conventional live-action shots and not character animation. The edit makes those stills feel active through **252 hard cuts** and **225 rigid whole-image transforms**: **73 centered push-ins**, **77 upward virtual-camera moves** and **75 downward virtual-camera moves**. The remaining **28 shots are true static holds**.

The decisive reconstruction rule is therefore simple: generate or illustrate one correct 16:9 master image per visual state, keep all characters and objects frozen, add exact text as editor overlays, animate only the complete flattened plate with deterministic scale/position keyframes, keep the small channel watermark fixed in screen space, and hard-cut to the next image. No independent head, hand, cloth, plant, pet, light, particle or environmental animation is visibly evidenced.

Confidence: **HIGH** for metadata, shot count, boundary timing, global motion classes and transcript timing; **MEDIUM** for precise object geometry and unreadably small environmental lettering; **LOW / NOT VERIFIABLE** for the original image model, editor, plugins, font files, easing curves, music track and sound-effect library.

## Evidence package

- `visual_reconstruction_cards.md` — 253 complete 28-section production cards.
- `visual_catalog.csv` — compact shot/state descriptions, beat alignment, text and motion classes.
- `animation_prompts.csv` — all animation events with source/target states, methods, ≤500-character prompts and counts.
- `edl.csv` — full edit decision list.
- `script_beats.md` — 41 script beats with loop status and transcript text.
- `transcript.txt`, `transcript.srt`, `transcript.json` — local Base English Whisper transcript, including word timestamps in JSON.
- `shot_manifest.json` — measured cut points, sample times, change metrics and affine motion estimates.
- `evidence/overview_contact_sheet.jpg` and 16 shot montage pages — visual overview.
- `evidence/motion_triplets_01.jpg` through `motion_triplets_32.jpg` — start/mid/end motion evidence for every shot.
- `audio_summary.json`, `audio_envelope.csv`, `audio_envelope.png` — full-mix audio measurements.

## Pass 0 — media inspection

| Property | Measured value |
|---|---:|
| Duration | 843.636 s / 00:14:03.636 |
| File size | 61,671,022 bytes (about 58.8 MiB) |
| Resolution | 1280×720 |
| Aspect ratio | 16:9 |
| Orientation | Landscape |
| Frame rate | 30 fps |
| Video | H.264 Main, `avc1`, yuv420p, BT.709, progressive, about 453 kb/s |
| Audio | AAC-LC, 44.1 kHz, stereo, about 128 kb/s |
| Audio presence | Yes |
| Container | ISO Base Media / MP4 |

The source was directly decoded in full. Overview frames, 253 shot representative frames and 759 start/mid/end samples were generated. Transcript extraction succeeded for English narration: 282 ASR segments over the full program.

## Passes 1–3 — shots, visual states and dense sampling

### Shot/state detection

- Major shots: **253**.
- Meaningful visual states: **253**. Each cut introduces a new base illustration; no within-shot independently animated object state was found.
- Transitions: **252 hard cuts**. Two boundaries at **00:03:01.833** and **00:04:30.233** scored just below a stricter scene threshold and were recovered through dense 4 fps sampling and a lower validated threshold.
- Average shot length: **3.335 s**.
- Median shot length: **3.367 s**.
- Shortest: **S056**, 1.367 s, 00:02:41.500–00:02:42.867.
- Longest: **S043**, 5.567 s, 00:01:59.500–00:02:05.067.
- Opening cluster: 34 shots before routine one, averaging 2.777 s.
- Eight-routine body: 202 shots, averaging 3.411 s.
- Closing cluster: 17 shots, averaging 3.537 s.

### Motion-critical finding

Feature registration across every start/end triplet found only four reference-faithful behaviors:

| Behavior | Count | Observed construction |
|---|---:|---|
| Centered push-in | 73 | Full illustration scales by roughly five percent; internal scene remains rigid. |
| Camera moves up | 77 | Full illustration shifts down by roughly 21 px, revealing a slightly higher crop. |
| Camera moves down | 75 | Full illustration shifts up by roughly 21 px, revealing a slightly lower crop. |
| Static hold | 28 | No measurable camera or object movement. |

No local object deformation survived registration as an independent event. Apparent action—walking, waving, pancake tossing, gardening, pointing, laughing—is represented by a frozen mid-action drawing. This is crucial: those poses imply action, but the video does **not** animate that action.

## Pass 4 — persistent asset manifest

| ID | Type | Persistent production role |
|---|---|---|
| C01 | Character | Primary gray-haired, bespectacled retiree; identity varies perceptibly across generated illustrations. |
| C02 | Character | Older woman/wife/peer, used for meals, care, laughter and gratitude. |
| C03 | Character set | Older male friends, younger adults, workers and helpers. |
| C04 | Character set | Children/grandchildren in setup and family examples. |
| E01 | Environment | Warm home interiors: kitchen, bedroom, living room, hall and office. |
| E02 | Environment | Porch, garden, street, park and sunrise exteriors. |
| E03 | Environment | Bank, store, clinic, office, subway, café, community center and gym. |
| O01 | Object family | Coffee mugs, glasses, meals and kitchen props. |
| O02 | Object family | Television, phone, tablet, laptop and news screens. |
| O03 | Object family | Bed, bedside lamp, clock and sleep props. |
| O04 | Object family | Plants, garden tools, cats and dogs. |
| O05 | Object family | Papers, calendars, budgets, lists and newspapers. |
| G01 | Graphic | Eight routine title boards/whiteboards/chalkboards. |
| G02 | Graphic | Small circular channel watermark fixed at upper-right. |
| G03 | Graphic | Occasional subscribe overlay near lower-right. |
| T01 | Text system | Handwritten routine headings; deterministic overlay recommended. |
| A01 | Audio | Continuous male English narration. |
| A02 | Audio | Low-level full-mix bed persisting under many narration gaps; likely music/ambience, track unverified. |
| A03 | Audio | Short silence/near-silence at section boundaries and about 0.9 s at the tail. |

## Pass 5 — frame-state chain

Animated shots use one state chain only:

`F###.0 — source crop → T### — rigid whole-plate position/scale transform → F###.1 — measured end crop → hard cut`

Static shots use:

`F###.0 — unchanged hold → hard cut`

There are no verified sequential object states, no simultaneous independent object motions, no persistent internal loops and no first/last-frame morphs. The complete state-chain package for every shot appears in `visual_reconstruction_cards.md`.

## Engine A — script intelligence

### A1–A2: grounding and packaging promise

Title promise: **Simple Routines Thriving Retirees Practice Daily**. No separate thumbnail was supplied, so a thumbnail promise cannot be verified. The title's click question is: *Which simple daily routines distinguish thriving retirees?* The video answers with eight named routines, each explained through a problem, mechanism, examples and an actionable close. Packaging/body/payoff classification: **STRONG MATCH**.

### A3: hook architecture

The opening validates a familiar retirement fantasy—beach, cruise, golf, grandkids—then breaks it with “that's the trailer, not the movie.” The reveal that retirement is a random Tuesday converts an abstract future into a repeatable unit of daily life. “About 10,000 Tuesdays” is the key curiosity and value frame. Context, relevance, contradiction, open question and value preview all arrive before the first routine at 01:31.68.

### A4: causal story spine

The macro spine is: **retirement is sold as highlights → but most of it is ordinary time → therefore daily routines determine lived quality → eight routines repair common forms of drift → money buys freedom, but routines build the life**.

Each routine repeats a strong causal micro-spine: **name the trap → show what retirement removed or loosened → explain the physical/psychological consequence → offer a small daily behavior → close with an aphoristic payoff**. This is mostly `BUT → THEREFORE`, not a loose “and then” list.

### A5–A6: curiosity and payoff

The numbered list creates stable forward curiosity, but each routine is announced before explanation, so suspense is modest rather than expanding. Micro-payoffs include “chase the daylight,” “guard your sleep,” “control the information,” “being needed is medicine,” “feed yourself like you're worth the effort,” “order out there creates calm in here,” “laugh on purpose,” and “find three good things.” The ultimate payoff—money is the tool, routines are what you build with it—correctly returns to the ordinary-Tuesday premise.

### A7: logic

Most advice follows claim → mechanism → consequence → minimum action. The video does not cite sources for several health claims, including morning light's downstream effects, sleep “power washing” the brain, laughter's cardiac benefit, and nursing-home plant/pet outcomes. Those claims may be directionally plausible, but within this video they are unsupported assertions. Medical precision should be softened or sourced if the script is republished.

### A8: emotion

The dominant emotional progression is aspiration → comic recognition → mild anxiety about drift → relief through small actions → warm closure. Humor prevents the advice from becoming scolding: the “wise lizard,” “toddler's finger painting,” “sink grazing,” “coffee and hope,” “human keep-off-the-grass sign,” and caveman analogy are deliberate pressure releases.

### A9–A10: retention, share and replay

Strengths: frequent visual resets, numbered structure, vivid metaphors and highly quotable closes. Risks: 14 minutes of the same illustration grammar can become visually predictable; eight routines create a midpoint list-fatigue risk; title cards reveal each answer before its mechanism; some examples over-explain after the point is understood. Positive replay candidates are the ordinary-Tuesday hook, the information-diet punchline and the money/toolbox synthesis. Confusion replay risk is low, though unsupported health specificity could invite scrutiny.

### A11–A12: CTA and next video

The commitment CTA—pick one, name what you already do well and what needs work—arrives after the full payoff and is **EARNED**. Like/subscribe follows and is short. The next-video bridge is generic (“new videos every week”) rather than a specific unresolved related question; this is the weakest packaging transition.

### A13: consensus

- Strong agreements: the Tuesday reframing, repeated causal routine structure, humor and practical micro-actions are the system's strongest elements.
- Important tradeoff: breadth delivers eight ideas but limits evidence and novelty within each.
- Critical problem: visual identity drift and repetitive pan/zoom grammar reduce perceived polish.
- Highest leverage fixes: tighten redundant explanations, add source-backed specificity where medical claims are made, and vary the visual mechanism at routine-level transitions without adding decorative motion inside ordinary shots.

## Engine B — visual intelligence

### Objective visual grounding and spatial geometry

The visual system is a sequence of warm 16:9 editorial cartoons. C01 usually occupies the center or one side of a medium-wide frame; a single routine object sits close to the face or hands; the environment fills the remaining thirds. Eye path is consistently face → gesture/prop → contextual background. Numerical element coordinates were not invented; each card records defensible frame-third relationships and measured global transforms.

### Cinematography and attention

Most scenes simulate eye-level medium-wide photography, occasionally switching to closer domestic reactions or wide environmental tableaux. Positive routines use amber sun, warm wood and green gardens; failure states use blue night, purple television light, cool clinics and dim rooms. Attention is usually clean because the large expressive face and one prop dominate. Overload is intentionally used for clutter, news and paperwork examples.

### Editing and temporal change

Every new state arrives by hard cut. Within a state, nothing is added, removed, redrawn or independently animated. Temporal change is only crop, scale or hold. This is more accurately a Ken Burns-style editorial slideshow than AI video animation.

### Information value and object lifecycle

Screens/phones progress from passive consumption to deliberate shutoff; beds/clocks progress from chaos to protected rhythm; plants/pets move from example to responsibility; papers/clutter move from stress to order; food progresses from snack improvisation to intentional meals. The title boards are explicit routine resets and the protagonist is the persistent continuity device.

### Continuity drift

Identity continuity is **MEDIUM–LOW**. Hair shape, beard density, glasses, age, face proportions and even body type change across shots. Wardrobe changes are often motivated by context but not consistently tracked. Secondary characters also shift style. Environmental perspective and object scale vary. These are visible generation inconsistencies, not motion events. A locked character sheet and seed/reference workflow would materially improve fidelity.

### Color, typography and visual DNA

Dominants: amber, tan, brown, muted red plaid and garden green. Negative states shift toward navy, cyan and violet. Routine title cards use hand-lettered black text on whiteboard/green chalkboard surfaces. Environmental lettering is often small, warped or pseudo-legible. Recreate all semantic text outside the image generator. Visual DNA: storybook/editorial AI illustration, expressive older protagonist, literal metaphors, warm domestic spaces, one visual idea per frame, hard cuts and alternating whole-frame reframes.

## Engine C — reconstruction and motion intelligence

### Image system

Generate 253 text-free master illustrations from the standalone prompts in the card file. Use a persistent C01 character reference, but permit explicitly different supporting characters where shown. Generate at least 1344×756 or, preferably, 1920×1080 so a five-percent zoom and 21 px pan do not expose edges. Crop/export to 1280×720 only after motion.

### Text bake policy

Semantic text should not be baked by an image model. Build routine headings, calendar data, signs, screens and callouts as editable vector/text overlays, matched to the source surface and line breaks. Flatten those overlays with the illustration before applying the global move so they remain registered to the scene. The small circular watermark and subscribe bug remain separate screen-space layers.

### Complete motion inventory

Total motion events: **225**. Every event is a single rigid global transform. Total non-events/static holds: **28**. Motion relationship classification for all moving shots: **CAMERA + SUBJECT COUPLED**. Motion hero: complete illustration plate. Static anchors: all internal geometry and screen-space overlays.

### AI / deterministic / hybrid routing

- Primary method: **EDITOR KEYFRAMES** for all 225 moves.
- Static method: **STATIC HOLD** for 28 shots.
- AI single pass recommended: 0.
- AI multi-pass recommended: 0.
- AI state-chain generation recommended: 0.
- First/last-frame AI recommended: 0.
- Hybrid internal animation recommended: 0.

AI image generation is useful for the base illustrations; AI image-to-video is not the faithful motion method. Optional AI prompts are included because the specification requests them, but they are rated LOW suitability. The deterministic editor instructions are the authoritative reconstruction path.

### Motion-cue conflict

Many source drawings depict mid-action poses—walking, waving, tossing food, laughing, watering or pointing. Those cues suggest motion, but dense sampling shows that the pose remains frozen while the camera reframes. Do not “complete” the implied action. The corrected source is the exact frozen reference pose, without motion blur or speed lines unless visibly present.

### Editor build

For each shot: import the master illustration → add deterministic surface text → precompose those two → apply measured scale/position keyframes to the precomp → add watermark and subscribe bug above it → hard-cut at the EDL boundary. No optical flow, frame interpolation, puppet deformation, parallax, 2.5D depth or AI video generation is needed.

## Editing intelligence

EDL status: **COMPLETE**. Shot count 253; transitions 252 hard cuts; average 3.335 s; median 3.367 s. Cut motivation follows phrase completion, metaphor change, example change, routine title or payoff. The fastest-feeling cluster is the stereotype montage and early hook; the slowest shots appear where one complex metaphor or emotional beat needs more reading time. The complete row-level EDL is in `edl.csv`.

## Audio intelligence

Narration is verified across 282 timestamped ASR segments. The full mix measures approximately **−11.86 LUFS integrated**, **−0.10 dBTP true peak** and **4.0 LU loudness range**—loud, dense and tightly controlled. Median 0.25 s RMS is -16.12 dBFS; narration-majority windows are -15.29 dBFS; near-non-speech windows remain around -36.56 dBFS. That persistent low-level energy is consistent with a music or ambience bed, but no stem or semantic track identification is available, so the exact track is **NOT VERIFIED**. Top peaks align primarily with speech; no unique SFX can be confidently named. Near-silence occurs around 04:08.50, 06:51.75, 06:55.75, 11:22.50 and the final 0.9 s. Narration ends at about 14:02.62, followed by a short tail/fade.

Audio event → visual event mapping is primarily rhetorical: narration phrase changes trigger hard cuts; routine titles receive clean visual resets; punchlines receive reaction or metaphor images. No frame-accurate SFX hits were verified.

## Thumbnail and Shorts extraction

### Thumbnail candidates

1. **V020 at 00:45.833** — retiree with a wall of Tuesdays. Dominant object: calendar. Mobile question: “How many ordinary Tuesdays are left?” Remove tiny peripheral clock details; enlarge the retiree and “10,000 Tuesdays” as new deterministic thumbnail text. Strongest title relationship.
2. **V043 at 02:02.300** — retiree under a spotlight with arms raised. Strong silhouette and high contrast, but weaker direct relationship to the title. Pair with “8 DAILY ROUTINES” only if text is added outside the image.
3. **V251 at 13:54.167** — savings progress, new week and planner. Clear habit/system symbolism, though less emotionally immediate.

### Shorts candidates

- **00:20.74–00:48.32**: “That's the trailer, not the movie” → ordinary Tuesday → thousands of Tuesdays. Context required: minimal. Core payoff: retirement quality is daily, not occasional.
- **04:45.25–05:30.34**: information industry → check once → do not hand your peace back to a screen. Strong standalone contradiction and close.
- **10:49.37–11:19.26**: laugh at aging instead of raging at it → walking into a room and forgetting why. Humor-led, low-context clip.
- **12:59.30–13:28.93**: money is the tool; routines are what you build with it. Best channel-positioning Short and conclusion.

Use the corresponding visual cards and animation prompt rows for exact images and motion. Do not force additional CTA animation.

## Engine D — master synthesis

### Story engine

**HOOK:** retirement postcard fantasy. **ESCALATION:** most time is ordinary and unstructured. **REVERSAL:** thriving is built through tiny routines, not exceptional events. **PAYOFF:** money creates freedom; daily behaviors turn freedom into a life.

### Creator visual and motion formula

`Narration phrase → literal/metaphorical editorial illustration → one rigid push/pan/hold → hard cut on next phrase`

What moves: the complete flattened image. What stays static: everything inside it. Static coordinate frame: 1280×720 canvas plus watermark. Trigger: narration phrase or micro-payoff. Camera moves only as an editorial crop; the creator cuts instead of animating whenever the idea changes.

### AI reconstruction engine

Base images: AI/illustration-friendly. Motion: deterministic editor-only. State chains: one transform per moving shot. Text: vector/editor. First/last frames: unnecessary because the target is a crop, not a changed scene. Multi-pass isolation: unnecessary if the art remains a single plate. Validation: frame-difference the finished clip against the reference and reject any internal deformation.

### Master image DNA

- Character: late-sixties gray-haired bespectacled retiree, short beard, expressive eyes, average build; lock a turnaround sheet and five core expressions.
- Objects: simplified domestic props with dark outlines and readable silhouettes; one routine-relevant hero prop per scene.
- Environments: warm American suburban homes and public spaces, rendered in layered but shallow editorial depth.
- Graphics: clean chalkboards, whiteboards, screens and signs with text added later.
- Style: polished hand-inked digital cartoon, softly painted texture, warm midtones, stable anatomy, 16:9 medium-wide staging.
- Color: amber/brown/green for thriving; navy/cyan/violet for fatigue, news and worry.
- Typography: hand-lettered display for routine titles, plain readable sans serif for calendars/screens; never accept pseudo-text from the image model.

### Repeated attention engine

Face/expression first → hand/prop second → environment/board third. The motion does not redirect the eye internally; it only changes crop scale. Routine title cards reset the hierarchy by making the heading first.

### Improvements

| Priority | What works | Friction | Minimal fix | Aggressive fix |
|---|---|---|---|---|
| Critical | Clear protagonist and warm visual tone | Character face, beard, glasses and age drift | Use one locked character reference and reject off-model frames | Build a full C01 model sheet and fine-tuned/consistent illustration pipeline |
| High | Frequent visual resets | 225 moves repeat only three transform types | Vary start crops and hold timing while keeping internal stillness | Introduce a small set of deterministic diagrams or object reveals only at major mechanisms |
| High | Eight clear routine boards | Small text is often warped or pseudo-legible | Replace semantic text in editor | Generate all scenes as text-free clean plates and maintain a typography system |
| High | Humor and practical metaphors | Some health claims are unsourced | Soften absolute wording | Add succinct source cards or linked references |
| Medium | Hard cuts maintain pace | Constant cuts can feel mechanical | Let selected payoff images breathe one extra second | Group examples into visual mini-arcs with purposeful callback frames |
| Medium | CTA is earned | Next-video bridge is generic | Name a specific related unanswered question | Script the conclusion into the next episode's packaging promise |
| Optional | Warm color system | Negative states lean on similar blue-TV imagery | Rotate among composition, prop and lighting contrasts | Create routine-specific accent colors and recurring visual motifs |

### New-topic translation

No new topic was supplied. Use this mapping template without copying surface content:

| Original function | Original mechanism | New-topic equivalent |
|---|---|---|
| Postcard retirement fantasy | Rapid idealized montage | Show the new topic's culturally familiar “highlight reel” |
| Ordinary Tuesday reveal | One mundane domestic unit repeated over time | Identify the smallest repeatable unit where outcomes are actually decided |
| Eight routine boards | Numbered chapter reset | Use a fixed count of practical levers with deterministic title cards |
| Trap scenes | Blue/dim failure-state illustrations | Show the default failure behavior in the new domain |
| Mechanism scenes | Literal metaphor cartoons | Visualize why the lever works, not just what to do |
| Minimum action | One person and one hero prop | Stage the smallest executable behavior |
| Aphoristic close | Warm payoff image | End each chapter with a memorable one-line rule |
| Money/tool synthesis | Return to opening premise | Reconcile the enabling resource with the behavior that creates value |

Keep the composition grammar, motion grammar, pacing, transition logic, proof logic, payoff structure and asset reuse. Change facts, objects, characters, maps, numbers, branding and literal imagery.

## Zero-to-final rebuild order

1. Lock the title promise and one clear click question.
2. Segment the script into the 41 supplied beats.
3. Preserve the macro causal spine and routine micro-spines.
4. Import `edl.csv` as the timing blueprint.
5. Use `visual_catalog.csv` to assign all 253 states.
6. Build the persistent asset library and C01 character sheet.
7. Generate 253 text-free master illustrations from the card prompts.
8. Quality-control identity, pose, object count, composition, lighting and negative space.
9. Rebuild all semantic text as deterministic overlays.
10. Place illustration plus surface text in one precomp per shot.
11. Apply the exact measured transform in each card: push-in, upward move, downward move or hold.
12. Keep watermark and subscribe overlay fixed above the moving precomp.
13. Assemble 252 hard cuts at the EDL boundaries.
14. Lay in narration and verify phrase-to-cut sync.
15. Add or recreate a low-level music bed only after verifying the desired track; do not invent SFX.
16. Mix to an intentional target, preferably about −14 to −16 LUFS with true peak at or below −1 dBTP unless the distribution platform requires otherwise.
17. Run continuity, text, crop-edge and motion-leakage audits.
18. Compare start/mid/end frames against the evidence triplets.
19. Verify the title promise, ordinary-Tuesday payoff and CTA bridge.
20. Export H.264, 1280×720, 30 fps, BT.709 with AAC audio.

## Completeness audit

| Requirement | Result |
|---|---:|
| Source video inspected | YES |
| Major shots | 253 |
| Visual states | 253 |
| Script beats | 41 |
| Persistent assets | 19 |
| Visual cards | 253 / 253 |
| Standalone image prompts | 253 / 253 |
| Text bake decisions | 253 / 253 |
| Frame state chains | 253 / 253 |
| Total motion events | 225 |
| Motion events identified | 225 / 225 |
| Why-move/static analysis | 253 / 253 |
| Motion coupling classified | 253 / 253 |
| Motion interference checks | 253 / 253 |
| AI suitability decisions | 253 / 253 |
| Primary methods | 253 / 253 |
| AI single-pass recommended | 0 |
| AI multi-pass recommended | 0 |
| AI state-chain recommended | 0 |
| First/last-frame recommended | 0 |
| Hybrid recommended | 0 |
| Deterministic/editor | 225 |
| Static | 28 |
| AI source images identified | 225 / 225 |
| Optional AI prompts | 225 / 225 |
| AI prompts ≤500 | 225 / 225 |
| Prompt character counts | min 310, max 328, all PASS |
| Transitions | 252 / 252 |
| EDL | COMPLETE |
| Audio | COMPLETE for full-mix timing/loudness; LIMITED for music/SFX stem identity |
| Master synthesis | COMPLETE |

## Final quality gate

- Reference fidelity: PASS. No decorative internal animation was added.
- Image coverage: PASS. Every state has an independent generation prompt and text plan.
- Motion inventory: PASS. All 225 meaningful events are global plate transforms; 28 static states are explicit.
- Motion isolation: PASS. Illustration/surface text move together; watermark remains isolated in screen space.
- Same-frame motion: PASS. No independent same-frame events exist.
- AI routing: PASS. AI is reserved for still generation; deterministic keyframes are preferred for motion.
- Prompt limit: PASS. Maximum optional animation prompt length is 328 characters.
- State chain: PASS. Every moving shot starts from its own F0 and ends at measured F1.
- Editing: PASS. The EDL and compositing method prevent drift.
- Final reconstruction test: PASS for a competent illustrator/AI image operator and editor. Exact original fonts, model, plugin, easing curves, music track and source-project files remain unverifiable.

## Limitations stated exactly

Missing/unverifiable: original image-generation model and seeds, original editor and plugins, exact font files, exact easing curves, exact source artwork beyond the encoded 1280×720 frames, separate music/SFX stems, original thumbnail and audience analytics. Cause: those assets and project files were not embedded in the supplied MP4. Small environmental text that cannot be read at source resolution is labeled rather than invented. Transcript is locally generated ASR, not a supplied script; use the JSON word probabilities and source audio for final copy editing.
