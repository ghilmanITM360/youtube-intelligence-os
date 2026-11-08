# ORIGINAL RECONSTRUCTION BLUEPRINT — learned techniques from Uumnx2Fo6cE

PURPOSE: how an editor/motion designer can build a NEW, ORIGINAL video using the *general techniques* measured in the source. SOURCE_FORENSIC_DESCRIPTION lives in STATE_BY_STATE_VISUAL_FORENSICS.md; per-state ORIGINAL_PRODUCTION_INSTRUCTIONS live in PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json (507 records, each with source-grounded frame refs, a build instruction and an original image prompt). This file is the system-level layer.

Do NOT reproduce: the source's presenter characters, their faces/hair/outfits, its doodle props, the captured articles/filings/charts/logos, its script, the sponsor segment, the QR code, or the creator's identity. Use fictional topics, original captures you author, and your own characters.

## 1. Art-direction principles
1. Off-white canvas (#FCFCFC-class) with ≥85% negative space on doodle states.
2. One subject per frame; the second element is a number/label; everything else waits for its beat.
3. Marker-weight uniform outline (≈ 0.6–0.9% of frame height), 2–3 flat fills per object, no gradients, no shading.
4. Evidence objects (captures) are rectangles with their own scale; the presenter overlaps their edge, never their centre.
5. Colour is a pointer: red/yellow only for what the viewer must read next.

## 2. Shape and illustration system
Characters: circle head 12–18% of frame height on screen-sized poses, 2 dot eyes, 1-stroke mouth (smile/flat/frown), 3-stroke brow set; stick body, no hands detail; 8 reusable expression heads × 6 body poses × 2 prop-hold variants = 96 swappable parts (the source swaps whole heads/poses on a single frame; 38 pose swaps and 11 expression swaps were measured).
Props: houses (3 styles), towers (grid-window), documents with a coloured label, price tags, money, bag, magnifier, chain, ice block, icons; each as a transparent PNG/SVG with outline baked in.

## 3. Original character directions (pick your own, do not clone)
- Lead presenter: circle head, distinct hair silhouette (e.g. a single swoop), warm neutral skin, a thin pointer prop.
- Two foils of contrasting silhouette (tall/thin; short/round), one "expert" prop (clipboard), one "doubter" (crossed arms).
- Keep ≥1 silhouette-readable difference (head shape OR hair OR prop) between recurring characters.

## 4. Typography scale
Handwritten marker numerals 8–15% frame height for key numbers; headings 4–6% (rounded sans); labels 1.8–3%; capture body text is a texture (1–2%) and must be paired with a highlight if it must be read. Rule: any text the viewer must read ≥ 3% frame height.

## 5. Colour
Canvas #FCFCFC; ink #202020; skin tones from a 3-swatch warm set; accent set: red #D8312B-class, highlighter yellow #F6D743-class, green #3FA34D-class, plus 2 greys for buildings. Dark-capture regime #1E1E1E–#202020 reserved for "document/transcript" blocks (measured: dark UI captures were 15 states, 2.2% of runtime).

## 6. Layout and grid
12-column grid, 5% safe margins; capture panels centred or left/right-docked occupying 50–100% width; presenter docked bottom-right/left with ≥12% crop allowed; callout numbers float on the empty side. Sponsor/CTA block: separate layout system (QR lower right, handwritten offer line lower centre, yellow progress bar 8 px high at the bottom edge).

## 7. Asset categories (inventory in PRODUCTION_ASSET_AND_EDITING_PLAN.md)
Presenter parts, props/icons, capture frames (created by you), chart overlays, drawn-on strokes (highlight/underline/box/curve), text cards, end card, sponsor block.

## 8. Scene-by-scene specifications
One record per state in PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json (507) with style family F1–F11, duration in 24-fps frames, original prompt and build instruction, plus intra-state beats (218) with animation instructions.

## 9. Image-generation prompt guidance
Template: "flat hand-drawn whiteboard-style illustration, off-white background, [subject + count + position], [colour tokens], marker outline, no text except [quoted original text], no logos". Always specify counts and relative positions; request transparent background for props; generate presenters as separate layers.

## 10. Animation/motion instructions (measured behaviours)
- Default: hard replacement on a single frame (370 of 506 state-changing events were 1–2-frame changes).
- Additive entry: the new element appears fully drawn on one frame (233 of 757 reviewed events are typed additive entries); no fade or scale-in.
- Scroll/pan of a capture layer: 15–40 frames at 24 fps, ease-out dominant (reviewer labels ease-out 63 of 169 intervals); content continues scrolling while presenter layer is static.
- Zoom/scale of a capture: 10–30 frames, ease-out or ease-in-out.
- Draw-on strokes (highlight/underline/box/line series): stroke front advances 8–60 px per frame over 3–30 frames; chart curve stroke advanced in ~5 successive segments of ~0.1–0.5 s.
- Handwritten number reveal: one glyph per 1–6 frames.
- Screen-recording cursor: tiny arrow drifting a few px per frame inside captures.

## 11. Frame-accurate transitions
Plan every change as (frame, event) at 24 fps. Hard replace = new layer set on frame N, old removed on frame N. Never cross-dissolve unless the reference technique is a measured motion interval. Do not add black dips (none measured in this source).

## 12. Layering and compositing
Layer order bottom→top: canvas, capture(s), props, presenter, highlight/stroke layer, handwritten number, cursor, progress bar, QR/CTA. Strokes are separate vector/raster layers with write-on masks; captures can scale/pan under a fixed presenter layer.

## 13. Editing rhythm
Mean state 1.6 s, median 1.25 s; 24 state changes/min; shorten to 0.2–0.6 s for gag/animation frames; hold dense captures 6–12 s only if a highlight keeps moving. Insert a pacing break (full-bleed drawn scene or card) about every 90–150 s (observed F9/F7/F10 placements).

## 14. Visual-to-script timing guidance
Large composition changes should start within ±0.25 s of a sentence start (58% in the source vs 10% by chance); small additive/highlight beats follow the phrase they illustrate. Do not copy word-level offsets (no measurable word-sync).

## 15. Production implementation options
(a) After Effects/Premiere-style layered timeline with 24-fps comps; (b) Blender/2D vector or Figma + a code-driven renderer; (c) Remotion/React with SVG strokes and `stroke-dashoffset` draw-on; (d) Canva/Capcut for cut-only variants (no draw-on). Choose by whether you need write-on masks (b/c/a) — avoid claiming which tools the source used (unknown).

## 16. Continuity and QC rules
Same canvas hex, outline weight and font family everywhere; recurring props reused as the same file; presenter pointer always the same length; every capture used must be your own authored mock-up; QC: frame-by-frame diff report must show no unintended pixel changes (≤ 30 px at contrast ≥ 150 outside planned events) and every planned event present.

## 17. Asset inventory
See PRODUCTION_ASSET_AND_EDITING_PLAN.md.

## 18. Originality and rights
Create all characters, props, captures and text yourself; do not re-use screenshots of real articles, news pages, filings, logos, QR codes or sponsor material; fictional data in charts; credit sources only where you actually cite real data. Style learning is limited to non-protectable techniques (flat marker look, additive reveals, highlight draw-on, scale/pan of a document layer). Verify fonts' licences.

## Not verified / limits
Software, rendering pipeline and asset origin of the source are unknown; durations/easing labels for motion are inferred from 4 sampled frames per interval; all narration is ASR-only.
