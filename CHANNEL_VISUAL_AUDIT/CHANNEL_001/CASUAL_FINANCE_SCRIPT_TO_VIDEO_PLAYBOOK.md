# CASUAL FINANCE: SCRIPT-TO-VIDEO PLAYBOOK (operational guide)

See the [current status and media guide](CURRENT_STATUS_AND_MEDIA.md) for authority, external evidence and first-run commands.

Audience: a fresh AI with NO access to earlier conversations. Read `CASUAL_FINANCE_VISUAL_INTELLIGENCE_INDEX.md` first (reading order, canonical files). This playbook is how to turn a NEW script into an original video.
Evidence labels used everywhere: **[M]** measured by script on pixels/frames, **[O]** observed on viewed frames, **[I]** inferred (hypothesis, not creator intent), **[U]** unavailable/not tested. Nothing here is a measured audience effect (no retention/CTR data exists). Do not copy the reference channel's characters, artwork, pop-culture clips or screenshots of third parties' work; copy the *method*.

Root paths (all under the worktree `/Users/ghilmankhan/workprojects/visual-audit-worktrees/casually-finance/`): `CH=CHANNEL_VISUAL_AUDIT/CHANNEL_001`, `V1=productions/new-original-video-v1-rent-01`.

---
## 0. Decide the format first
- **Long-form** (1920x1080, ~6-17 min): follow this playbook with `CH/22_LONGFORM_VISUAL_DNA.md` + `CH/LONGFORM_RHYTHM_STATS.md`.
- **Short** (1080x1920): `CH/05, 06, 09, 13, 21` govern; different pacing (states/min 40-60 median, bottom captions in some families). Do not mix. This playbook's evidence/beat method applies to both; the numbers in section 8 are long-form only.

## 1. The 19-step pipeline (every step has an output file)
| # | Step | Output (in `productions/<project>/`) |
|---|---|---|
| 1 | Read Visual DNA for the format | none (note any deviation in `DECISIONS.md`) |
| 2 | Read the script, mark sentence IDs (S001...) | `CLAIMS_AND_BEATS.csv` |
| 3 | Extract every factual claim (number, date, causal claim, named org/person, "X said") | claim register (id, text, type, needs_evidence Y/N) |
| 4 | Research primary sources; verify each claim (section 5) | `RESEARCH_DOSSIER.md` + `evidence/<publisher>/` |
| 5 | Align narration timestamps (ASR word times from the final voice take; do not use the draft script's times) | `beats.csv` with t0/t1 |
| 6 | Design storyboard (sections 3-4) | `STORYBOARD.md` (scene spec per beat) |
| 7 | Choose visual approach per beat (section 3 table) | column in storyboard |
| 8 | Exact asset inventory (section 10 decision: generate / draw / procedural / acquire / screenshot / reuse) | `ASSET_INVENTORY.csv` |
| 9 | Generate coherent original assets (Codex for artwork; Claude for procedural) | `assets/` + provenance row each |
| 10 | Assign responsibilities (section 11) | handoff doc per owner |
| 11 | Prepare transparent layers / rig (section 6) | layer files + anchor json |
| 12 | Capture authentic sources (section 5) | `evidence/` with URL, date, sha256 |
| 13 | Animation spec (section 8) per scene | in storyboard |
| 14 | Render 15-20 s proof of the hardest beats; independent review; fix (max 2 loops) | `out_proof/` |
| 15 | Fix material defects only | change log |
| 16 | Render full video in segments | `out_full/` |
| 17 | Independent QA: separate reviewer, frames + claims + decode (section 12) | QA report |
| 18 | Preserve: sha256 manifest, local git checkpoint (no push without owner) | manifest |
| 19 | Write lessons back into the KB (section 14) | KB addendum |

## 2. What the 13 scanned long-forms show (use as priors, not templates)
[M] pooled over 2,052 shots: median shot 2.87 s (IQR 1.9-4.4); per video 12-24 hard cuts/min; states (any visual change) 19-53/min; only hard cuts, POP_IN and POSE swaps, TEXT_SWAP, SCREEN_SWAP, ZOOM_IN, MICRO, ANIM (`CH/LONGFORM_RHYTHM_STATS.md`).
[M] evidence-type graphics (charts, screenshots, logos, photos) appear in 3-10 states/min.
[O] Same visual register end to end: hand-drawn flat vector on white, one focal subject per beat, a recurring simple character, real screenshots dropped into the same white canvas.

## 3. HOW TO THINK THROUGH A BEAT (core method)
For every narration sentence answer, in writing, these ten questions (this is the storyboard's reasoning log):
1. What does the narrator say? 2. What concept must the viewer take away? 3. What job must the visual do (see function list)? 4. What will literally be on screen? 5. Does it add information the words do not? (If not, is it deliberate emphasis or a reset?) 6. What is deliberately left out? 7. Why is this a plausible visual (one sentence)? 8. How does it lead into the next beat? 9. What is the original, topic-specific construction? 10. How will I verify it?

**Visual functions** (pick one primary per beat): LITERAL (show the thing), METAPHOR (one object stands for an idea), NUMBER (attributed figure), COMPARISON (two scaled elements), EVIDENCE (real source proves a claim), HISTORY (timeline/before-after), DIAGRAM (process in stages), EXAMPLE (a person/prop in a mini-story), REACTION (character emotion), CONTRAST/JOKE, TEXT-ONLY (a phrase on white: "Then came 2008."), RESET (new subject to refresh attention / chapter card).

**Conditional rules** (each: trigger -> treatment; evidence; confidence). Frequencies come from `CH/BEAT_STATS.md` (1,437 narration sentences x visual states in the same time window, ASR unverified, correlational):
| ID | Trigger in narration | Treatment | Evidence | Conf. |
|---|---|---|---|---|
| R-N | Sentence contains a number, %, $ amount | Show the number as large text or on a real/drawn chart; red hand-drawn ring/arrow on the figure | evidence graphic in 60% of number sentences vs 39% base (lift 1.5); callout lift 2.0 | MED [M] |
| R-D | A date or "N years ago" | Year text/timeline strip or period-specific picture; evidence lift 1.4 | [M] | MED |
| R-Q | Question ("why", "how", "what") | Character or text card, fewer evidence graphics (lift 0.7); question marks or a board with the question | [M]+[O] | MED |
| R-C | Contrast ("but", "actually", "instead") | Character beat (lift 1.2) or strike-through of the wrong claim, then the correct one | [M]+[O] holdout 7uu6 "Centralized Exchange" struck | MED |
| R-X | Cause ("because", "which means") | Object/map and character (objects lift 1.4, maps 2.3) showing the mechanism | [M] | LOW (small n) |
| R-E | "Imagine / for example" | Literal staged example with props (evidence lift 2.1 on n=6: too small to trust) | [M] | LOW |
| R-S | A claim about a named organisation or "X said" | Authentic source (article headline, filing, website) cropped to the passage, then highlight | [O] 95 labelled callouts across 13 videos | MED |
| R-T | Short rhetorical beat ("Then came 2008.", "By 2010...") | Text-only line centered on white, no other element | [O] holdout 7uu6 | MED |
| R-H | Section change | Hard cut to a new subject; sometimes a titled card ("Chapter 3 ...") | [O] holdout 7uu6 | LOW |
| R-M | Abstract money idea (debt, bubble, credit) | One concrete object metaphor (machine with labeled inputs, tower, jar), never a dashboard | [O] 7uu6 CDO machine | MED |
Rules are conditional defaults. Override when the claim needs something else, and record why.

**What the channel avoids [O]**: generic dashboard widgets, stock footage montages with no point, decorative imagery unrelated to the sentence, constant camera moves, continuous idle bob on characters.

## 4. Storyboard scene spec (use this exact template; one block per scene)
```yaml
scene_id: S012
audio: {start: 41.20, end: 46.80}
narration: "Commercial bankruptcies have risen over 7%..."
claim_ids: [C-14]
purpose: EVIDENCE            # one function from section 3
concept: "reported change in business filings"
visual_concept: "dark article card with the 7.1% passage ringed; money character sad at bottom-left"
composition: {canvas: white, focal: article card center 60% width, secondary: character bottom-left 15%}
background: white #FDFDFD
main_subject: "cropped real source passage (evidence/... sha256)"
character: {pose: arms_down, head: worried}
layers: [bg, article_crop, ring_red, character_body, character_head, source_tag]
real_evidence: {file: evidence/x/y.png, url: ..., retrieved: 2026-..., passage: "7.1% increase"}
on_screen_text: ["7.1% increase"]   # only if not already legible in the crop
hierarchy: [ring_target, article_headline, character]
animation: [{t: 0.00, op: cut_in, layer: article_crop}, {t: 2.0, op: reveal, layer: ring_red}]
camera: static
transition: {in: hard_cut, out: hard_cut}
sound: voice only (+ optional soft pop at ring)
licensing: "screenshot of public article, attribution tag bottom-left; fair-use note in dossier"
acceptance: ["number legible at 25% frame height (phone)", "ring lands on the spoken figure within 0.3 s of the word", "source tag present"]
```
**Worked example A (reference, [M]+[O], yViMyIVOHkQ, state S221 ~275.8 s):** narration: "commercial bankruptcies have risen over 7%". On screen: dark Google-style answer card quoting "7.1% increase in business filings", entered by hard cut with a tower and a sad banknote character drawn in the empty margins; the complete red ellipse first appears at frame 6667 around "7.1% increase". Evidence frames: `CH/EVIDENCE_FRAMES/sheetA.jpg` (bottom row).
**Worked example B (reference, dPoDyl9Ys38 S242, ~311.7 s):** narration "2% of addresses control 95% of the supply". A real article page (title + body) cuts in on white; a yellow marker highlight appears over exactly "2% of addresses control 95% of the supply" (sheetA top row). Highlight = a separate layer, full-width of the phrase.
**Worked example C (reference, DKyJABtbF2o S132, ~404 s):** the article crop shows the seven-stock list; a red ellipse around the 36% sentence appears ~3.9 s after entry (sheetB bottom row).
**Worked example D (our production, V1 Rent R9b ~247.9-253.7 s):** the on-screen wording must not contradict the narration's subtlety: "each home is repriced every six months" + "the index itself is published every month". Lesson: when a fact is subtle, put the subtlety on screen as two short lines.

## 5. RESEARCH-TO-EVIDENCE workflow
1. Mark claims needing evidence: every figure, every statement about an organisation/person, every causal claim, every "X said".
2. Find primary sources (agency release/table, filing, company page, dataset). Prefer the publisher's own page over a news summary.
3. Verify the actual published value (read the page; record the figure and the exact wording).
4. Capture legitimately: browser screenshot of the real page, official CSV download, or official chart export. Never bypass access controls. If blocked (e.g. HTTP 403): do not claim you read it; use another primary source or a clearly attributed redrawn chart from a data file you hold (V1 Rent: Zillow methodology page returned 403, so no on-screen claim used it).
5. Preserve originals untouched: `evidence/<publisher>/<file>` + manifest with URL, title, retrieved date, version/vintage, sha256.
6. Identify the exact passage (quote with page position). Do not alter the meaning.
7. Build separate layers from a copy: `crop` (rectangle that keeps headline/source visible when possible), `highlight` (yellow marker rectangle behind/over text), `ring` (red ellipse), `underline`, `arrow`.
8. Animate the layers to the narration (sections 8 and 18). There is NO default delay: set mark onset/complete frames from the verified narration clause. Observed (n=9 events, 5 videos): the mark lands as the number is said (+0.1 s) or at the clause start (up to 1.3 s before the number), or the document arrives already marked. **The earlier "4.8 s after the source enters" rule is RETRACTED** (it measured the next callout-family label within five visual states, across cuts and documents; see `CODEX_CORRECTION_DISPOSITION.md`).
9. Verify: the highlighted words equal the narrated claim; the crop does not hide a qualifier; the source tag names publisher + date.
10. Rights: screenshots of public pages are used in the reference as commentary evidence [O]; rights status [U]. For our productions: keep source tags, keep crop minimal, record fair-use reasoning, and never reuse the reference channel's own animations or third-party cartoon/film clips.
If no authentic page exists for a claim: say so on screen only if material; else draw an original chart from verified data with the number, source and date.

**Scene templates (evidence):** (1) Headline reveal: article crop cut in, headline legible, optional underline of the key clause. (2) Progressive sentence highlight: same page, yellow marker moves sentence by sentence at the words. (3) Document zoom: ZOOM_IN state (reference has 41 CUT+ZOOM_IN evidence states) toward the passage, then ring. (4) Table row emphasis: crop to the table, red ring or marker on the row. (5) Official chart: real chart image, red ring/bracket on the point ("~$300B", "60 bps" in the holdout), plus a small spoken-number label. (6) Organisation/person intro: logo or portrait + name label (holdout "Blackstone" sign on a figure is an original drawing alternative). (7) Two-source comparison: two crops side by side, same scale and colour code per source. (8) Corroboration: three crops enter one after another (0.4-0.7 s stagger), one line of text stating the agreement.

## 6. Character and rig specification (original)
Derived from `CH/22`, `09_CHARACTER_SYSTEM.md`, `V1/V1_RENT_ASSET_VISUAL_DNA.md`, `V1/CODEX_HANDOFF_V2_LONGFORM_RIG.md`, `V1/V1_RENT_LONGFORM_STYLE_RULES.md`.
- [M] Reference host: thin line body, large round head: head/figure height 0.31-0.38, line ~1.6-2.5% of figure height. Expression = head swap; no lip sync (head region changed 11 times in 8 s as instant swaps) [M]. Richer characters (caricatures, map-characters, objects with faces) appear as one-beat story roles [O].
- Our rig: separate head and body layers, stable anchors, >=3 arm poses and >=5 heads (neutral, smile, worried, flat/skeptical, surprised), original identity (never trace the reference), line colour from a fixed palette, phone-readable expression at 110 px head width.
- Layer contract: `body_<pose>.png`, `head_<expr>.png` (transparent, same canvas scale), `anchor.json` {neck_x, neck_y, scale}. Validate with an all-pairings sheet (V1: 15 pairings pass).
- Codex generates artwork from prompts (`PRODUCTION_SYSTEM/ASSET_PROMPTS_BATCH1_FOR_CODEX.md`); Claude validates hashes, anchors, alpha, pairings. Approve poses as a set in one pass; **do not run repeated master-only approval loops** (V1 cost).
- A character appears only when it adds meaning (reaction, mini-story, scale reference).

## 7. Graphic design and typography (original, measured ranges)
- Canvas `#FDFDFD`; ~83% of long-form frames light [M]. A coloured/photographic/dark plate appears when the beat IS the place or a screenshot (12.5% "full" frames).
- Line art: black outlines of irregular hand weight, flat fills, minimal shading. Accent: red only for alarm/callout; one accent per beat.
- Type: hand-lettered/Comic-style for labels and one-line cards, high contrast, large; numbers in a clear numeral face (V1: Caveat Brush so "9" is not read as "q"); source tags in a plain legible face at least 3.4% of frame height, bottom-left. All fonts must be redistributable (V1 used Patrick Hand, Caveat Brush, Atkinson Hyperlegible, all OFL).
- Charts: drawn axes or flat bars on white; same px/unit within one chart, **label a different scale when two charts differ** (V1 defect P2-6); keep one colour per source throughout the video (V1 defect P2-7).
- Numbers: pop in at the final value; no rolling counter (intermediate values would be false).
- Never put a glyph the font lacks (V1: arrow tofu box). Draw arrows as shapes.

## 8. Motion library
Observed [M]/[O]: hard cut (dominant); pop-in (small objects, 3-9 frames); pose/head swap (hard); text swap; screen swap (SCREEN_SWAP); slide-ins of characters; ZOOM_IN on documents; micro-motion (small local change); yellow marker sweep (progressive, ~linear, 2.0 s observed once); red ellipses/underlines/arrows were mostly INSTANT complete marks (observed 4 of 9 events) or pre-placed; progressive red drawing not observed in the 2026-11-22 sample; stepped 24 fps content in a 30 fps file.
Not observed / insufficient evidence [U]: 3D, particles, parallax, rolling counters, eased camera pans, speed ramps, mouth sync. Do not add them.
Parameters: pop-in 3-6 frames at 24 fps; stagger 0.4-0.7 s; callout draw: use instant by default (observed), progressive 0.4-0.8 s only as an editable parameter (V1 style); hold everything else still; ease only a deliberate slide. Holds are a choice: leave still frames still.
Incorrect: idle bob, constant slow zoom, cross-dissolves, animating a number through wrong values.

## 9. Editing and audio
- Rhythm priors (long-form): shot median ~2.9 s, 12-24 cuts/min. Set by meaning, not a quota; a beat may hold 10-25 s while a table is explained.
- Cuts land at sentence/clause starts; the number graphic is on screen before the number is spoken or within 0.3 s [I: aligned with ASR pairs; timing curves unverified].
- Sound [U]: no sound-design verdict is possible from the existing evidence (audio never human-listened). Default: clean voice + optional light music bed; any edited narration seam requires a human listening check before release (V1 had two seams).
- Edited narration: never alter the recorded master; keep edited copies as new files with checksums.

## 10. Asset method decision
| Need | Method | Why |
|---|---|---|
| Recurring character/props with consistent style | Codex image generation -> transparent PNG layers | consistency |
| Simple shapes, arrows, rings, charts, text cards | Procedural vector (Python/PIL or SVG) | exact numbers, editable |
| Evidence page | Authentic screenshot/data file capture | proof |
| Map/flag/logo | Acquire with a licence or draw an original simplified shape | avoid rights issues |
| Reused pose/prop | Existing asset library (`PRODUCTION_SYSTEM/asset_registry.json`) | cheap |

## 11. Responsibilities
Codex: character poses/heads, prop and metaphor illustrations, backgrounds as transparent layers, per prompts with consistency instructions. Claude: research/evidence capture, storyboard, procedural graphics, rig integration, render, QA, manifests. Reviewer (independent): frames + claims, never the author.
Existing production code: `V1/tools/v1r4_render.py`, `v1r4_rig_adapter.py`, `v1r9_render_all.py` (PIL, hard cuts, ffmpeg libx264 crf17); asset pipeline `CH/PRODUCTION_SYSTEM/` (import_assets.py, render_scene.py). Reuse; do not write a new engine.
**Document workflow:** The reusable crop, annotation and zoom renderer is available in section 18.2. Evidence capture and manifest preparation still require review. The proof build validates the resolved rendering payload against the reviewed claim register before building frames. Follow the [render contract](../../productions/doc-animation-proof-01/RENDER_CONTRACT.md) when adapting it to a new episode.

## 12. QA gates
Technical: decode with no errors, resolution/fps/duration, audio length vs video, last word not truncated, hard-cut boundaries clean. Content: every on-screen number has a source tag and matches the register; wording does not overstate (V1: "moves in six-month steps" was ambiguous, an owner decision); no untagged figures if narration promises tags. Visual: phone-size legibility, no clipped descenders, no tofu glyphs, scale labelled, colour per source consistent. Audio: human listening of every edit seam. Independent reviewer must see the final file, not only earlier versions.

## 13. When things go wrong
- Unfamiliar object: draw a simple flat original with a label word; one prop per concept; ask Codex for 2 variants.
- Source page inaccessible: record the denial, use another primary source or a data-file redraw; never fabricate.
- Generated asset fails: fix the prompt once with a measurable correction (e.g. anchor offset, line weight); after two failures redraw procedurally.
- New animation needed: first check section 8 "not observed"; if truly needed, build the smallest layered version and add it to the KB with evidence.
- Existing templates cannot explain a concept: use function RESET + a text-only line, then a metaphor object; test in a 15 s proof.
- Voice and script disagree: the recorded voice governs; update the on-screen text and claim register to the spoken words; flag claims the audio makes that the script did not.
- Claim cannot be verified: remove it from screen; if spoken, mark for the owner and do not publish until resolved.

## 14. V1 Rent lessons (general only; details in `V1/`)
Channel-derived transfer that worked: white canvas, one focal subject, red callout marks, head-swap character, drawn charts with exact numbers, source tags, claim registers, independent QA.
Errors: persistent apartment backdrop and a detailed first character style did not match the channel's white-canvas thin-rig grammar (fixed in R4+); repeated master-asset approval loops; font choices that misrender digits; scale/colour inconsistencies; no authentic imagery (owner rated the result about 60-70%: subjective, not an audience metric); ambiguous wording on a subtle fact; audio edit seams needing a human listen.
Owner preferences recorded: authentic news/webpage evidence with animated highlights; faster imagination in storyboards; do not spend time perfecting isolated assets.

## 15. Known limits
17 of 216 videos are fully scanned (visual only); narration alignment is ASR-based and partly provisional; audio never human-listened; small on-screen text inside screenshots not transcribed; evidence-type counts come from label vocabulary; the rules above are priors from 13 long-forms plus one holdout contact sheet (7uu6qaCGZsY, 24 frames).

## 16. Feedback loop
After each production append to `CH/PRODUCTION_LESSONS.md`: what rule held, what failed, new family seen, owner reaction. Promote a rule to "HIGH" only after it holds in two productions and the reference.

## 17. Added after the fresh-context transfer test (2026-11-22; gaps the test agent reported, see `TRANSFER_TEST_OUTPUT_2026-11-22.md`)
- **True but misleading claims:** if a script sentence is literally defensible but implies more than the data (e.g. a spread presented as a bank's margin), the claim register gets a `misleading_risk` column; show the exact bounded figure on screen (what is measured, over what, source/date) and flag the sentence for the owner. Do not silently "fix" spoken words.
- **Hypothetical numbers:** label as "example" on screen, make arithmetic exactly reconcile (parts sum to the whole), and keep them visually distinct from sourced figures (no source tag, an "example" label).
- **Unsourceable beats** (opinion, "feels like work"): use a character reaction or text line; never a chart that implies data. Record as `no_evidence_by_design`.
- **Periods without authentic screenshots (e.g. 1980s):** redraw a chart from an official data series with source/date, or use a titled text card; do not invent period documents.
- **Two valid official figures:** pick one, state the definition on screen, record the other in the dossier.
- **Competitor/brand pages:** prefer the regulator or data-publisher page; crop minimal, tag the source; log a rights note; if unsure, draw a generic original substitute.
- **Claim register columns:** id, sentence_id, text, type, needs_evidence, source_url, retrieved, value_verified, misleading_risk, status. **Ten-question log:** one short line per question, stored in the scene block as `reasoning:`.


## 18. Closure 2 (2026-11-22): claim gate, document renderer, evidence recipes, proof
**Reading order add-on:** `CLOSURE2/EVIDENCE_FORENSICS_2026-11-22.md`, `CLOSURE2/forensics/EVIDENCE_EVENTS.csv`, `CLOSURE2/CODEX_CORRECTION_DISPOSITION.md`, `CLOSURE2/CLOSURE_REPORT.md`, proof folder `productions/doc-animation-proof-01/`.

### 18.1 Claim-blocking production contract (mandatory between steps 'claim register' and 'storyboard')
Chain: research claim -> supporting evidence (verbatim excerpt + locator + source SHA) -> approved wording -> scene (claim_ids) -> on-screen graphics -> render authorization.
- Statuses: VERIFIED, VERIFIED WITH QUALIFICATION, HYPOTHETICAL, DISPUTED, UNVERIFIED, MISLEADING, REJECTED. UNVERIFIED/MISLEADING/REJECTED block the affected factual scene. Qualified claims carry their qualification in narration and/or visuals. HYPOTHETICAL needs the on-screen label and recomputable arithmetic. DISPUTED needs two sources and an explicit disputed presentation.
- Every VERIFIED claim records ten reviewed checks: definition, population, geography, denominator, units, time period, publication date, dataset vintage, causal vs correlational, comparable measures (each `ok`, or `na` with a note). A source tag is never entailment: evidence must carry a verbatim excerpt that contains each claimed number, defining term and quotation.
- Run `python3 CHANNEL_VISUAL_AUDIT/CHANNEL_001/CLOSURE2/tools/claim_gate.py check claims.json scenes.json` (exit 1 = BLOCKED). For the actual path, run `python3 productions/doc-animation-proof-01/build_proof.py --check`. The render contract binds the exact resolved text, annotations, source capture, graphics geometry and planned cues. Keep new operation types behind the same gate. Scene `on_screen_text` and digit-bearing narration must be licensed by the cited claims' numbers with the same unit (so a dollar amount shown as a percentage is refused).
- Limits: the gate cannot establish truth, spoken number-words are not parsed, and the ten checks and keyword lists are only as honest as the reviewer. See the [operational engineering record](ADAPTIVE_VISUAL_RESEARCH/OPERATIONAL_ENGINEERING_CLOSURE.md) for the regression results.

### 18.2 Authentic document scenes (renderer)
`productions/new-original-video-v1-rent-01/tools/doc_scene.py` + `doc_scene_schema.md`: immutable capture with SHA check, crop/zoom in source pixels with the viewport aspect enforced, annotations in document-local coordinates through one transform with the image, instant or progressive marks, persistence/exit, legibility and required-context guards, wrapped source tag. Integrates with the existing beat engine via `document_item()`. 17 unit tests, including a pixel test that a marker inside the document lands at the transformed position during a zoom.

### 18.3 Evidence animation recipes (from the forensics)
1. Pre-marked entry: card enters with its mark (D04, D06). 2. Instant ellipse on a figure that is on screen (D01, D02, D03, D05). 3. Lead-in hold then reveal: card enters title-only, text plus underline appear in one frame at the clause start (D07). 4. Yellow sweep paced to the clause (D03, 2.0 s). 5. Clause-boundary replacement cut (D07 to second card). 6. Mechanism by chalkboard step list, brand logo identification, 'before/after' number pair with staggered red arrows reused later as a callback (7uu6, OC1y).
Not transferable: third-party film/TV/cartoon clips and pop-culture covers. Do not generalize rates from n=9.

### 18.4 Source acquisition and preservation
Capture the page as an original PNG plus HTML text in `evidence/originals/` with retrieval UTC timestamp and SHA-256; never edit originals; marks are separate layers. BLS and some federal sites refuse automated retrieval (do not bypass; capture manually in a normal browser). Check page date/review date and print them. Crops must exclude logos you have not cleared, keep row labels and units visible, and keep the source tag readable (two lines at about 3.5% of frame height).

### 18.5 Conditional visual selection (adds to the ten-question method)
Official definition or worked example: show the real passage, mark the sentence/figure, then draw an original labelled hypothetical mechanism with the same units. Large comparison of two numbers: one number pair side by side, staggered arrows, reuse as callback. Person/company introduced: identity visual (logo/card) first. Entities and flows (lenders, banks, borrowers): character vignette plus labelled box. Hypothetical numbers: label on screen every time, bars from zero, state assumptions. A static, character-free shot while a dense document is readable.

### 18.6 Proof and limits
`productions/doc-animation-proof-01/out/DOC_PROOF_60s.mp4` (silent, 60 s, planned timing track, audible review PENDING). Not tested: other document types (PDF pages, tables with scrolling), BLS-type captures, tall-page scrolling, mobile viewing on a real phone, narration sync against real speech.

## Adaptive visual research

Read the [master visual DNA](CASUAL_FINANCE_MASTER_VISUAL_DNA.md) and the [adaptive checkpoint](ADAPTIVE_VISUAL_RESEARCH/CONTINUATION_CHECKPOINT.md) for tested variations, scope and unresolved gates.

### Scene and asset acceptance checklist

For each clause produce an editable scene specification with claim ID and status, viewer question, why this visual answers it, cue, duration, layers and z-order, location/crop/anchor, asset ID and provenance, entrance/exit, completion and readability hold, and the bridge to the next explanation. Separate authentic factual evidence from attributable identity imagery, original metaphor and explicitly hypothetical mechanism. Research the source version, author, date, exact passage and scope before locking a mark. When scrolling, specify a legible destination and check when caption, axes and values become fully visible separately from when the page indicator changes. If a publisher passage remains visible under a new explanatory overlay, preserve the exact marked text and give the drawing its own reading area.

For every displayed arrow, multiplier or rate conversion write the actual operands, units, reference period and calculation in the claim register. Show the matching operands next to the arrow. Market cap and investment return are different series requiring different inputs. If a one-month chart follows a year-over-year headline, state the switch in narration and print both bases where their figures occur. Mark illustrative spend trajectories and annualized rate equivalents with the relevant assumption. QA against the actual render-facing scene plus voiced and printed language. For planning examples see [fresh-context storyboards](ADAPTIVE_VISUAL_RESEARCH/TRANSFER_STORYBOARDS_AND_REVIEW.md).
