# STATE-BY-STATE VISUAL FORENSICS — Uumnx2Fo6cE

507 visual states (stable composition intervals between state-changing events). Frames are 0-based decode indices; PTS=(i+1)/24 s. SOURCE_FORENSIC_DESCRIPTION only; original-production text is in PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json and ORIGINAL_RECONSTRUCTION_BLUEPRINT.md.

Labels: OBSERVED = seen in decoded frames (tiles 640x360 / 256x144 — small text not guaranteed readable); INFERRED = reviewer interpretation; narration = ASR_ONLY_NOT_AUDIO_VERIFIED. Every state was reviewed twice (first pass + independent second pass).

## S0000 — f0-0 (0.042-0.042 s, 1 frames, 0.04 s) — shot SH001 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0000.jpg; entry start of video, exit EP0001; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter stick figure at right (x0.73-0.94,y0.25-0.93), brown pointer held diagonally across its body; nothing else.
- **Background:** Blank off-white canvas (#FCFCFC-like).
- **Illustration:** Thick black marker outline, peach flat head fill, scribble hair, dot eyes, smiling mouth, brown pointer stick.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.951 #f3d2b7:0.032 #080504:0.011 #534945:0.004 #9d9794:0.002
- **Hierarchy:** Single figure is the only focal point.
- **Camera/motion:** STATIC 2D; **entry/exit:** Opens the video at frame 0; exits via EP0001 motion as the screenshot reveals.
- **Narration (ASR, unverified):** Last
- **Story function (INFERRED):** Inferred: cold-open one-frame first frame before the first source appears.
- **Continuity:** Same presenter reused in S0001-S0010.
- **Confidence:** MEDIUM; **evidence split:** Observed: figure and blank canvas; one-frame duration.

## S0001 — f13-21 (0.583-0.917 s, 9 frames, 0.38 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0001.jpg; entry EP0001, exit EP0002; second review: OK
- **Objects/placement (OBSERVED):** News-article screenshot centre-left (x0.04-0.70,y0.09-0.92): red top banner, small logo/nav row, large serif headline, byline, social icons, 4 bullet lines, a paragraph. Presenter at right (x0.72-0.97) pointing at the headline.
- **Background:** Full-bleed white web page capture with red header banner.
- **Illustration:** Flat UI screenshot; presenter in thick marker line, peach fill, calm smile, pointer touching headline.
- **Typography:** Headline serif/sans mix ~6% frame height dark grey; body sans ~1.5% grey; banner white on red.
- **Readable text:** It's Now The Strongest Buyer's Market on Record, Driven by the Sun Belt
- **Unreadable/uncertain text:** Bullets, byline, nav menu and body paragraph.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.862 #e2cbbd:0.059 #c62646:0.034 #888384:0.029 #1b1716:0.017
- **Hierarchy:** Headline is largest/darkest and first; red banner second; presenter pointer draws the eye to the headline.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered via EP0001 reveal; ends with EP0002 scroll.
- **Narration (ASR, unverified):** month,
- **Story function (INFERRED):** Inferred: establishes the source article for the 'last month' claim.
- **Continuity:** Continues into S0002-S0005 as the same page scrolls.
- **Confidence:** MEDIUM; **evidence split:** Observed: headline and layout; bullets illegible.

## S0002 — f32-34 (1.375-1.458 s, 3 frames, 0.12 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0002.jpg; entry EP0002, exit EP0003; second review: OK
- **Objects/placement (OBSERVED):** Article screenshot scrolled so the bullet list is at top-left and a green line chart with header sits at bottom (x0.04-0.7,y0.0-0.95); red handwritten '58%' at upper centre-right (x0.52-0.68,y0.19-0.32); presenter right.
- **Background:** Full-bleed white article capture.
- **Illustration:** Handwritten red marker numeral over screenshot; presenter pointer rests on text.
- **Typography:** Red handwritten marker '58%' ~12% height; body sans small grey; chart header bold sans ~2%.
- **Readable text:** 58%; Surplus of Sellers Over Buyers Hits Record High
- **Unreadable/uncertain text:** Bullet text, paragraphs, axis labels.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.877 #dfcec1:0.067 #908e8e:0.034 #171311:0.015 #c91126:0.007
- **Hierarchy:** Red '58%' pops most by colour and size; chart second; presenter third.
- **Camera/motion:** SCROLL; **entry/exit:** Entered by scroll (EP0002); exits by scroll EP0003.
- **Narration (ASR, unverified):** 58
- **Story function (INFERRED):** Inferred: highlights headline statistic 58% while sellers outnumber buyers.
- **Continuity:** Same label persists S0003-S0006.
- **Confidence:** MEDIUM; **evidence split:** Observed: label and chart header.

## S0003 — f45-52 (1.917-2.208 s, 8 frames, 0.33 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0003.jpg; entry EP0003, exit EP0004; second review: OK
- **Objects/placement (OBSERVED):** Article scrolled further: chart header and green line chart centred (x0.03-0.7,y0.3-0.8) with paragraph above and below; '58%' red at upper right of article; presenter right.
- **Background:** Full-bleed article capture.
- **Illustration:** Same as S0002; chart line mint green with axis.
- **Typography:** Red marker '58%'; chart title bold sans; axis labels tiny.
- **Readable text:** 58%; Surplus of Sellers Over Buyers Hits Record High
- **Unreadable/uncertain text:** Axis labels, paragraph text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.882 #e2d2c3:0.064 #9e9e9d:0.031 #191514:0.016 #c70f23:0.007
- **Hierarchy:** Chart plus red 58%; presenter pointer crosses chart.
- **Camera/motion:** SCROLL; **entry/exit:** Between scroll EP0003 and EP0004.
- **Narration (ASR, unverified):** % more
- **Story function (INFERRED):** Inferred: moving the viewer down to the chart evidence.
- **Continuity:** Intermediate scroll between S0002 and S0004.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0004 — f57-67 (2.417-2.833 s, 11 frames, 0.46 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0004.jpg; entry EP0004, exit EP0005; second review: OK
- **Objects/placement (OBSERVED):** Chart settled at upper centre (x0.04-0.7,y0.18-0.5) with explanatory paragraphs below; '58%' at upper right; presenter pointer tip on chart's end (x0.55,y0.3).
- **Background:** Full-bleed article capture.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** 58%; Surplus of Sellers Over Buyers Hits Record High
- **Unreadable/uncertain text:** Paragraph under chart, axis ticks.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.884 #e4d2c3:0.060 #a0a3a1:0.033 #100c0b:0.014 #a42732:0.010
- **Hierarchy:** Chart rise at right and pointer tip.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0004 stop; exit EP0005 additive.
- **Narration (ASR, unverified):** people trying
- **Story function (INFERRED):** Inferred: pointer indicates the record-high end of the line.
- **Continuity:** Final resting layout reused in S0005.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0005 — f68-77 (2.875-3.250 s, 10 frames, 0.42 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0005.jpg; entry EP0005, exit EP0006; second review: OK
- **Objects/placement (OBSERVED):** Same layout as S0004 plus a small red-roofed house icon and a grey office-block icon at lower left (x0.06-0.2,y0.64-0.83).
- **Background:** Article capture.
- **Illustration:** Doodle icons with fine ink outlines and flat colour.
- **Typography:** Same.
- **Readable text:** 58%
- **Unreadable/uncertain text:** Article paragraphs.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.865 #e2d2c3:0.064 #9a9e9d:0.034 #0b0909:0.019 #7d3a40:0.019
- **Hierarchy:** Label and chart, then the new icons.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0005 additive; exit by EP0006 zoom.
- **Narration (ASR, unverified):** trying to sell a
- **Story function (INFERRED):** Inferred: houses and buildings stand for homes for sale.
- **Continuity:** S0004 plus icons; icons continue S0006.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0006 — f106-141 (4.458-5.917 s, 36 frames, 1.50 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0006.jpg; entry EP0006, exit EP0008; second review: OK
- **Objects/placement (OBSERVED):** Zoomed scene: chart wide (x0-0.85,y0.2-0.8); green face-bearing blob top-left (x0-0.22,y0.0-0.6); four grey/black buildings and two houses at lower left; red '58%' at x0.52-0.68,y0.1-0.28; larger smiling presenter at right (x0.73-0.97).
- **Background:** Article capture.
- **Illustration:** Marker-drawn green blob with eyes and smile; grey building icons; presenter bigger smile.
- **Typography:** Red marker '58%'; chart title bold; paragraph small.
- **Readable text:** 58%; Surplus of Sellers Over Buyers Hits Record High; Those places are driving the strongest national buyer's market
- **Unreadable/uncertain text:** Remaining article text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfb:0.770 #d9cbbc:0.093 #5f8c66:0.092 #10120e:0.037 #c11426:0.008
- **Hierarchy:** Smiling presenter and blob; label then chart.
- **Camera/motion:** ZOOM; **entry/exit:** Entered by EP0006 zoom; exit EP0008 animation.
- **Narration (ASR, unverified):** than there were people trying to buy one.
- **Story function (INFERRED):** Inferred: blob = a region/market, buildings = sellers' stock.
- **Continuity:** Zoomed continuation of S0005.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0001 (ADDITIVE_ENTRY, f123) Tiny change at lower right near presenter's hand: a small red mark/pointer tip shifts as the pointer lowers; rest static.

## S0007 — f159-253 (6.667-10.583 s, 95 frames, 3.96 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0008.jpg; entry EP0008, exit EP0012; second review: OK
- **Objects/placement (OBSERVED):** Zoomed chart full width (x0.0-0.95,y0.18-0.8) with paragraph above and below; presenter frowning large at centre-right (x0.45-0.65,y0.4-1.0) holding pointer toward upper right; a small chart end tag at top right. Red arrows appear mid-state (EP0009,0010).
- **Background:** Article capture, no props.
- **Illustration:** Presenter frown with downturned mouth, thick marker line.
- **Typography:** Chart title bold sans; paragraphs sans ~2%.
- **Readable text:** Surplus of Sellers Over Buyers Hits Record High; Those places are driving the strongest national buyer's market in our records, which go back through 2013.
- **Unreadable/uncertain text:** Remaining paragraph text and axis labels.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.864 #e7d3c2:0.069 #9ea6a3:0.034 #0c0908:0.017 #676564:0.016
- **Hierarchy:** Frowning presenter is the strongest focal; chart second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0008; exit EP0012. Micro events EP0009-0011 add and change red arrows during this state.
- **Narration (ASR, unverified):** largest gap Redfin has seen since it started tracking this in 2013.
- **Story function (INFERRED):** Inferred: presenter reacts negatively to the surplus; the red arrows emphasise the sharp rise.
- **Continuity:** Layout reused S0008-S0010 with presenter moved.
- **Confidence:** MEDIUM; **evidence split:** Observed. Sheet tile shows the first frame only; arrows seen in boundary sheets.
- **Intra-state events:** EVI0002 (ADDITIVE_ENTRY, f168) A red double-headed vertical arrow appears at right edge beside the chart end (x~0.93, y~0.45-0.65).; EVI0003 (ADDITIVE_ENTRY, f198) A small red diagonal arrow pointing down-left appears at upper left of the chart (x~0.05, y~0.3).; EVI0004 (NUMBER_OR_LABEL_CHANGE, f212) Tiny change near the chart's right end, where a small cursor/data-tag mark flickers for two frames; red arrows unchanged.

## S0008 — f254-283 (10.625-11.833 s, 30 frames, 1.25 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0012.jpg; entry EP0012, exit EP0014; second review: OK
- **Objects/placement (OBSERVED):** Chart page now with presenter at right (x0.78-0.98) flat neutral mouth; orange highlighter bar over the first words of top line (x0.03-0.1,y0.05); tooltip tag at chart left; rest as S0007.
- **Background:** Article capture.
- **Illustration:** Flat orange highlight band, presenter neutral dash mouth.
- **Typography:** Same plus bold orange-highlighted text.
- **Readable text:** Those places are driving the strongest national buyer's market in our records, which go back through 2013.
- **Unreadable/uncertain text:** Remaining text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.862 #e6d3c1:0.069 #9da79e:0.036 #6d665d:0.018 #0c0807:0.016
- **Hierarchy:** Highlight at top, then chart, then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0012 recomposition; exit EP0014 additive.
- **Narration (ASR, unverified):** By their measure, it's the strongest
- **Story function (INFERRED):** Inferred: highlighting key phrase of source sentence.
- **Continuity:** Next states keep highlight extending.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0005 (NUMBER_OR_LABEL_CHANGE, f263) A tiny cursor and small data tooltip (year and percent) appears at left start of the green chart line (x~0.05, y~0.3).

## S0009 — f284-293 (11.875-12.250 s, 10 frames, 0.42 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0014.jpg; entry EP0014, exit EP0015; second review: OK
- **Objects/placement (OBSERVED):** As S0008 plus a coloured doodle two-storey house with red roof and bushes above the chart at upper centre-right (x0.45-0.67,y0.05-0.32); highlight extends to 'strongest buyer's market'.
- **Background:** Article capture.
- **Illustration:** Detailed doodle house, fine ink line, red roof and green bushes.
- **Typography:** Same.
- **Readable text:** Those places are driving the strongest national buyer's market
- **Unreadable/uncertain text:** Rest of article.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfb:0.825 #dfcfbc:0.084 #868b83:0.045 #211711:0.031 #ca8626:0.015
- **Hierarchy:** House, then highlighted text, chart.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0014; exit EP0015.
- **Narration (ASR, unverified):** strongest buyer's
- **Story function (INFERRED):** Inferred: house = homes in the market.
- **Continuity:** Same layout S0010.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0010 — f294-327 (12.292-13.667 s, 34 frames, 1.42 s) — shot SH001 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0015.jpg; entry EP0015, exit EP0016; second review: OK
- **Objects/placement (OBSERVED):** As S0009 plus second character at lower left (x0.1-0.3,y0.55-1.0): bald tan head, closed-eye smile, green tie, green dollar bill in raised hand; highlight reaches 'in our records, which'.
- **Background:** Article capture.
- **Illustration:** Second figure drawn with tan fill and green tie; dollar bill with $ sign.
- **Typography:** Same.
- **Readable text:** Those places are driving the strongest national buyer's market in our records, which go back
- **Unreadable/uncertain text:** Article body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.788 #decdba:0.098 #81897b:0.052 #18110c:0.044 #cc8a25:0.018
- **Hierarchy:** Money-holding figure and house new; highlight; presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0015; exit EP0016 hard cut.
- **Narration (ASR, unverified):** buyer's market on record.
- **Story function (INFERRED):** Inferred: money-holder represents buyer.
- **Continuity:** Last state before blank-canvas S0011.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0011 — f328-354 (13.708-14.792 s, 27 frames, 1.12 s) — shot SH002 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0016.jpg; entry EP0016, exit EP0017; second review: OK
- **Objects/placement (OBSERVED):** Single full-body stick figure at centre (x0.44-0.6,y0.1-0.95): bent arm toward chin, neutral raised-eyebrow face; nothing else.
- **Background:** Blank off-white canvas.
- **Illustration:** Thick marker outline, peach head, raised brow, thin limbs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.032 #080504:0.011 #958e89:0.002 #4d453f:0.002
- **Hierarchy:** Figure alone.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard cut in EP0016; exit EP0017 motion.
- **Narration (ASR, unverified):** So you'd think that means
- **Story function (INFERRED):** Inferred: rhetorical pause 'So you'd think that means...'.
- **Continuity:** Same presenter as S0000 but now full body at centre.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0012 — f388-404 (16.208-16.875 s, 17 frames, 0.71 s) — shot SH002 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0017.jpg; entry EP0017, exit EP0018; second review: MINOR
- **Objects/placement (OBSERVED):** Bald tan-faced character with big grin and green tie, pointing arm out to the right, at left (x0.15-0.41,y0.25-1.0); large detailed house with red roof, chimney, two bushes and a red 'FOR SALE!' sign at right (x0.47-0.94,y0.25-0.8).
- **Background:** Blank off-white canvas.
- **Illustration:** Fine ink line, red/brown roof, green shrubs; character tan fill with grin and green tie.
- **Typography:** Sign lettering handwritten caps white on red ~3% height.
- **Readable text:** FOR SALE!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.835 #100807:0.057 #ceb8a2:0.057 #627055:0.028 #af3c39:0.022
- **Hierarchy:** House and grin figure share weight; red sign gives a colour accent.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0017 element swaps; exit EP0018 hard replace.
- **Narration (ASR, unverified):** When sellers outnumber
- **Story function (INFERRED):** Inferred: the seller who is happy to sell, for-sale house.
- **Continuity:** Figure type is the tan character from S0010; house reused S0014/S0016.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0013 — f405-433 (16.917-18.083 s, 29 frames, 1.21 s) — shot SH002 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0018.jpg; entry EP0018, exit EP0019; second review: OK
- **Objects/placement (OBSERVED):** Hooded character in grey sweatshirt and dark sunglasses at centre (x0.42-0.62,y0.15-0.95), one hand holding a fan of green banknotes at right of body; nothing else.
- **Background:** Blank canvas.
- **Illustration:** Thick outline, tan head, sunglasses, grey fill hoodie, thin legs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.943 #888d85:0.022 #060504:0.018 #d3baa8:0.013 #44463f:0.004
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0018; hard replace EP0019.
- **Narration (ASR, unverified):** outnumber buyers in a market,
- **Story function (INFERRED):** Inferred: the buyer with cash.
- **Continuity:** Reused as tiny buyer in S0014.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0014 — f434-477 (18.125-19.917 s, 44 frames, 1.83 s) — shot SH002 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0019.jpg; entry EP0019, exit EP0021; second review: MINOR
- **Objects/placement (OBSERVED):** 'Sellers' label top (x0.21-0.34,y0.06-0.14) over a row of six small green-tied figures (x0.11-0.45,y0.2-0.45); 'Buyers' label (x0.22-0.36,y0.5-0.58) above one tiny sunglasses buyer holding cash (x0.3,y0.62-0.9); right: house (x0.53-0.92,y0.35-0.75) with a large tilted yellow price tag showing red '$$$' above it (x0.5-0.73,y0.15-0.42).
- **Background:** Blank canvas.
- **Illustration:** Handwritten caps labels; mini figures; tag drawn as yellow slanted label with red dollar glyphs.
- **Typography:** Handwritten ~6% height black labels; red tag text bold.
- **Readable text:** Sellers; Buyers; $$$
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.857 #c0ae9c:0.043 #130d0a:0.043 #7d5b49:0.041 #e3d536:0.016
- **Hierarchy:** Left diagram: six sellers outnumber one buyer; price tag eye-catching in yellow/red.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0019; micro EP0020 changes tag; exit EP0021.
- **Narration (ASR, unverified):** prices are supposed to come down.
- **Story function (INFERRED):** Inferred: illustrates supply outweighing demand; price falling from $$$ to $20 as sign of buyers' market.
- **Continuity:** Reuses house, buyer from S0012-S0013.
- **Confidence:** MEDIUM; **evidence split:** Observed; tile shows first frame ($$$).
- **Intra-state events:** EVI0006 (NUMBER_OR_LABEL_CHANGE, f461) Yellow price tag on the house changes its red text from '$$$' to '$20' at upper right.

## S0015 — f478-488 (19.958-20.375 s, 11 frames, 0.46 s) — shot SH002 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0021.jpg; entry EP0021, exit EP0022; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter alone left of centre (x0.4-0.57,y0.1-0.95): tan-peach head with messy hair, raised brow, flat mouth, one arm bent at hip, one up.
- **Background:** Blank canvas.
- **Illustration:** Marker outline, peach fill.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.032 #080504:0.011 #938c87:0.002 #4b433d:0.002
- **Hierarchy:** Single presenter face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0021 replace; exit EP0022.
- **Narration (ASR, unverified):** Except they
- **Story function (INFERRED):** Inferred: beat before the 'Except they...' turn.
- **Continuity:** Same pose family as S0011.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0016 — f489-509 (20.417-21.250 s, 21 frames, 0.88 s) — shot SH002 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0022.jpg; entry EP0022, exit EP0024; second review: OK
- **Objects/placement (OBSERVED):** Very large presenter head and torso at left (x0.1-0.5,y0.1-1.0) with furrowed brow; house with red roof right (x0.62-0.9,y0.1-0.5); small leaping stick figure between (x0.52-0.58,y0.45-0.62).
- **Background:** Blank canvas.
- **Illustration:** Head drawn about 1/2 frame height; thick outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.818 #f2d2b8:0.084 #0d0705:0.049 #795a4b:0.027 #b79f85:0.022
- **Hierarchy:** Giant face first, then house, then tiny figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0022; micro EP0023 changes small figure; exit EP0024 to screenshot.
- **Narration (ASR, unverified):** they haven't.
- **Story function (INFERRED):** Inferred: 'they haven't' - house prices have not dropped; small figure might be a falling price.
- **Continuity:** House as S0012/S0014.
- **Confidence:** HIGH; **evidence split:** Observed.
- **Intra-state events:** EVI0007 (POSE_SWAP, f497) The tiny stick figure below-left of the house changes limb pose (arms/legs reposition) while the large presenter and house stay.

## S0017 — f510-513 (21.292-21.417 s, 4 frames, 0.17 s) — shot SH003 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0024.jpg; entry EP0024, exit EP0025; second review: OK
- **Objects/placement (OBSERVED):** Association web page capture: top nav bar, blue menu strip (x0.08-0.92,y0.05-0.12), blue bold headline at left (y0.15-0.3), small article meta, 'Month-Over-Month' and 'Year-Over-Year' bullet blocks, dark-blue infographic thumbnail at right (x0.83-0.93,y0.78-0.98).
- **Background:** Full-bleed white web page.
- **Illustration:** UI screenshot, flat.
- **Typography:** Headline sans bold blue ~4%; body ~1.5% grey.
- **Readable text:** NAR Existing-Home Sales Report Shows 2.0% Decrease in August; Month-Over-Month; Year-Over-Year; 2.0% decrease in existing-home sales
- **Unreadable/uncertain text:** Bullets, infographic numbers, menu.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.896 #186da2:0.032 #569ebb:0.025 #132336:0.025 #adbfc7:0.022
- **Hierarchy:** Blue headline at top-left leads; infographic second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0024 hard replace; exit EP0025 scroll.
- **Narration (ASR, unverified):** Last
- **Story function (INFERRED):** Inferred: cite a second source for housing data.
- **Continuity:** Same page scrolled in S0018-S0020.
- **Confidence:** MEDIUM; **evidence split:** Observed headline.

## S0018 — f535-547 (22.333-22.833 s, 13 frames, 0.54 s) — shot SH003 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0025.jpg; entry EP0025, exit EP0026; second review: OK
- **Objects/placement (OBSERVED):** Same page scrolled: left-aligned text column (x0.2-0.6) with headings 'National Snapshot', 'Total Existing-Home Sales for August', 'Inventory in August', 'Median Sales Price in August', 'Housing Affordability in August' and bullets; logo at top-left.
- **Background:** Full-bleed web page.
- **Illustration:** UI capture.
- **Typography:** Bold section headings ~1.7%, body ~1.2%.
- **Readable text:** National Snapshot; Total Existing-Home Sales for August; Inventory in August; Median Sales Price in August; Housing Affordability in August
- **Unreadable/uncertain text:** Bullet text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.946 #d8d9d9:0.019 #b2b3b4:0.017 #8f9090:0.015 #525557:0.004
- **Hierarchy:** Section headings structure.
- **Camera/motion:** SCROLL; **entry/exit:** Entry EP0025; exit EP0026.
- **Narration (ASR, unverified):** typical American
- **Story function (INFERRED):** Inferred: zero in on the snapshot data.
- **Continuity:** S0017 scrolled.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0019 — f566-630 (23.625-26.292 s, 65 frames, 2.71 s) — shot SH003 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0026.jpg; entry EP0026, exit EP0027; second review: MINOR
- **Objects/placement (OBSERVED):** Magnified text page: headings at left-centre with bullets; text column x0.05-0.65; a yellow highlight appears on the price bullet during the state (frame 631 shows it).
- **Background:** Full-bleed web page.
- **Illustration:** Capture.
- **Typography:** Heading bold ~2%, bullets ~1.6%.
- **Readable text:** Total Existing-Home Sales for August; 2.0% decrease in existing-home sales month-over-month; Inventory in August; Median Sales Price in August; $429,100: Median existing-home price for all housing types; 1.6% increase from one year ago ($422,400)
- **Unreadable/uncertain text:** Longer bullet lines.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #dadada:0.028 #7e7e7e:0.022 #afafaf:0.022 #4b4b4b:0.008
- **Hierarchy:** Median price bullet and heading.
- **Camera/motion:** ZOOM; **entry/exit:** Entry EP0026; exit EP0027 additive presenter.
- **Narration (ASR, unverified):** for about $429 ,000. That's
- **Story function (INFERRED):** Inferred: median price $429,100 anchors the point; highlight emphasises it.
- **Continuity:** S0020 same.
- **Confidence:** MEDIUM; **evidence split:** Observed; highlight arrival inferred from boundary frames.
- **Intra-state events:** EVI0008 (OTHER, f570) Three tiny red specks appear on an article text block (lower-left and right of the text column); too small to identify at sheet scale, possibly annotation ticks or cursor residue

## S0020 — f631-726 (26.333-30.292 s, 96 frames, 4.00 s) — shot SH003 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0027.jpg; entry EP0027, exit EP0028; second review: MINOR
- **Objects/placement (OBSERVED):** Same text page; yellow-highlighted bullet at mid; surprised presenter at right edge (x0.8-0.98,y0.2-1.0): open mouth, raised brows, hand under chin.
- **Background:** Full-bleed web page.
- **Illustration:** Presenter with mouth open as an 'o' shape, thick outline.
- **Typography:** Same.
- **Readable text:** Total Existing-Home Sales for August; $429,100: Median existing-home price for all housing types; 1.6% increase from one year ago ($422,400)-the 38th consecutive month of year-over-year price increases.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.850 #e3d0be:0.077 #87827f:0.039 #181410:0.022 #e2c634:0.013
- **Hierarchy:** Highlight and presenter reaction.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0027; exit hard replace EP0028.
- **Narration (ASR, unverified):** That's the 38th month in a row that prices were higher than the year before.
- **Story function (INFERRED):** Inferred: reacts to the 38-month price rise.
- **Continuity:** Same as S0019 plus presenter.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0021 — f727-793 (30.333-33.083 s, 67 frames, 2.79 s) — shot SH004 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0028.jpg; entry EP0028, exit EP0031; second review: MINOR
- **Objects/placement (OBSERVED):** Web page capture: news logo top-left (x0.1-0.25,y0.05-0.1), paragraph at top with one yellow-highlighted word, chart header 'Surplus of Sellers Over Buyers Hits Record High', mint-green line chart (x0.1-0.76,y0.3-0.7), body text at bottom.
- **Background:** Full-bleed white web page.
- **Illustration:** UI capture, mint-green chart line; yellow highlight marks.
- **Typography:** Chart header bold ~2.5%, body ~1.5%.
- **Readable text:** Redfin News; Surplus of Sellers Over Buyers Hits Record High; Those places are driving the strongest national buyer's market in our records, which go back through 2013.
- **Unreadable/uncertain text:** Chart axes, bottom paragraph.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.934 #d2d7d5:0.027 #a6b0a8:0.023 #807c7b:0.013 #2e2d2c:0.003
- **Hierarchy:** Chart line at centre; header.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0028 hard replace; EP0029 highlight animation inside; exit EP0031 overlay.
- **Narration (ASR, unverified):** We're seeing more than three sellers for every two buyers.
- **Story function (INFERRED):** Inferred: return to first source's chart for the 'three sellers for every two buyers' line.
- **Continuity:** Same page as S0007-S0010 without presenter.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0009 (OTHER, f758) Very small change near the chart's end label at upper right (cursor or data tag); highlighted lines unchanged.
- **Intra-state motion intervals:** EP0029

## S0022 — f825-832 (34.417-34.708 s, 8 frames, 0.33 s) — shot SH004 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0031.jpg; entry EP0031, exit EP0032; second review: OK
- **Objects/placement (OBSERVED):** Chart page behind; overlaid text snippet card at middle (x0.0-0.65,y0.38-0.62) with highlighted bullets (yellow and orange); worried presenter lower right (x0.75-1.0,y0.0-0.9) with frown.
- **Background:** Chart page + snippet overlay.
- **Illustration:** Highlights yellow and orange; presenter worried eyes small, mouth downturned.
- **Typography:** Snippet bold heading ~2%.
- **Readable text:** Median Sales Price in August; $429,100: Median existing-home price for all housing types; 1.6% increase from one year ago ($422,400)-the 38th consecutive month of year-over-year price increases.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.848 #e2d2bd:0.066 #dcb532:0.043 #8b8888:0.026 #231a10:0.017
- **Hierarchy:** Overlay card then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0031; exit EP0032.
- **Narration (ASR, unverified):** up.
- **Story function (INFERRED):** Inferred: brings the earlier price fact back to contrast with the surplus.
- **Continuity:** Snippet is the S0020 text.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0023 — f833-917 (34.750-38.250 s, 85 frames, 3.54 s) — shot SH005 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0032.jpg; entry EP0032, exit EP0035; second review: MINOR
- **Objects/placement (OBSERVED):** Man with round glasses and red tie at right-centre (x0.56-0.71,y0.15-0.95), arm extended holding a tilted white blank board (x0.31-0.57,y0.12-0.5) with a small red dot at its centre.
- **Background:** Blank canvas.
- **Illustration:** Thick outline, hair tuft, thin torso, red tie.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.961 #060404:0.022 #d4c5b9:0.009 #9b7b7c:0.004 #4a4544:0.004
- **Hierarchy:** Board then man.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0032; exit EP0035.
- **Narration (ASR, unverified):** All the easy explanations people usually reach for don't work here.
- **Story function (INFERRED):** Inferred: a pointer to 'All the easy explanations' as a blank board for a list.
- **Continuity:** Board reused in S0024 start.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0010 (TEXT_CHANGE, f876) The small red dot on the white board is replaced by hand-lettered black caps 'REASONS' at the board centre; figure and board outline unchanged.; EVI0011 (HIGHLIGHT_ADD, f897) A red hand-drawn X (two crossing strokes) is struck across the word 'REASONS' on the board.

## S0024 — f918-1023 (38.292-42.667 s, 106 frames, 4.42 s) — shot SH006 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0035.jpg; entry EP0035, exit EP0037; second review: OK
- **Objects/placement (OBSERVED):** Smiling presenter at left (x0.05-0.3,y0.2-0.95) holding pointer toward the page; article capture at right (x0.43-0.9,y0.05-0.92): red logo/nav, large headline, byline, social icons, five bullets. A red rectangle gets drawn around the headline mid-state (EP0036).
- **Background:** White; article on white page.
- **Illustration:** Presenter smiling, thick outline; red marker rectangle drawn over headline.
- **Typography:** Headline light-weight sans ~4.5% dark grey; bullets ~1.3% italic.
- **Readable text:** Investor Home Purchases Fall to Lowest Level Since 2020; Redfin News; Published on May 28th, 2026
- **Unreadable/uncertain text:** Bullet lines, nav items.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.901 #e8d1bf:0.047 #9e9c9d:0.020 #636060:0.019 #0c0908:0.012
- **Hierarchy:** Headline then red rectangle then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0035 hard cut; EP0036 inside; exit EP0037 hard cut.
- **Narration (ASR, unverified):** Earlier this year, investor buying fell to its lowest level since 2020.
- **Story function (INFERRED):** Inferred: investors pulling back - one of the 'easy explanations' to examine.
- **Continuity:** Contrasts with S0023 board.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0012 (DRAW_ON_OR_REVEAL, f978) Thin vertical red stroke completes the right edge of a red rectangular outline drawn around the article headline text (x~0.87,y~0.24-0.36)
- **Intra-state motion intervals:** EP0036

## S0025 — f1024-1044 (42.708-43.542 s, 21 frames, 0.88 s) — shot SH007 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0037.jpg; entry EP0037, exit EP0039; second review: OK
- **Objects/placement (OBSERVED):** Chart slide (centre top): bold two-line title (x0.2-0.75,y0.12-0.2), 'Housing Deficit' and year axis 2019, 2020*, 2021, 2022, 2023, 2024 (y0.3-0.4); house and apartment-block icons lower left (x0.05-0.2,y0.65-0.85); blue badge and tiny house lower right (x0.73-0.97,y0.82-0.9); a single blue bar grows during state.
- **Background:** White slide.
- **Illustration:** Flat vector bars in blue; icons doodle.
- **Typography:** Bold sans black ~3% title, axis ~1.8%.
- **Readable text:** Two decades of underbuilding left a 4.7 million-home gap. In 2024, it finally stopped growing.; Housing Deficit; 2019 2020* 2021 2022 2023 2024; Zillow
- **Unreadable/uncertain text:** Footnote beneath chart.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.946 #0e0c0c:0.016 #464a61:0.013 #cbcbc6:0.013 #818789:0.012
- **Hierarchy:** Bold title then bars area.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0037 hard replace; EP0038 bar grows; exit EP0039.
- **Narration (ASR, unverified):** And it's not just
- **Story function (INFERRED):** Inferred: introduces the housing deficit metric for the 'not just homes' / supply point.
- **Continuity:** S0026 identical with bars.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state motion intervals:** EP0038

## S0026 — f1072-1086 (44.708-45.292 s, 15 frames, 0.62 s) — shot SH007 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0039.jpg; entry EP0039, exit EP0040; second review: OK
- **Objects/placement (OBSERVED):** Same chart slide with five blue bars hanging from axis at y0.4-0.76: 2019 lighter blue 3.8M, 2020 gap, 2021 4.3M, 2022 4.5M, 2023 4.7M, 2024 4.7M darker; icons lower left; badge lower right.
- **Background:** White slide.
- **Illustration:** Bars gradient lighter to darker navy, white value labels.
- **Typography:** Bold sans title; white bold bar labels ~1.8%.
- **Readable text:** Two decades of underbuilding left a 4.7 million-home gap. In 2024, it finally stopped growing.; Housing Deficit; 3.8M; 4.3M; 4.5M; 4.7M; 4.7M
- **Unreadable/uncertain text:** Footnote about 2020 omitted.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.876 #152664:0.044 #0632ac:0.041 #959ba3:0.023 #0f0d0c:0.016
- **Hierarchy:** Bar row then title.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0039; exit EP0040 cut.
- **Narration (ASR, unverified):** homes.
- **Story function (INFERRED):** Inferred: gap plateaued at 4.7M - the statement 'it's not just homes' leading to money.
- **Continuity:** Completes S0025.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0027 — f1087-1092 (45.333-45.542 s, 6 frames, 0.25 s) — shot SH008 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0040.jpg; entry EP0040, exit EP0041; second review: MINOR
- **Objects/placement (OBSERVED):** Single green dollar sign at left (x0.14-0.24,y0.32-0.67); rest blank.
- **Background:** Blank canvas.
- **Illustration:** Thick black outline, fill green.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.981 #3fa43c:0.008 #020e02:0.007 #325a31:0.002 #9d9a9f:0.001
- **Hierarchy:** Single glyph.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0040 replace; exit EP0041 add.
- **Narration (ASR, unverified):** That's why
- **Story function (INFERRED):** Inferred: money counting series.
- **Continuity:** Part of S0028-S0031 series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0028 — f1093-1099 (45.583-45.833 s, 7 frames, 0.29 s) — shot SH008 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0041.jpg; entry EP0041, exit EP0042; second review: MINOR
- **Objects/placement (OBSERVED):** Two green dollar signs side by side at left (x0.14-0.4,y0.32-0.67) same size.
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.962 #41a33e:0.017 #030f03:0.015 #2c5329:0.004 #a19fa2:0.002
- **Hierarchy:** Row.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0041 add; exit EP0042.
- **Narration (ASR, unverified):** That's why prices
- **Story function (INFERRED):** Inferred: progression.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0029 — f1100-1106 (45.875-46.125 s, 7 frames, 0.29 s) — shot SH008 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0042.jpg; entry EP0042, exit EP0043; second review: MINOR
- **Objects/placement (OBSERVED):** Three dollar signs in a row (x0.14-0.56,y0.32-0.67).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.943 #41a43e:0.025 #030f03:0.022 #31562e:0.007 #a4a2a5:0.003
- **Hierarchy:** Row.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0042; exit EP0043.
- **Narration (ASR, unverified):** prices are
- **Story function (INFERRED):** Inferred: progression.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0030 — f1107-1113 (46.167-46.417 s, 7 frames, 0.29 s) — shot SH008 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0043.jpg; entry EP0043, exit EP0044; second review: MINOR
- **Objects/placement (OBSERVED):** Four dollar signs in a row (x0.14-0.73,y0.32-0.67).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.924 #41a43e:0.034 #030f03:0.029 #2f562d:0.009 #a4a2a4:0.005
- **Hierarchy:** Row.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0043; exit EP0044.
- **Narration (ASR, unverified):** are high.
- **Story function (INFERRED):** Inferred: progression.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0031 — f1114-1121 (46.458-46.750 s, 8 frames, 0.33 s) — shot SH008 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0044.jpg; entry EP0044, exit EP0045; second review: MINOR
- **Objects/placement (OBSERVED):** Five dollar signs in a row (x0.14-0.9,y0.32-0.67).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.904 #41a43e:0.042 #031003:0.037 #345832:0.011 #a6a4a7:0.005
- **Hierarchy:** Row of five.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0044; exit EP0045 hard cut.
- **Narration (ASR, unverified):** high.
- **Story function (INFERRED):** Inferred: money piling up ('high').
- **Continuity:** Series end.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0032 — f1142-1181 (47.625-49.250 s, 40 frames, 1.67 s) — shot SH009 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0045.jpg; entry EP0045, exit EP0046; second review: OK
- **Objects/placement (OBSERVED):** Line chart (x0.1-0.95,y0.08-0.85) with title 'Number of Sellers Jumps to 6-Year High' and subtitle; cyan and crimson lines; axis ticks; labels SELLERS 1,534,918 and BUYERS 972,300 at right; presenter head tilted at lower left (x0-0.18,y0.4-0.7) arms flat on left.
- **Background:** White chart capture.
- **Illustration:** Presenter head peach with skeptical brow, arms extended horizontally to the edge.
- **Typography:** Bold sans title ~3% black; labels tiny.
- **Readable text:** Number of Sellers Jumps to 6-Year High; Estimated number of U.S. homebuyers and sellers actively in the market; SELLERS 1,534,918; BUYERS 972,300
- **Unreadable/uncertain text:** Axis values.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.923 #ebd0be:0.040 #979799:0.014 #0a0606:0.012 #6c464d:0.011
- **Hierarchy:** Title then lines then face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0045; exit EP0046.
- **Narration (ASR, unverified):** why they won't come down in a month when
- **Story function (INFERRED):** Inferred: sellers curve above buyers curve.
- **Continuity:** Same chart in S0033-S0034.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0033 — f1186-1189 (49.458-49.583 s, 4 frames, 0.17 s) — shot SH009 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0046.jpg; entry EP0046, exit EP0047; second review: OK
- **Objects/placement (OBSERVED):** As S0032 plus three-house cluster upper right (x0.5-0.95,y0.05-0.28).
- **Background:** White chart capture.
- **Illustration:** Doodle houses.
- **Typography:** Same.
- **Readable text:** Number of Sellers Jumps to 6-Year High
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.894 #e8d0bf:0.044 #6f4c4a:0.022 #9e9893:0.021 #160e0a:0.019
- **Hierarchy:** House cluster at top.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0046; exit EP0047.
- **Narration (ASR, unverified):** the homes
- **Story function (INFERRED):** Inferred: houses = listings.
- **Continuity:** S0034.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0034 — f1193-1260 (49.750-52.542 s, 68 frames, 2.83 s) — shot SH009 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0047.jpg; entry EP0047, exit EP0050; second review: MINOR
- **Objects/placement (OBSERVED):** As S0033 plus a second house cluster at lower centre (x0.24-0.47,y0.51-0.75); a third single house is only briefly visible later in the state.
- **Background:** White chart capture.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** Number of Sellers Jumps to 6-Year High
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.866 #e6d0c0:0.048 #714e49:0.032 #a0978f:0.028 #1c110d:0.026
- **Hierarchy:** Two clusters over the lines.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0047; EP0048 mid; exit EP0050.
- **Narration (ASR, unverified):** homes for sale outnumber the people trying to buy them.
- **Story function (INFERRED):** Inferred: homes for sale outnumber buyers.
- **Continuity:** S0033.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0013 (ADDITIVE_ENTRY, f1200) A single house pops in at lower right near the end of the chart lines.; EVI0014 (ADDITIVE_ENTRY, f1231) A tiny grey-hooded figure with glasses pops in at lower centre-right over the chart lines near the buyers line.

## S0035 — f1261-1314 (52.583-54.792 s, 54 frames, 2.25 s) — shot SH010 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0050.jpg; entry EP0050, exit EP0052; second review: OK
- **Objects/placement (OBSERVED):** Green chalkboard with brown wooden frame at right (x0.38-0.95,y0.1-0.78) bearing white hand-lettered 'Still NOT cheap'; presenter at left (x0.08-0.3,y0.2-0.95) smiling with pointer lowered; at frame 1286 (EP0051) the mouth flips to a frown and the pointer raises toward the board.
- **Background:** White canvas.
- **Illustration:** Chalk-like white lettering, board in flat green/brown; presenter smiling.
- **Typography:** Chalk-style handwriting white ~9% height.
- **Readable text:** Still NOT cheap
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.620 #398440:0.186 #6f534a:0.084 #060503:0.073 #ead1b7:0.037
- **Hierarchy:** Board text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0050 hard cut; EP0051 expression change inside; exit EP0052.
- **Narration (ASR, unverified):** It's also not that borrowing is cheap. Mortgage
- **Story function (INFERRED):** Inferred: affordability point.
- **Continuity:** Mortgage rate boards next.
- **Confidence:** HIGH; **evidence split:** Observed.
- **Intra-state events:** EVI0015 (EXPRESSION_CHANGE, f1286) Presenter's mouth changes from smile to frown and pointer raises toward the board; board unchanged.

## S0036 — f1315-1319 (54.833-55.000 s, 5 frames, 0.21 s) — shot SH011 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0052.jpg; entry EP0052, exit EP0053; second review: MINOR
- **Objects/placement (OBSERVED):** Stack of cream 'MORTGAGE' papers at left (x0.09-0.3,y0.29-0.78): cream pages with red 'MORTGAGE' title and squiggle lines with scribbled signatures at bottom.
- **Background:** Blank canvas.
- **Illustration:** Doodle paper stack, thick ink outline, cream fill, red caps title.
- **Typography:** Red handwritten caps ~3%.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.923 #e7e0c8:0.052 #060402:0.016 #a3655f:0.006 #454139:0.003
- **Hierarchy:** Papers only.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0052 cut; exit EP0053.
- **Narration (ASR, unverified):** Mortgage
- **Story function (INFERRED):** Inferred: topic card for mortgage rates.
- **Continuity:** Papers reused S0037-S0041 and S0049.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0037 — f1320-1325 (55.042-55.250 s, 6 frames, 0.25 s) — shot SH011 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0053.jpg; entry EP0053, exit EP0054; second review: MINOR
- **Objects/placement (OBSERVED):** Papers at left (x0.09-0.3); one dark news card with small thumbnail at upper right (x0.30-0.74,y0.08-0.3).
- **Background:** Blank canvas.
- **Illustration:** Screenshot card cut-in as rectangle.
- **Typography:** Card headline sans ~1.5% light blue-white on dark.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage
- **Unreadable/uncertain text:** Card summary line.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.835 #23252a:0.079 #e6e0c8:0.052 #877475:0.018 #050302:0.016
- **Hierarchy:** Card then papers.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0053 add; exit EP0054.
- **Narration (ASR, unverified):** Mortgage rates
- **Story function (INFERRED):** Inferred: headlines about 7% mortgage.
- **Continuity:** Cards accumulate S0038-S0041.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0038 — f1326-1332 (55.292-55.542 s, 7 frames, 0.29 s) — shot SH011 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0054.jpg; entry EP0054, exit EP0055; second review: MINOR
- **Objects/placement (OBSERVED):** Papers left; two overlapping dark cards at upper right (x0.30-0.96,y0.08-0.4).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage; US mortgage rates brush 7%, weighing on buyers, sellers and further straining a bleak housing market
- **Unreadable/uncertain text:** Card body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.770 #24252a:0.132 #e4dec7:0.054 #7f7477:0.028 #060403:0.017
- **Hierarchy:** Newest card.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0054; exit EP0055.
- **Narration (ASR, unverified):** rates just
- **Story function (INFERRED):** Inferred: stacked evidence.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0039 — f1333-1340 (55.583-55.875 s, 8 frames, 0.33 s) — shot SH011 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0055.jpg; entry EP0055, exit EP0056; second review: MINOR
- **Objects/placement (OBSERVED):** Papers left; three overlapping dark cards (x0.30-0.92,y0.1-0.5).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage; US mortgage rates brush 7%, weighing on buyers, sellers and further straining a bleak housing market; The New Rules for Selling Your Home With Mortgage Rates Near 7%
- **Unreadable/uncertain text:** Card bodies.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.701 #23242a:0.188 #e3ddc7:0.057 #7c7478:0.037 #060404:0.017
- **Hierarchy:** Newest card at lower left.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0055; exit EP0056.
- **Narration (ASR, unverified):** just hit 7%.
- **Story function (INFERRED):** Inferred: stacked evidence.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0040 — f1341-1347 (55.917-56.167 s, 7 frames, 0.29 s) — shot SH011 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0056.jpg; entry EP0056, exit EP0057; second review: MINOR
- **Objects/placement (OBSERVED):** Papers left; four overlapping dark cards (x0.30-0.94,y0.1-0.65).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage; US mortgage rates brush 7%...; The New Rules for Selling Your Home With Mortgage Rates Near 7%; Selling a home just got harder as mortgage rates hit 7%
- **Unreadable/uncertain text:** Card bodies.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.648 #1f2026:0.234 #e5dfc8:0.055 #565053:0.033 #8e8d8f:0.031
- **Hierarchy:** Newest at lower right.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0056; exit EP0057.
- **Narration (ASR, unverified):** 7%.
- **Story function (INFERRED):** Inferred: stacked evidence.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0041 — f1348-1363 (56.208-56.833 s, 16 frames, 0.67 s) — shot SH011 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0057.jpg; entry EP0057, exit EP0058; second review: MINOR
- **Objects/placement (OBSERVED):** Papers left; five overlapping dark cards (x0.30-0.94,y0.1-0.8), newest at bottom centre.
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Same.
- **Readable text:** Struggling U.S. homebuyers, and market, face new hurdles as mortgage rates brush 7%; The Stagnant Housing Market Is About to Face a 7% Mortgage
- **Unreadable/uncertain text:** Other card text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.568 #202127:0.302 #e5dfc8:0.055 #5b565a:0.039 #929295:0.036
- **Hierarchy:** Cascade of cards.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0057; exit EP0058 cut.
- **Narration (ASR, unverified):** Higher
- **Story function (INFERRED):** Inferred: breadth of coverage of 7% mortgage rates.
- **Continuity:** End of series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0042 — f1378-1392 (57.458-58.042 s, 15 frames, 0.62 s) — shot SH012 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0058.jpg; entry EP0058, exit EP0059; second review: MINOR
- **Objects/placement (OBSERVED):** Handwritten 'In theory...' top-left (x0.03-0.2,y0.08-0.15); orange percent coin (x0.11-0.23,y0.28-0.5); green zig-zag arrow rising from lower left (x0.09-0.36,y0.4-0.78); rest blank.
- **Background:** Blank canvas.
- **Illustration:** Marker-drawn arrow green, coin orange with white percent.
- **Typography:** Black handwritten ~6% height.
- **Readable text:** In theory...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.970 #d37f4d:0.011 #59a847:0.008 #110a09:0.006 #c6cf9e:0.005
- **Hierarchy:** Text then coin then arrow.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0058 cut; arrow draws; exit EP0059.
- **Narration (ASR, unverified):** rates are supposed to
- **Story function (INFERRED):** Inferred: theoretical rate increase, upward arrow.
- **Continuity:** Continues in S0043.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0043 — f1424-1430 (59.375-59.625 s, 7 frames, 0.29 s) — shot SH012 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0059.jpg; entry EP0059, exit EP0060; second review: MINOR
- **Objects/placement (OBSERVED):** 'In theory...' and orange coin as S0042; green arrow now longer (x0.09-0.47,y0.28-0.78) pointing up-right; red falling zig-zag arrow (x0.52-0.89,y0.28-0.78) with a small green dollar sign at its right (x0.82-0.89,y0.35-0.65).
- **Background:** Blank canvas.
- **Illustration:** Marker arrows.
- **Typography:** Same.
- **Readable text:** In theory...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.947 #d08c60:0.017 #53a345:0.016 #c8111c:0.010 #0d1309:0.010
- **Hierarchy:** Two arrows contrast.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0059 draw-on; exit EP0060.
- **Narration (ASR, unverified):** —
- **Story function (INFERRED):** Inferred: rates up, prices down 'in theory'.
- **Continuity:** S0042.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0044 — f1467-1478 (61.167-61.625 s, 12 frames, 0.50 s) — shot SH013 (inferred) — F9 full-bleed drawn scene
- **Evidence:** frames/ep_stable/e0060.jpg; entry EP0060, exit EP0061; second review: MINOR
- **Objects/placement (OBSERVED):** Full-bleed underwater blue iceberg illustration: darker blue water with lighter faceted iceberg mass tapering down (x0.2-0.8,y0.0-0.9).
- **Background:** Solid ocean blue.
- **Illustration:** Flat vector gradients, hard-edged facets.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #1b5b95:0.501 #20619f:0.271 #3a84c4:0.092 #2b73b9:0.078 #347bbe:0.059
- **Hierarchy:** Iceberg shape.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0060 pan ends; exit EP0061 hard cut.
- **Narration (ASR, unverified):** deeper.
- **Story function (INFERRED):** Inferred: 'deeper' hidden problem metaphor.
- **Continuity:** Same asset starts in EP0060.
- **Confidence:** MEDIUM; **evidence split:** PAN

## S0045 — f1479-1511 (61.667-63.000 s, 33 frames, 1.38 s) — shot SH014 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0061.jpg; entry EP0061, exit EP0062; second review: OK
- **Objects/placement (OBSERVED):** Lone weathered brown house with red roof and chimney at centre (x0.38-0.62,y0.28-0.72); blank elsewhere.
- **Background:** Blank canvas.
- **Illustration:** Doodle house with texture dots, sagging wood.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.928 #918c6c:0.031 #0a0504:0.026 #664139:0.011 #a7c2bd:0.004
- **Hierarchy:** House.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0061 cut; EP0062 add; exit.
- **Narration (ASR, unverified):** It's a structural problem,
- **Story function (INFERRED):** Inferred: 'structural problem' single home.
- **Continuity:** House reused S0046.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0046 — f1537-1575 (64.083-65.667 s, 39 frames, 1.62 s) — shot SH014 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0062.jpg; entry EP0062, exit EP0063; second review: MINOR
- **Objects/placement (OBSERVED):** Large weathered house at left (x0.12-0.36,y0.28-0.72) plus seven tiny houses in two groups at right (x0.37-0.98,y0.28-0.45).
- **Background:** Blank canvas.
- **Illustration:** Same doodle style, scaled down.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.856 #8c866b:0.056 #100806:0.048 #5b3f39:0.028 #adaf99:0.012
- **Hierarchy:** Big house vs rows.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0062 slide; exit EP0063.
- **Narration (ASR, unverified):** into how the housing market works.
- **Story function (INFERRED):** Inferred: many identical homes.
- **Continuity:** S0045.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0047 — f1576-1617 (65.708-67.417 s, 42 frames, 1.75 s) — shot SH015 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0063.jpg; entry EP0063, exit EP0064; second review: OK
- **Objects/placement (OBSERVED):** Presenter at left (x0.05-0.25,y0.1-0.95) neutral dot-mouth with pointer; green chalkboard right (x0.38-0.95,y0.05-0.8) with white text.
- **Background:** White canvas.
- **Illustration:** Chalk lettering.
- **Typography:** Chalk handwriting white ~8%.
- **Readable text:** How tf did this happen???
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.623 #398440:0.180 #6f544a:0.085 #060503:0.072 #e8d2b7:0.039
- **Hierarchy:** Board text.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0063 cut; exit EP0064.
- **Narration (ASR, unverified):** But to understand how we got here,
- **Story function (INFERRED):** Inferred: question card.
- **Continuity:** Same board style as S0035.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0048 — f1650-1685 (68.792-70.250 s, 36 frames, 1.50 s) — shot SH015 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0064.jpg; entry EP0064, exit EP0066; second review: MINOR
- **Objects/placement (OBSERVED):** Curly grey-haired character with hand raised behind head at right (x0.69-0.89,y0.1-0.95); small blue house with trees to its left (x0.45-0.7,y0.3-0.55).
- **Background:** Blank canvas.
- **Illustration:** Grey curls, tan fill, thinking pose, blue house with green trees.
- **Typography:** Tiny caption appears at lower right.
- **Readable text:** none
- **Unreadable/uncertain text:** small caption text bottom right
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.915 #050607:0.037 #656a66:0.020 #bbbdbd:0.019 #29414d:0.010
- **Hierarchy:** Character then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0064; exit EP0066.
- **Narration (ASR, unverified):** people who already own a home.
- **Story function (INFERRED):** Inferred: homeowner introduction.
- **Continuity:** Same house/figure through EP0066.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0016 (TEXT_CHANGE, f1668) Tiny small-print text appears at the lower right of the frame under the character.

## S0049 — f1699-1792 (70.833-74.708 s, 94 frames, 3.92 s) — shot SH016 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0066.jpg; entry EP0066, exit EP0069; second review: MINOR
- **Objects/placement (OBSERVED):** Government site capture occupying x0.06-0.61: nav bar and logo at top-left, light-blue panel (x0.06-0.30,y0.15-0.65) with bold headline, photo of a smiling older couple before a white house (x0.30-0.61,y0.15-0.65), bold headline text below.
- **Background:** White web page.
- **Illustration:** Photo and flat UI.
- **Typography:** Bold sans black ~3%.
- **Readable text:** Share of Owner-Occupied, Mortgage-Free Homes Up in 2024; Nearly 40% of U.S. Homeowners Did Not Have a Mortgage in 2024
- **Unreadable/uncertain text:** Nav and small meta.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.767 #c5dcef:0.115 #727650:0.042 #b0aba0:0.039 #212b1a:0.038
- **Hierarchy:** Blue panel and photo.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0066; EP0067 micro; exit EP0069.
- **Narration (ASR, unverified):** to the latest data from the U .S. Census Bureau, four in 10 homeowners don't
- **Story function (INFERRED):** Inferred: source for mortgage-free homeowners.
- **Continuity:** S0050.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0017 (DRAW_ON_OR_REVEAL, f1715) Red outline begins around the small site logo at the top-left of a government-site web capture (x~0.06-0.12,y~0.08-0.15); EVI0018 (HIGHLIGHT_ADD, f1734) A red rectangle outline appears around the agency logo at top-left of the page.; EVI0019 (DRAW_ON_OR_REVEAL, f1737) Red outline around the same top-left site logo is extended/finished over six frames; EVI0020 (TEXT_CHANGE, f1755) Red handwritten '4 in 10' appears at upper right of the page.

## S0050 — f1793-1822 (74.750-75.958 s, 30 frames, 1.25 s) — shot SH016 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0069.jpg; entry EP0069, exit EP0071; second review: OK
- **Objects/placement (OBSERVED):** Same page plus red '4 in 10' at upper right (x0.9) and papers MORTGAGE (x0.9,y0.4); yellow highlight over headline; red box on logo.
- **Background:** White web page.
- **Illustration:** Handwritten red text.
- **Typography:** Red handwritten ~8%.
- **Readable text:** 4 in 10; MORTGAGE; Nearly 40% of U.S. Homeowners Did Not Have a Mortgage in 2024
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.704 #cbdce7:0.147 #bbae83:0.052 #736746:0.050 #1a1e10:0.047
- **Hierarchy:** '4 in 10'.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0069; exit EP0071 via X.
- **Narration (ASR, unverified):** don't have a mortgage,
- **Story function (INFERRED):** Inferred: no-mortgage share.
- **Continuity:** S0049.
- **Confidence:** HIGH; **evidence split:** Observed.
- **Intra-state events:** EVI0021 (HIGHLIGHT_ADD, f1806) A red X is drawn across the mortgage papers.

## S0051 — f1823-1833 (76.000-76.417 s, 11 frames, 0.46 s) — shot SH017 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0071.jpg; entry EP0071, exit EP0072; second review: MINOR
- **Objects/placement (OBSERVED):** Single DEBT calendar-and-paper icon at left (x0.15-0.3,y0.39-0.72).
- **Background:** Blank canvas.
- **Illustration:** Doodle red calendar with paper.
- **Typography:** Red caps.
- **Readable text:** DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.968 #e6dfd9:0.015 #100907:0.010 #a93036:0.004 #7f7673:0.003
- **Hierarchy:** Icon.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0071; exit EP0072.
- **Narration (ASR, unverified):** which means no
- **Story function (INFERRED):** Inferred: no debt payments.
- **Continuity:** S0052-S0053.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0052 — f1834-1846 (76.458-76.958 s, 13 frames, 0.54 s) — shot SH017 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0072.jpg; entry EP0072, exit EP0073; second review: MINOR
- **Objects/placement (OBSERVED):** Two DEBT icons side by side (x0.15-0.48,y0.39-0.72).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Red caps.
- **Readable text:** DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.935 #e6e1db:0.030 #0f0807:0.019 #94383c:0.011 #998e8b:0.004
- **Hierarchy:** Pair.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0072; exit EP0073.
- **Narration (ASR, unverified):** means no monthly
- **Story function (INFERRED):** Inferred: recurring bills.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0053 — f1847-1856 (77.000-77.375 s, 10 frames, 0.42 s) — shot SH017 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0073.jpg; entry EP0073, exit EP0074; second review: MINOR
- **Objects/placement (OBSERVED):** Three DEBT icons in a row (x0.15-0.67,y0.39-0.72).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Red caps.
- **Readable text:** DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.902 #e7e1db:0.045 #0f0807:0.029 #94383c:0.017 #9f928f:0.007
- **Hierarchy:** Trio.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0073 added; exit EP0074.
- **Narration (ASR, unverified):** monthly debt payment,
- **Story function (INFERRED):** Inferred: monthly payments.
- **Continuity:** Series.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0054 — f1857-1862 (77.417-77.625 s, 6 frames, 0.25 s) — shot SH017 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0074.jpg; entry EP0074, exit EP0075; second review: MINOR
- **Objects/placement (OBSERVED):** Four DEBT icons in a row (x0.15-0.86,y0.3-0.7), each a red calendar with an overlapping paper labelled DEBT.
- **Background:** Blank canvas.
- **Illustration:** Doodle icons, cream paper, red calendar.
- **Typography:** Red caps.
- **Readable text:** DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.870 #e7e2db:0.059 #0f0807:0.039 #94383c:0.022 #a39694:0.010
- **Hierarchy:** Row of four.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0074 add; exit EP0075 cut.
- **Narration (ASR, unverified):** payment,
- **Story function (INFERRED):** Inferred: repeated monthly bills.
- **Continuity:** Series from S0051.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0055 — f1863-1876 (77.667-78.208 s, 14 frames, 0.58 s) — shot SH018 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0075.jpg; entry EP0075, exit EP0076; second review: OK
- **Objects/placement (OBSERVED):** Grey bank building with triangular pediment, columns and two round-handled doors, centre-left (x0.12-0.45,y0.12-0.9).
- **Background:** Blank canvas.
- **Illustration:** Grey flat fill, thick outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.820 #d6d6d6:0.078 #929292:0.054 #030303:0.042 #4a4a4a:0.007
- **Hierarchy:** Building.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0075 hard replace; exit EP0076 bubble.
- **Narration (ASR, unverified):** no bank to
- **Story function (INFERRED):** Inferred: the lender.
- **Continuity:** Reused S0056, S0067-S0070.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0056 — f1877-1893 (78.250-78.917 s, 17 frames, 0.71 s) — shot SH018 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0076.jpg; entry EP0076, exit EP0077; second review: MINOR
- **Objects/placement (OBSERVED):** Bank at left-centre (x0.16-0.58,y0.28-0.9) plus handwritten speech bubble at upper right (x0.56-0.88,y0.16-0.57) with its tail pointing to the bank.
- **Background:** Blank canvas.
- **Illustration:** Bubble outline black, white fill.
- **Typography:** Handwritten black ~4%.
- **Readable text:** Where's my money?!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.795 #d6d6d6:0.081 #030303:0.059 #929292:0.056 #4a4a4a:0.010
- **Hierarchy:** Bubble then bank.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0076; exit EP0077.
- **Narration (ASR, unverified):** to answer to,
- **Story function (INFERRED):** Inferred: lender lacking payments (no bank to answer to).
- **Continuity:** S0055.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0057 — f1894-1933 (78.958-80.583 s, 40 frames, 1.67 s) — shot SH018 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0077.jpg; entry EP0077, exit EP0078; second review: MINOR
- **Objects/placement (OBSERVED):** Small blue house with trees at left (x0.11-0.5,y0.3-0.55); brown-haired character at right (x0.62-0.84,y0.15-1.0) with hand at chin, furrowed puzzled face.
- **Background:** Blank canvas.
- **Illustration:** Tan face, brown hair, thin limbs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.849 #040405:0.063 #babab3:0.042 #5d5842:0.029 #1f4456:0.017
- **Hierarchy:** Character then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0077 replace; exit EP0078.
- **Narration (ASR, unverified):** and no reason to sell their house unless
- **Story function (INFERRED):** Inferred: homeowner thinking.
- **Continuity:** S0058 same.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0058 — f1934-1967 (80.625-82.000 s, 34 frames, 1.42 s) — shot SH018 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0078.jpg; entry EP0078, exit EP0079; second review: MINOR
- **Objects/placement (OBSERVED):** Same layout as S0057 (house x0.11-0.5; character x0.62-0.85) but the character's arm is out to the side (shrugging), face with raised brow.
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.847 #040506:0.066 #45514a:0.042 #c3ab90:0.024 #afcbda:0.021
- **Hierarchy:** Gesture.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0078 pose swap; exit EP0079.
- **Narration (ASR, unverified):** unless they decide they want to. While
- **Story function (INFERRED):** Inferred: carefree homeowner.
- **Continuity:** S0057.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0059 — f1968-2015 (82.042-84.000 s, 48 frames, 2.00 s) — shot SH018 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0079.jpg; entry EP0079, exit EP0080; second review: OK
- **Objects/placement (OBSERVED):** Dark-haired bow-tie character at left (x0.2-0.4) hand at chin, worried; large red-roof two-storey house with bushes at right (x0.55-0.95,y0.1-0.75).
- **Background:** Blank canvas.
- **Illustration:** Brown skin tone fill, bow tie.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.862 #120c0a:0.061 #b89e84:0.040 #5e6d54:0.022 #a94540:0.015
- **Hierarchy:** Character then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0079; exit EP0080.
- **Narration (ASR, unverified):** While the homeowners who do have a mortgage are
- **Story function (INFERRED):** Inferred: mortgaged homeowner.
- **Continuity:** House as S0012.
- **Confidence:** HIGH; **evidence split:** Observed.

## S0060 — f2016-2047 (84.042-85.333 s, 32 frames, 1.33 s) — shot SH018 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0080.jpg; entry EP0080, exit EP0081; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling presenter at left (x0.08-0.3,y0.15-0.95) with pointer; empty green board with brown frame right (x0.38-0.95,y0.05-0.75).
- **Background:** White canvas.
- **Illustration:** Same board family.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.615 #38843f:0.195 #6f5349:0.084 #060503:0.072 #efd1b7:0.034
- **Hierarchy:** Board then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0080; exit EP0081.
- **Narration (ASR, unverified):** are stuck in what's called a
- **Story function (INFERRED):** Inferred: setting up a term.
- **Continuity:** S0035, S0047.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0061 — f2048-2071 (85.375-86.333 s, 24 frames, 1.00 s) — shot SH018 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0081.jpg; entry EP0081, exit EP0082; second review: MINOR
- **Objects/placement (OBSERVED):** As S0060 with frown and white chalk 'Rate lock' large on board (x0.45-0.9,y0.15-0.4); pointer raised.
- **Background:** White canvas.
- **Illustration:** Chalk text.
- **Typography:** Chalk handwriting white ~10%.
- **Readable text:** Rate lock
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.623 #38843f:0.184 #6f5349:0.084 #060503:0.072 #ebd1b6:0.037
- **Hierarchy:** Chalk text.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0081; exit EP0082.
- **Narration (ASR, unverified):** a rate lock,
- **Story function (INFERRED):** Inferred: key concept named.
- **Continuity:** S0060.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0062 — f2086-2139 (86.958-89.167 s, 54 frames, 2.25 s) — shot SH019 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0082.jpg; entry EP0082, exit EP0085; second review: MINOR
- **Objects/placement (OBSERVED):** Very large laughing presenter at left (x0.0-0.37,y0.05-1.0), mouth open wide, arm raised; dark video-channel page at upper right (x0.48-1.0,y0.0-0.65) with a tab row and two white thumbnail cards partly cut off at the right edge.
- **Background:** White canvas + dark page.
- **Illustration:** Large head, red open mouth.
- **Typography:** Card titles bold dark serif-like sans on white cards ~4%; tab labels small white on dark.
- **Readable text:** It's Just Starting.; Nobody's Reacting.; To Save the Economy... We're About to Break It; America Is Walking
- **Unreadable/uncertain text:** Small stats, durations.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.678 #0e0e0d:0.207 #eed2ba:0.067 #597757:0.028 #a29591:0.020
- **Hierarchy:** Face then cards.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0082; EP0083-0084 micro; exit EP0085.
- **Narration (ASR, unverified):** last video, I explained what this is.
- **Story function (INFERRED):** Inferred: plug for previous video.
- **Continuity:** None.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0022 (EXPRESSION_CHANGE, f2099) The presenter's open laughing mouth changes shape (smaller red mouth) at left; channel page static.; EVI0023 (TEXT_CHANGE, f2120) A tiny line of caption text fades in below the video thumbnails at the lower right.

## S0063 — f2140-2172 (89.208-90.542 s, 33 frames, 1.38 s) — shot SH020 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0085.jpg; entry EP0085, exit EP0086; second review: OK
- **Objects/placement (OBSERVED):** Government report page capture centre (x0.2-0.8,y0.05-0.97): dark-blue banner, small menu, title, left menu, body.
- **Background:** Light page.
- **Illustration:** UI capture.
- **Typography:** Banner serif white ~2%; body ~1%.
- **Readable text:** Board of Governors of the Federal Reserve System; Monetary Policy Report - July 2026; Recent Economic and Financial Developments
- **Unreadable/uncertain text:** Body text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.750 #3c4c5f:0.094 #66788d:0.072 #a5abaf:0.046 #d7dadd:0.038
- **Hierarchy:** Banner.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0085; exit EP0086.
- **Narration (ASR, unverified):** If you didn't see that, it's where homeowners
- **Story function (INFERRED):** Inferred: citing the central bank report on rate lock.
- **Continuity:** S0064.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0064 — f2228-2306 (92.875-96.125 s, 79 frames, 3.29 s) — shot SH020 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0086.jpg; entry EP0086, exit EP0087; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed report page (x0.02-0.97) with left side menu (x0.04-0.3) and body column (x0.3-0.89); one yellow-highlighted phrase in a paragraph, a small figure with chart at bottom; presenter head at lower left (x0.09-0.3,y0.55-1.0) with flat mouth.
- **Background:** White page with blue-grey side margins.
- **Illustration:** Yellow highlight, presenter flat.
- **Typography:** Body serif ~1.7%.
- **Readable text:** Residential investment growth remains weak; Figure 23. Existing home sales
- **Unreadable/uncertain text:** Paragraph.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfc:0.743 #6a7a8d:0.134 #ddd3cc:0.070 #a9a69d:0.044 #1f160d:0.009
- **Hierarchy:** Highlighted line.
- **Camera/motion:** ZOOM; **entry/exit:** EP0086; exit EP0087.
- **Narration (ASR, unverified):** rate far below today's rates, so they don't want to move.
- **Story function (INFERRED):** Inferred: 'rate lock' defined.
- **Continuity:** S0063.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0024 (HIGHLIGHT_ADD, f2230) Short red mark and a yellow highlight strip appear on the right-hand article text column near the top (x~0.8-0.97,y~0.2)

## S0065 — f2307-2389 (96.167-99.583 s, 83 frames, 3.46 s) — shot SH021 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0087.jpg; entry EP0087, exit EP0090; second review: MINOR
- **Objects/placement (OBSERVED):** Chart in light-blue frame (x0.06-0.94,y0.19-0.8): blue line with grey recession band near 2020, axes and year labels, source note and fullscreen button below.
- **Background:** White with blue frame.
- **Illustration:** Flat chart.
- **Typography:** Tiny sans.
- **Readable text:** FRED; 30-Year Fixed Rate Mortgage Average in the United States
- **Unreadable/uncertain text:** Axis, notes.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfd:0.770 #e9f2f7:0.188 #d1d8dd:0.027 #95aab9:0.010 #516e83:0.006
- **Hierarchy:** Line rising.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0087; EP0088-0089; exit EP0090.
- **Narration (ASR, unverified):** The buyers from 2021 are locked in at rates around 3%.
- **Story function (INFERRED):** Inferred: ~3% buyers in 2021.
- **Continuity:** None.
- **Confidence:** MEDIUM; **evidence split:** Observed.
- **Intra-state events:** EVI0025 (NUMBER_OR_LABEL_CHANGE, f2377) The hover-line tooltip jumps to a new position and its date/value text changes slightly on the chart's low area.
- **Intra-state motion intervals:** EP0088

## S0066 — f2395-2408 (99.833-100.375 s, 14 frames, 0.58 s) — shot SH022 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0090.jpg; entry EP0090, exit EP0091; second review: MINOR
- **Objects/placement (OBSERVED):** Large red-roof house with FOR SALE sign at left (x0.17-0.62,y0.2-0.78) and grey-haired character in purple tie at right (x0.68-0.9,y0.2-1.0).
- **Background:** Blank canvas.
- **Illustration:** Grey curly hair, purple tie.
- **Typography:** FOR SALE! in sign.
- **Readable text:** FOR SALE!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.828 #0d0707:0.064 #bdb0a4:0.063 #6f646e:0.024 #ae3b38:0.020
- **Hierarchy:** House then character.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0090; exit EP0091.
- **Narration (ASR, unverified):** Selling means handing
- **Story function (INFERRED):** Inferred: selling.
- **Continuity:** S0012 house.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0067 — f2409-2420 (100.417-100.875 s, 12 frames, 0.50 s) — shot SH022 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0091.jpg; entry EP0091, exit EP0092; second review: MINOR
- **Objects/placement (OBSERVED):** MORTGAGE papers centre-left (x0.2-0.45,y0.3-0.8); bank at upper right (x0.65-0.95,y0.05-0.45).
- **Background:** Blank canvas.
- **Illustration:** Doodle.
- **Typography:** Red caps.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.870 #e1ddce:0.068 #060504:0.027 #979290:0.026 #604a47:0.009
- **Hierarchy:** Papers.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0091; exit EP0092.
- **Narration (ASR, unverified):** handing that cheap
- **Story function (INFERRED):** Inferred: handing cheap mortgage back.
- **Continuity:** S0055.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0068 — f2435-2449 (101.500-102.083 s, 15 frames, 0.62 s) — shot SH022 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0092.jpg; entry EP0092, exit EP0093; second review: MINOR
- **Objects/placement (OBSERVED):** Bank at right (x0.7-0.95,y0.05-0.45) with tiny MORTGAGE papers at its left base (x0.68,y0.35).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Tiny red.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.924 #dbd8d2:0.034 #959392:0.022 #070705:0.015 #595450:0.006
- **Hierarchy:** Bank.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0092 motion; exit EP0093.
- **Narration (ASR, unverified):** back and taking
- **Story function (INFERRED):** Inferred: giving mortgage to bank.
- **Continuity:** S0067.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0069 — f2462-2485 (102.625-103.583 s, 24 frames, 1.00 s) — shot SH022 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0093.jpg; entry EP0093, exit EP0094; second review: MINOR
- **Objects/placement (OBSERVED):** Large MORTGAGE papers lower-left (x0.22-0.41,y0.44-0.86); bank with small paper stack at right (x0.64-0.87,y0.15-0.55).
- **Background:** Blank canvas.
- **Illustration:** Same.
- **Typography:** Red caps.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.860 #e2ddcd:0.075 #080604:0.029 #999390:0.026 #654e4a:0.010
- **Hierarchy:** Large papers.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0093; exit EP0094.
- **Narration (ASR, unverified):** expensive debt at
- **Story function (INFERRED):** Inferred: new expensive mortgage.
- **Continuity:** S0068.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0070 — f2503-2513 (104.333-104.750 s, 11 frames, 0.46 s) — shot SH022 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0094.jpg; entry EP0094, exit EP0095; second review: MINOR
- **Objects/placement (OBSERVED):** As S0069 with highlighted text snippet at upper left (x0.05-0.55,y0.08-0.2).
- **Background:** Blank canvas.
- **Illustration:** Yellow/orange highlighter.
- **Typography:** Sans ~1.5%.
- **Readable text:** Median Sales Price in August; $429,100: Median existing-home price for all housing types; 1.6% increase from one year ago ($422,400)-the 38th consecutive month of year-over-year price increases.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.826 #e2dccb:0.082 #100e0b:0.033 #8c8a88:0.032 #d39933:0.026
- **Hierarchy:** Snippet.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0094; exit EP0095.
- **Narration (ASR, unverified):** prices.
- **Story function (INFERRED):** Inferred: high prices.
- **Continuity:** S0020.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0071 — f2514-2595 (104.792-108.167 s, 82 frames, 3.42 s) — shot SH022 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0095.jpg; entry EP0095, exit EP0096; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling character with red headband and spiky brown hair at left-bottom (x0.12-0.40,y0.1-1.0); grey office tower right (x0.55-0.83,y0.17-0.75).
- **Background:** Blank canvas.
- **Illustration:** Headband red.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.775 #050505:0.075 #878980:0.074 #54504e:0.050 #d6c2a9:0.026
- **Hierarchy:** Character then tower.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0095; exit EP0096.
- **Narration (ASR, unverified):** So homeowners are doing the only thing that makes financial sense, which
- **Story function (INFERRED):** Inferred: homeowners making sense decision.
- **Continuity:** None.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0072 — f2596-2627 (108.208-109.500 s, 32 frames, 1.33 s) — shot SH022 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0096.jpg; entry EP0096, exit EP0097; second review: MINOR
- **Objects/placement (OBSERVED):** Red armchair at centre (x0.35-0.67,y0.24-0.81) with person reclined, head at right, arms crossed.
- **Background:** Blank canvas.
- **Illustration:** Red fill and shading.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.874 #b55251:0.075 #160605:0.024 #8d4344:0.021 #cfbca6:0.006
- **Hierarchy:** Armchair.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0096; exit EP0097 to seal.
- **Narration (ASR, unverified):** which is doing nothing. The
- **Story function (INFERRED):** Inferred: doing nothing.
- **Continuity:** None.
- **Confidence:** MEDIUM; **evidence split:** Observed.

## S0073 — f2641-2677 (110.083-111.583 s, 37 frames, 1.54 s) — shot SH023 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0097.jpg; entry EP0097, exit EP0099; second review: MINOR
- **Objects/placement (OBSERVED):** One circular agency seal centred right (x~0.73,y~0.50, diameter ~0.6 of frame height); left half of canvas empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Navy double-ring seal with house-and-shield glyph, red stars, red monogram; vector logo, not hand-drawn.
- **Typography:** Seal lettering is curved serif caps (navy) around the ring; red serif monogram at centre.
- **Readable text:** FEDERAL HOUSING FINANCE AGENCY (curved on seal); FHFA (red monogram at centre)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.952 #3d406f:0.017 #c4c4da:0.012 #321f26:0.010 #8685a1:0.010
- **Hierarchy:** Seal is the sole object; eye lands on it by size and navy/red contrast against the empty white.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0097 (prior-shard event); ends via EP0099 (ADDITIVE_ENTRY); children: EP0098
- **Narration (ASR, unverified):** that regulates Fannie Mae and
- **Story function (INFERRED):** INFERRED: establishes the regulator being named in the voice-over ('that regulates...').
- **Continuity:** Same seal reused in S0074 (stays at right while logos are added at left).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0026 (ADDITIVE_ENTRY, f2659) A small teal-outlined house emblem plus the word-mark of the first lending company appears at upper left, left of the circular agency seal which stays put on the right.

## S0074 — f2678-2695 (111.625-112.333 s, 18 frames, 0.75 s) — shot SH023 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0099.jpg; entry EP0099, exit EP0100; second review: MINOR
- **Objects/placement (OBSERVED):** Three elements on white: small serif wordmark with house-in-circle glyph upper left (x~0.11-0.48,y~0.16-0.31); larger green-and-teal rounded wordmark with roof glyph left (x~0.09-0.52,y~0.45-0.64); circular agency seal right (x~0.56-0.90,y~0.15-0.78); tiny handwritten caption under the seal (x~0.82-0.93,y~0.80).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Vector corporate logos (teal house glyph + serif word-mark; green roof glyph + rounded sans word-mark) beside navy seal; caption is a tiny scribble.
- **Typography:** Logos: serif and rounded sans; caption: small handwritten black, ~2% height.
- **Readable text:** Fannie Mae; Freddie Mac; FEDERAL HOUSING FINANCE AGENCY; FHFA
- **Unreadable/uncertain text:** Tiny handwritten caption under the seal (~2% height), probably a short sarcastic remark about the names; not reliably legible at this size.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.924 #9ab097:0.028 #484871:0.021 #26252d:0.015 #23afd5:0.012
- **Hierarchy:** Largest teal/green word-mark pulls first, then the seal, then the upper logo; caption is a minor aside.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0099 (ADDITIVE_ENTRY); ends via EP0100 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** and Freddie Mac,
- **Story function (INFERRED):** INFERRED: names the two firms the agency oversees while ASR says 'and Freddie Mac'.
- **Continuity:** Builds on S0073 by adding two logos at left (EP0098, EP0099).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0075 — f2696-2706 (112.375-112.792 s, 11 frames, 0.46 s) — shot SH024 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0100.jpg; entry EP0100, exit EP0101; second review: MINOR
- **Objects/placement (OBSERVED):** Stacked area chart screenshot (x~0.11-0.88,y~0.08-0.90): title and legend row top-left, y-axis in trillions, x-axis labels 01-26, grey base band, black middle band, blue top band, gold total line rising to the right; end labels 9.4, 2.8, 3.1, 3.5 at x~0.89; source and note footnotes below left.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Clean vector corporate chart screenshot, thin axis lines, no hand-drawing.
- **Typography:** Sans-serif UI chart type; title ~3.5% height black; labels ~1.5-2% grey; note text ~1.3%.
- **Readable text:** Agency Mortgage-Backed Securities; Fannie Mae; Freddie Mac; Ginnie Mae; Total; Trillions; $10.0 ... $0.0; 9.4; 2.8; 3.1; 3.5
- **Unreadable/uncertain text:** Footnote lines (Sources: ..., Note: ...) and year tick labels are tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.804 #c4c4c2:0.086 #030304:0.052 #4c98c5:0.033 #808177:0.026
- **Hierarchy:** Eye hits the black/blue bands and the large title top-left; then the end labels at right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0100 (FULL_REPLACE); ends via EP0101 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** the two government
- **Story function (INFERRED):** INFERRED: shows the scale of the backed-loan market while the narrator says '$6.6 trillion'.
- **Continuity:** Same chart frame persists through S0076-S0079 with different overlays.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0076 — f2718-2750 (113.292-114.625 s, 33 frames, 1.38 s) — shot SH024 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0101.jpg; entry EP0101, exit EP0102; second review: MINOR
- **Objects/placement (OBSERVED):** Same chart as S0075 in the same position (x~0.12-0.86,y~0.10-0.85) with a green cartoon country-shaped character entering from the left edge (x~0.0-0.20,y~0.09-0.64), round worried eyes and open mouth, overlapping the y-axis labels.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Chart vector; map character hand-drawn green fill, thick black outline, two big round worried eyes, small mouth, stubby legs.
- **Typography:** Same chart type as S0075.
- **Readable text:** Agency Mortgage-Backed Securities; Fannie Mae; Freddie Mac; Ginnie Mae; Total; $10.0...$0.0
- **Unreadable/uncertain text:** Footnotes and tick labels too small.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.761 #c1c0bd:0.091 #56905a:0.058 #030604:0.056 #4d98c5:0.033
- **Hierarchy:** Green character is the only saturated element, pulling the eye left; then the black band.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0101 (ADDITIVE_ENTRY); ends via EP0102 (ELEMENT_EXIT); children: none
- **Narration (ASR, unverified):** -backed companies standing behind $6
- **Story function (INFERRED):** INFERRED: personifies the country reacting to the figure; accompanies '$6' of '$6.6 trillion'.
- **Continuity:** Characters re-used from S0073-era map character in S0113, S0124-S0125, S0135-S0139 (same drawn asset).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: character overlaps chart left edge; INFERRED: it is mid/after slide-in (EP0101)

## S0077 — f2760-2770 (115.042-115.458 s, 11 frames, 0.46 s) — shot SH024 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0102.jpg; entry EP0102, exit EP0103; second review: MINOR
- **Objects/placement (OBSERVED):** Chart only (x~0.12-0.86,y~0.10-0.85), identical to S0076 without the character; end labels 9.4, 2.8, 3.1, 3.5 at x~0.87-0.9; footnotes below left.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Vector chart, no doodle.
- **Typography:** Sans chart type.
- **Readable text:** Agency Mortgage-Backed Securities; Fannie Mae; Freddie Mac; Ginnie Mae; Total; 9.4; 2.8; 3.1; 3.5
- **Unreadable/uncertain text:** Footnotes tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.804 #c4c4c2:0.086 #030304:0.052 #4c98c5:0.033 #808177:0.026
- **Hierarchy:** Black and blue bands, then title.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0102 (ELEMENT_EXIT); ends via EP0103 (PARTIAL_REPLACE); children: none
- **Narration (ASR, unverified):** .6 trillion
- **Story function (INFERRED):** INFERRED: brief breath on the chart between '.6 trillion' words; 11 frames (0.46 s).
- **Continuity:** Same chart position as S0075/S0076; precedes the S0078 money-sack overlay.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0078 — f2771-2820 (115.500-117.542 s, 50 frames, 2.08 s) — shot SH024 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0103.jpg; entry EP0103, exit EP0104; second review: MINOR
- **Objects/placement (OBSERVED):** Chart (x~0.12-0.86,y~0.10-0.85) whose grey and black bands are replaced by a tiled pattern of olive money-sack doodles with yellow dollar signs (x~0.16-0.84,y~0.39-0.67); blue band, gold line, axes and end labels remain.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn green sacks with yellow dollar signs, thick black outlines, olive fill, tiled in rows under the chart line.
- **Typography:** Same chart sans type.
- **Readable text:** Agency Mortgage-Backed Securities; Fannie Mae; Freddie Mac; Ginnie Mae; Total; 9.4; 2.8; 3.1; 3.5
- **Unreadable/uncertain text:** Footnotes tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.811 #6e8469:0.087 #131a0b:0.040 #4d98c5:0.033 #baba84:0.029
- **Hierarchy:** Bright yellow dollar signs on dark bags dominate the lower half; title second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0103 (PARTIAL_REPLACE); ends via EP0104 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** trillion of American home loans,
- **Story function (INFERRED):** INFERRED: literalises 'trillions of home loans' as piles of money.
- **Continuity:** Overlay carries into S0079; chart base from S0075.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0079 — f2821-2840 (117.583-118.375 s, 20 frames, 0.83 s) — shot SH024 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0104.jpg; entry EP0104, exit EP0105; second review: MINOR
- **Objects/placement (OBSERVED):** Money-sack chart (x~0.12-0.86,y~0.10-0.85) with a smiling stick presenter at lower right: round beige head with curly black hair (x~0.73-0.94,y~0.43-0.67), thin arm reaching to x~0.95, body line running down to the frame bottom.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Chart vector plus hand-drawn bags; presenter: round beige head, black outline, two dot eyes, curved smile, thin black stick limbs.
- **Typography:** Chart sans type.
- **Readable text:** Agency Mortgage-Backed Securities; Fannie Mae; Freddie Mac; Ginnie Mae; Total; 9.4; 2.8; 3.1
- **Unreadable/uncertain text:** Footnotes tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.779 #75876a:0.085 #e1cfb0:0.058 #11160b:0.044 #4d98c5:0.033
- **Hierarchy:** Presenter face and bags compete; face is the larger flat-colour shape so reads second after the yellow $.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0104 (ADDITIVE_ENTRY); ends via EP0105 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** measured it.
- **Story function (INFERRED):** INFERRED: presenter signals the transition to the next claim ('measured it').
- **Continuity:** First appearance in this shard of the black-spiky-hair presenter drawn bust-only (see S0081, S0090).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0080 — f2841-2861 (118.417-119.250 s, 21 frames, 0.88 s) — shot SH025 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0105.jpg; entry EP0105, exit EP0106; second review: MINOR
- **Objects/placement (OBSERVED):** Web-page screenshot centred (x~0.22-0.78,y~0.0-0.94): blue header band with seal glyph, agency name and nav row, white page with red 'Staff Working Papers' kicker, blue serif title, small author line and dense abstract; blue accessibility icon at lower right of page.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real browser capture, no doodles; blue header band top.
- **Typography:** Header sans white on blue; title serif blue ~3% frame height equivalent; body tiny grey-black.
- **Readable text:** U.S. FEDERAL HOUSING; Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; Staff Working Papers
- **Unreadable/uncertain text:** Abstract body, author line and footer links are illegible at this scale.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.830 #0e71ae:0.054 #94969b:0.041 #c7cacf:0.040 #0a4575:0.034
- **Hierarchy:** Blue header and blue title draw the eye; the rest reads as a text block.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0105 (FULL_REPLACE); ends via EP0106 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** They found that for every
- **Story function (INFERRED):** INFERRED: establishes the primary-source study referenced ('They found...').
- **Continuity:** Same document reused as zoomed views in S0081-S0099 and again at S0089/S0091.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0081 — f2881-3007 (120.083-125.333 s, 127 frames, 5.29 s) — shot SH025 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0106.jpg; entry EP0106, exit EP0107; second review: OK
- **Objects/placement (OBSERVED):** Enlarged document (x 0.12-0.98,y 0-1) cropped to the title and abstract; yellow-orange highlight on one phrase (x~0.5,y~0.55); presenter bust at left (x~0.0-0.22,y~0.15-0.7) with a thin pointer stick crossing the text.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Document: serif blue headline and grey body; presenter hand-drawn: round beige head, black spiky hair, two dot eyes, curved smile; thin stick body.
- **Typography:** Headline serif blue ~6% height; body sans ~2% dark grey; highlight orange.
- **Readable text:** Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; This paper finds ...
- **Unreadable/uncertain text:** Abstract paragraph text partly readable only in fragments.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.791 #e0d1c6:0.095 #9d9b9a:0.059 #6a6b6e:0.041 #0c0a0b:0.014
- **Hierarchy:** Large blue headline top, then orange highlighted phrase, then presenter face left.
- **Camera/motion:** ZOOM in on document (entering via EP0106); static within the state afterwards; **entry/exit:** Begins via EP0106 (ZOOM_OR_SCALE); ends via EP0107 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** rate sits above the rate an owner already has, the odds they sell fall by about 18%. Between
- **Story function (INFERRED):** INFERRED: the highlighted sentence is the study's finding the narrator quotes ('odds they sell fall by about 18%').
- **Continuity:** Same enlarged view as S0090; presenter from S0079/S0090.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: zoomed page, highlight, presenter; INFERRED: which sentence is quoted in ASR

## S0082 — f3035-3112 (126.500-129.708 s, 78 frames, 3.25 s) — shot SH025 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0107.jpg; entry EP0107, exit EP0108; second review: OK
- **Objects/placement (OBSERVED):** Document (x 0.05-0.98,y 0.02-1) at medium zoom: dark-blue rule across the top, red kicker, blue serif title top-left, bold dateline and author lines, abstract with yellow highlight over two lines (x~0.45-0.95,y~0.54-0.63).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real article capture; neon-yellow highlight bars.
- **Typography:** Serif blue title ~5% height; body grey sans ~1.8%; kicker red caps.
- **Readable text:** Staff Working Papers; Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; Published: 03/18/2024; Author(s): Ross M. Batzer, Jonah R. Coste, William M. Doerner, and Michael J. Seiler; Abstract: ...
- **Unreadable/uncertain text:** Remaining abstract sentences are small; only partly legible.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.785 #0b4272:0.067 #d0d3d3:0.058 #9ea19d:0.050 #6f7273:0.041
- **Hierarchy:** Blue title then yellow highlight bar.
- **Camera/motion:** Zoom-in settling from EP0107, then static; **entry/exit:** Begins via EP0107 (ZOOM_OR_SCALE); ends via EP0108 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** 2022 and the end of 2023, they estimate that wiped out 1
- **Story function (INFERRED):** INFERRED: highlights the study's headline sales-lost sentence while ASR says 'wiped out 1'.
- **Continuity:** Same view continues through S0083-S0086 with overlays.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0083 — f3113-3123 (129.750-130.167 s, 11 frames, 0.46 s) — shot SH025 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0108.jpg; entry EP0108, exit EP0109; second review: MINOR
- **Objects/placement (OBSERVED):** Same document as S0082 plus one doodle cluster at left (x~0.09-0.34,y~0.33-0.60): small cream house with red roof, grey tower block with window grid, red 'SALE' sign on a post at its lower right.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn doodles: thick black outline, cream and grey flat fills, red sign with white 'SALE' marker text.
- **Typography:** Doc type as S0082; sign lettering handwritten white caps on red.
- **Readable text:** Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; Published: 03/18/2024; SALE (on sign)
- **Unreadable/uncertain text:** Body text tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.745 #123e64:0.084 #817f7c:0.075 #c6c8c6:0.063 #e6e22c:0.032
- **Hierarchy:** Doodle cluster overlapping the abstract draws the eye first (saturated red sign), then title.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0108 (ADDITIVE_ENTRY); ends via EP0109 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** out 1 .7
- **Story function (INFERRED):** INFERRED: houses-for-sale icons illustrate 'home sales' while ASR says 'out 1 .7'.
- **Continuity:** Cluster repeated in S0084 (x2) and S0085 (x3).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0084 — f3124-3136 (130.208-130.708 s, 13 frames, 0.54 s) — shot SH025 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0109.jpg; entry EP0109, exit EP0110; second review: MINOR
- **Objects/placement (OBSERVED):** Document with two identical doodle clusters (x~0.09-0.34 and x~0.37-0.62, y~0.33-0.60), each a small house, grey tower and red 'SALE' sign; highlight covers two text lines.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same doodles as S0083; second cluster identical copy.
- **Typography:** As S0083.
- **Readable text:** Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; SALE
- **Unreadable/uncertain text:** Body text tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.719 #153a5b:0.097 #807b77:0.084 #c6c8c4:0.066 #e7e32c:0.034
- **Hierarchy:** Two repeated clusters create rhythm; red signs lead.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0109 (ADDITIVE_ENTRY); ends via EP0110 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** .7
- **Story function (INFERRED):** INFERRED: counting-up beat for '.7' million lost sales (very short, 0.54 s).
- **Continuity:** Intermediate of S0083 and S0085.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0085 — f3137-3169 (130.750-132.083 s, 33 frames, 1.38 s) — shot SH025 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0110.jpg; entry EP0110, exit EP0111; second review: MINOR
- **Objects/placement (OBSERVED):** Document with three identical doodle clusters (x~0.09-0.34, 0.37-0.61, 0.64-0.87; y~0.34-0.61), each a house, grey tower and red 'SALE' sign over the abstract; yellow highlight below.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0083/S0084.
- **Typography:** As S0083.
- **Readable text:** Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates; Published: 03/18/2024; SALE x3
- **Unreadable/uncertain text:** Body text tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.695 #173753:0.111 #817976:0.093 #c8c9c4:0.068 #e7e32c:0.034
- **Hierarchy:** Row of three clusters dominates the middle, red signs as accents.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0110 (ADDITIVE_ENTRY); ends via EP0111 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** .7 million home sales that would
- **Story function (INFERRED):** INFERRED: visualises many lost home sales ('.7 million home sales that would').
- **Continuity:** Third step after S0083 and S0084; they dissolve in EP0111.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0086 — f3186-3196 (132.792-133.208 s, 11 frames, 0.46 s) — shot SH025 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0111.jpg; entry EP0111, exit EP0112; second review: OK
- **Objects/placement (OBSERVED):** Document (x 0.05-0.98,y 0-1) with orange circular percent badge at upper left (x~0.12,y~0.22,d~0.25H) and a green rising arrow's lower segment crossing the text lower left (x~0.03-0.22,y~0.62-0.98); clusters gone.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Badge: orange flat disc, thick black outline, white outlined % sign; arrow: green thick marker stroke with black-less edge.
- **Typography:** Doc as before.
- **Readable text:** Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates (partly hidden by badge)
- **Unreadable/uncertain text:** Body text tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.746 #8a846a:0.084 #0d406c:0.072 #c1c4c2:0.063 #e9e531:0.035
- **Hierarchy:** Orange badge first (high-saturation disc), arrow second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0111 (ELEMENT_SWAP); ends via EP0112 (PARTIAL_REPLACE); children: none
- **Narration (ASR, unverified):** happened,
- **Story function (INFERRED):** INFERRED: introduces interest rates ('happened,') as new subject.
- **Continuity:** Badge/arrow carry into S0087-S0088.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0087 — f3197-3239 (133.250-135.000 s, 43 frames, 1.79 s) — shot SH025 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0112.jpg; entry EP0112, exit EP0115; second review: MINOR
- **Objects/placement (OBSERVED):** Blank canvas with orange percent badge at upper left (x~0.10-0.24,y~0.06-0.33) and a long green zig-zag rising arrow from lower left (x~0.01,y~0.97) to arrowhead at upper right (x~0.45,y~0.31).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Badge flat orange with black outline; arrow thick green marker, hand-drawn zig-zag with arrowhead.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.955 #52b23c:0.019 #d37e4c:0.016 #c4d292:0.006 #140b09:0.005
- **Hierarchy:** Arrow's diagonal sweeps the eye to upper right; badge anchors upper left.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0112 (PARTIAL_REPLACE); ends via EP0115 (ADDITIVE_ENTRY); children: EP0113;EP0114
- **Narration (ASR, unverified):** which caused rising interest rates to have an
- **Story function (INFERRED):** INFERRED: rate-increase symbol; ASR 'which caused rising interest rates'.
- **Continuity:** Same assets as S0086/S0088; screenshot removed at EP0112.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0027 (DRAW_ON_OR_REVEAL, f3206) The upper-right end of the green arrow extends by a short stroke (net change only at the arrow tip).; EVI0028 (DRAW_ON_OR_REVEAL, f3214) An arrowhead is drawn at the upper-right tip of the green arrow, completing the arrow.

## S0088 — f3240-3278 (135.042-136.625 s, 39 frames, 1.62 s) — shot SH025 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0115.jpg; entry EP0115, exit EP0117; second review: MINOR
- **Objects/placement (OBSERVED):** Orange percent badge upper left (x~0.10-0.24,y~0.06-0.33); thick green zig-zag arrow rising from lower left (x~0.0,y~0.95) to arrowhead at upper right (x~0.66,y~0.09); worn olive-brown house with cracked brown roof at lower right (x~0.68-0.88,y~0.43-0.88).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** House: weathered olive-brown, black outline, cracked roof; arrow green; badge orange.
- **Typography:** Handwritten 'ouch' small black.
- **Readable text:** ouch
- **Unreadable/uncertain text:** A small handwritten scrawl near the house may appear in later frames; not visible in this tile.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.900 #b09065:0.040 #51b43b:0.031 #0c0604:0.020 #62433b:0.009
- **Hierarchy:** Arrow and badge first, house second for contrast in colour.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0115 (ADDITIVE_ENTRY); ends via EP0117 (FULL_REPLACE); children: EP0116
- **Narration (ASR, unverified):** an opposite effect on housing.
- **Story function (INFERRED):** INFERRED: rates rising 'hurt' housing; ASR 'opposite effect on housing'.
- **Continuity:** Same badge/arrow as S0087; house new (EP0115).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0029 (ADDITIVE_ENTRY, f3258) A small handwritten word appears to the left of the brown house at lower right, like an exclamation.

## S0089 — f3279-3293 (136.667-137.250 s, 15 frames, 0.62 s) — shot SH026 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0117.jpg; entry EP0117, exit EP0118; second review: MINOR
- **Objects/placement (OBSERVED):** Small web-page screenshot centred (x~0.23-0.77,y~0.0-0.95) with blue header band and nav, red kicker, blue serif title, tiny dense abstract and blue accessibility icon at lower right of the page.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real capture, blue header.
- **Typography:** As S0080.
- **Readable text:** U.S. FEDERAL HOUSING; Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates
- **Unreadable/uncertain text:** Abstract body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.832 #0e71ae:0.052 #cad0d3:0.043 #989da0:0.040 #0c4374:0.033
- **Hierarchy:** Blue header and title.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0117 (FULL_REPLACE); ends via EP0118 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** We saw higher
- **Story function (INFERRED):** INFERRED: return to the source while narrator says 'We saw higher' - 15 frames only.
- **Continuity:** Reuses S0080's page; zooms in EP0118.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0090 — f3312-3362 (138.042-140.125 s, 51 frames, 2.12 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0118.jpg; entry EP0118, exit EP0119; second review: OK
- **Objects/placement (OBSERVED):** Zoomed document text filling frame (x 0-1); presenter bust at right (x~0.60-0.85,y~0.4-1.0) with smile, black spiky hair and a thin raised pointer; small yellow highlight 'which decreased prices by 3.3%' (x~0.2,y~0.55).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn presenter on top of a real article capture.
- **Typography:** Body sans ~2.4% grey; highlight yellow.
- **Readable text:** which decreased prices by 3.3%; These findings underscore how mortgage rate lock-in restricts mobility; Mortgage lock-in data are available below in two formats
- **Unreadable/uncertain text:** Rest of paragraph is partially covered or tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.776 #e5d3c1:0.103 #6f6f6e:0.053 #a5a4a3:0.049 #0a0706:0.019
- **Hierarchy:** Presenter face centre-right first, highlighted phrase second.
- **Camera/motion:** ZOOM in (EP0118) then static; **entry/exit:** Begins via EP0118 (ZOOM_OR_SCALE); ends via EP0119 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** prices by a little over 3%, but
- **Story function (INFERRED):** INFERRED: highlighted '3.3%' matches 'higher prices by a little over 3%'.
- **Continuity:** Presenter layout echoes S0081 (mirrored).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0091 — f3363-3403 (140.167-141.833 s, 41 frames, 1.71 s) — shot SH026 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0119.jpg; entry EP0119, exit EP0120; second review: MINOR
- **Objects/placement (OBSERVED):** Small web-page screenshot centred (x~0.23-0.77,y~0.0-0.95): blue header band and nav, red kicker, blue serif title, tiny dense abstract, blue accessibility icon lower right of page; identical to S0089.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real capture.
- **Typography:** As S0080.
- **Readable text:** U.S. FEDERAL HOUSING; Working Paper 24-03: The Lock-In Effect of Rising Mortgage Rates
- **Unreadable/uncertain text:** Abstract body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.832 #0e71ad:0.052 #c9d0d5:0.042 #989da1:0.041 #0a4476:0.033
- **Hierarchy:** Blue header.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0119 (FULL_REPLACE); ends via EP0120 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** but the results from the supply reduction
- **Story function (INFERRED):** INFERRED: re-establishing the source before the 'supply reduction' claim.
- **Continuity:** Same as S0080, S0089; third use of the small page.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0092 — f3434-3506 (143.125-146.125 s, 73 frames, 3.04 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0120.jpg; entry EP0120, exit EP0123; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed document text fills frame; yellow highlight on 'The supply' (x~0.20-0.28,y~0.20); hand-drawn red-roofed mansion with brown wings and green bushes at lower right (x~0.59-0.77,y~0.54-0.85) overlapping the text; blue accessibility icon at right (x~0.96,y~0.60).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Mansion hand-drawn: cream walls, red roof, brown wings, green bushes, thick black outline.
- **Typography:** Body sans ~2.4% grey; highlight yellow.
- **Readable text:** The supply reduction increased home prices by 5.7%, outweighing the direct impact of elevated rates, which decreased prices by 3.3%
- **Unreadable/uncertain text:** Small text around.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.810 #cacac5:0.061 #989590:0.058 #70655e:0.053 #190e0a:0.017
- **Hierarchy:** Highlighted phrase then mansion.
- **Camera/motion:** ZOOM in (EP0120) then static; small money-bag micro-items added at EP0121/0122; **entry/exit:** Begins via EP0120 (ZOOM_OR_SCALE); ends via EP0123 (PARTIAL_REPLACE); children: EP0121;EP0122
- **Narration (ASR, unverified):** vanished pushed home prices up by nearly 6%. So
- **Story function (INFERRED):** INFERRED: the supply effect pushing prices up (ASR 'pushed home prices up by nearly 6%').
- **Continuity:** Zoom path continues from EP0120; house new, bags cleared at EP0123.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0030 (ADDITIVE_ENTRY, f3445) A small green money-bag doodle appears at lower left of the house over the document text.; EVI0031 (HIGHLIGHT_ADD, f3459) A second tiny bag-like item appears beside the first and the yellow highlight in the text grows slightly longer.

## S0093 — f3507-3548 (146.167-147.875 s, 42 frames, 1.75 s) — shot SH026 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0123.jpg; entry EP0123, exit EP0124; second review: MINOR
- **Objects/placement (OBSERVED):** Scrolled document text across the upper half (x 0-1,y 0-0.45) with yellow highlight on 'These findings' (x~0.64-0.73,y~0.19); blue accessibility icon at right (x~0.945,y~0.55); underlined blue bullet link 'Supplemental data for figures' (x~0.08-0.24,y~0.58); lower half empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real capture; yellow highlight.
- **Typography:** Body sans ~2.4% grey-black; link blue underlined.
- **Readable text:** Supplemental data for figures; These findings underscore how mortgage rate lock-in restricts mobility
- **Unreadable/uncertain text:** Paragraph text is mostly small.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.869 #d4d4d5:0.048 #a2a3a4:0.040 #707377:0.039 #e1db2b:0.003
- **Hierarchy:** Highlighted phrase top-right of text; large empty lower half draws space for overlays.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0123 (PARTIAL_REPLACE); ends via EP0124 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** So by the agency's own measure,
- **Story function (INFERRED):** INFERRED: sets up the 'by the agency's own measure' conclusion.
- **Continuity:** Same scroll position as S0094-S0099.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0094 — f3549-3575 (147.917-149.000 s, 27 frames, 1.12 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0124.jpg; entry EP0124, exit EP0126; second review: OK
- **Objects/placement (OBSERVED):** As S0093 plus orange percent badge at lower centre (x~0.4,y~0.82,d~0.3H); highlight now spans two lines.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Badge flat orange, black outline, white % sign.
- **Typography:** As S0093.
- **Readable text:** Supplemental data for figures; These findings underscore how mortgage rate lock-in restricts mobility
- **Unreadable/uncertain text:** Body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.842 #c2c2c0:0.059 #7b7d7f:0.055 #daa93c:0.037 #170f09:0.007
- **Hierarchy:** Badge first by saturation.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0124 (ADDITIVE_ENTRY); ends via EP0126 (ADDITIVE_ENTRY); children: EP0125
- **Narration (ASR, unverified):** the rate lock effect did
- **Story function (INFERRED):** INFERRED: introduces rate effect ('the rate lock effect did').
- **Continuity:** Badge also at S0095-S0099; lock added S0095.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0032 (ADDITIVE_ENTRY, f3553) A black padlock appears at lower left of the percent badge; the yellow highlight in the text widens.

## S0095 — f3576-3627 (149.042-151.167 s, 52 frames, 2.17 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0126.jpg; entry EP0126, exit EP0127; second review: OK
- **Objects/placement (OBSERVED):** S0094 plus black padlock at lower left of badge (x~0.24-0.36,y~0.72-0.93) and a worried stick figure with a thin pointer at lower right (x~0.52-0.62,y~0.8-1.0) frowning.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Padlock black with grey shackle, tilted; figure: round beige head, messy black hair, frown, thin line limbs.
- **Typography:** Doc body as before.
- **Readable text:** Supplemental data for figures; These findings underscore how mortgage rate lock-in restricts mobility
- **Unreadable/uncertain text:** Body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.790 #d3cac0:0.080 #7e7e80:0.062 #dcb338:0.043 #0d0906:0.024
- **Hierarchy:** Badge+lock pair then the figure's frown.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0126 (ADDITIVE_ENTRY); ends via EP0127 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** did more than offset the rate increase.
- **Story function (INFERRED):** INFERRED: 'rate lock' literalised as a padlock beside the rate badge.
- **Continuity:** Figure also at S0126-style states elsewhere; lock continues to S0099.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0096 — f3628-3653 (151.208-152.250 s, 26 frames, 1.08 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0127.jpg; entry EP0127, exit EP0128; second review: OK
- **Objects/placement (OBSERVED):** S0095 with the figure replaced by an upright green outlined dollar sign at right (x~0.88,y~0.72,~0.2H); highlight extends to longer line.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Dollar: green fill with dark green outline hand-drawn.
- **Typography:** As above.
- **Readable text:** Supplemental data for figures; ... restricts mobility, results in people not living in homes they would prefer, inflates prices, and worsens affordability
- **Unreadable/uncertain text:** Rest.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.799 #c4c3bc:0.061 #757e72:0.061 #dfbf35:0.056 #0a0c05:0.023
- **Hierarchy:** Badge+lock left, green $ right balance.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0127 (ELEMENT_SWAP); ends via EP0128 (OBJECT_MOTION); children: none
- **Narration (ASR, unverified):** The tool built to cool prices
- **Story function (INFERRED):** INFERRED: prices rising ('did more than offset the rate increase').
- **Continuity:** Ice-encased dollar slides out in EP0128 after this state; later red arrow at S0099.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: dollar at right; the last ~1 frame shows it in an ice block (EP0128 pre-1) per boundary sheet; INFERRED: ice block as 'frozen prices' pun

## S0097 — f3660-3671 (152.542-153.000 s, 12 frames, 0.50 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0128.jpg; entry EP0128, exit EP0129; second review: OK
- **Objects/placement (OBSERVED):** Document; badge (x~0.4,y~0.75) and padlock (x~0.3,y~0.82); right half empty; highlight spans full second sentence.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same doodles; no dollar.
- **Typography:** As above.
- **Readable text:** Supplemental data for figures; These findings underscore how mortgage rate lock-in restricts mobility, results in people not living in homes they would prefer, inflates prices, and worsens affordability
- **Unreadable/uncertain text:** none
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.812 #927c67:0.075 #c0c0c0:0.056 #ebe435:0.040 #090504:0.017
- **Hierarchy:** Badge+lock only.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0128 (OBJECT_MOTION); ends via EP0129 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** prices took
- **Story function (INFERRED):** INFERRED: 0.5 s beat after the dollar leaves, ASR 'prices took'.
- **Continuity:** Same as S0096 minus the dollar.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0098 — f3672-3720 (153.042-155.042 s, 49 frames, 2.04 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0129.jpg; entry EP0129, exit EP0131; second review: OK
- **Objects/placement (OBSERVED):** S0097 plus grey-haired stick figure holding head at far right (x~0.82-0.92,y~0.55-0.95), small blue house with trees at x~0.55-0.68 y~0.62-0.78.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Figure: grey curly hair, brownish-beige face, puzzled expression, thin black line body; house cartoon blue with chimney and green trees.
- **Typography:** As above.
- **Readable text:** Supplemental data for figures
- **Unreadable/uncertain text:** Body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.784 #bbbbba:0.063 #72746f:0.061 #e2c33a:0.060 #090909:0.032
- **Hierarchy:** Grey figure and blue house create secondary cluster right; badge left.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0129 (ADDITIVE_ENTRY); ends via EP0131 (ELEMENT_SWAP); children: EP0130
- **Narration (ASR, unverified):** took the sellers out of the market instead and
- **Story function (INFERRED):** INFERRED: seller who stays put ('took the sellers out of the market').
- **Continuity:** Grey-haired figure reused S0143 and EP0189.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0033 (ADDITIVE_ENTRY, f3690) A small handwritten speech bubble appears left of the grey-haired figure's head.

## S0099 — f3752-3761 (156.375-156.750 s, 10 frames, 0.42 s) — shot SH026 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0131.jpg; entry EP0131, exit EP0132; second review: MINOR
- **Objects/placement (OBSERVED):** Scrolled paper text with yellow highlight; orange percent badge (x~0.40,y~0.74) with black padlock at its left (x~0.24-0.34,y~0.6-0.9); green dollar sign at right (x~0.80-0.88,y~0.60-0.90); bold red jagged rising arrow from lower centre-right (x~0.53,y~0.91) to upper right (x~0.90,y~0.43).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Red marker arrow with black-less strokes; dollar green.
- **Typography:** As above.
- **Readable text:** Supplemental data for figures
- **Unreadable/uncertain text:** Body.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.815 #8a918d:0.086 #ede638:0.039 #c3602f:0.036 #0a0d06:0.023
- **Hierarchy:** Red arrow reads strongest (hue contrast) then $.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0131 (ELEMENT_SWAP); ends via EP0132 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** rise.
- **Story function (INFERRED):** INFERRED: prices rise ('rise.').
- **Continuity:** Dollar echoes S0096.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0100 — f3762-3795 (156.792-158.167 s, 34 frames, 1.42 s) — shot SH027 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0132.jpg; entry EP0132, exit EP0133; second review: MINOR
- **Objects/placement (OBSERVED):** Stick figure with round beige head, dot eyes, flat mouth and green tie (x~0.20-0.34,y~0.28-1.0) at left-centre; cream house with red roof, two blue windows and brown door (x~0.56-0.79,y~0.24-0.64) to its right.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Figure: thick black outlines, green tie, simple line limbs; house cream with red roof, two blue windows, brown door.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.882 #dcd0ba:0.056 #080605:0.046 #757e60:0.011 #a42723:0.006
- **Hierarchy:** Figure left, house right; both mid-weight.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0132 (FULL_REPLACE); ends via EP0133 (EXPRESSION_CHANGE); children: none
- **Narration (ASR, unverified):** And if a home won't sell,
- **Story function (INFERRED):** INFERRED: introduces the homeowner and the home ('if a home won't sell').
- **Continuity:** New asset pair; house also S0101, figure also S0101-S0103.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0101 — f3796-3824 (158.208-159.375 s, 29 frames, 1.21 s) — shot SH027 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0133.jpg; entry EP0133, exit EP0134; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling stick figure with round beige head and green tie (x~0.22-0.36,y~0.28-1.0) at left-centre; cream house with red roof, blue windows and brown door (x~0.56-0.79,y~0.24-0.64) at right.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0100; smile curve instead of flat mouth.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.883 #dcd0ba:0.053 #090605:0.046 #71835d:0.013 #a42723:0.006
- **Hierarchy:** Same.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0133 (EXPRESSION_CHANGE); ends via EP0134 (OBJECT_MOTION); children: none
- **Narration (ASR, unverified):** we're seeing homeowners just pull
- **Story function (INFERRED):** INFERRED: lead-in 'we're seeing homeowners just pull'; house then slides behind the figure (EP0134).
- **Continuity:** Expression change from S0100 (EP0133).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0102 — f3836-3845 (159.875-160.250 s, 10 frames, 0.42 s) — shot SH027 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0134.jpg; entry EP0134, exit EP0135; second review: MINOR
- **Objects/placement (OBSERVED):** Single smiling stick figure with round beige head and green tie (x~0.22-0.37,y~0.28-1.0), left of centre; rest of the canvas empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0101.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.946 #dec7b3:0.022 #040302:0.021 #648a59:0.008 #30302a:0.002
- **Hierarchy:** Figure only.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0134 (OBJECT_MOTION); ends via EP0135 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** listing and
- **Story function (INFERRED):** INFERRED: house 'pulled' off; 0.42 s.
- **Continuity:** Same figure as S0100.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0103 — f3846-3863 (160.292-161.000 s, 18 frames, 0.75 s) — shot SH027 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0135.jpg; entry EP0135, exit EP0136; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling green-tie stick figure (x~0.21-0.37,y~0.28-1.0) with a round speech bubble at upper right (x~0.41-0.66,y~0.10-0.46) containing two lines of handwritten text.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Bubble: black outline round-rect with tail pointing to figure's mouth; handwritten-style type.
- **Typography:** Handwritten marker, ~7% height, black.
- **Readable text:** Maybe later!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.930 #040303:0.032 #dac6b4:0.025 #67865e:0.010 #30312d:0.004
- **Hierarchy:** Bubble text first (largest dark type), then the figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0135 (ADDITIVE_ENTRY); ends via EP0136 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** and wait.
- **Story function (INFERRED):** INFERRED: homeowner delisting excuse ('and wait.').
- **Continuity:** Same figure as S0100-S0102.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0104 — f3864-3927 (161.042-163.667 s, 64 frames, 2.67 s) — shot SH028 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0136.jpg; entry EP0136, exit EP0137; second review: MINOR
- **Objects/placement (OBSERVED):** News-article screenshot cropped at top (x~0.08-0.51,y~0.0-0.92): share-icon row, three italic bullet lines, a short paragraph, bold chart title with two side-by-side crimson bar charts, footnote line and a last text line; right half of frame empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real article capture; crimson bar charts in two panels.
- **Typography:** Serif/sans mix: bullets italic ~1.5%; chart title bold ~1.7%.
- **Readable text:** Nearly 45,000 sellers who delisted their homes last year relisted them in January; Home Relistings Are on the Rise; Published on March 5th, 2026
- **Unreadable/uncertain text:** Chart axes and bullets small.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.939 #cac6c7:0.023 #c1254b:0.019 #9e9093:0.014 #665d61:0.005
- **Hierarchy:** Red bars draw the eye first, then bullets.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0136 (FULL_REPLACE); ends via EP0137 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** 45 ,000 homes that were pulled off the market last year
- **Story function (INFERRED):** INFERRED: source for '45,000 homes pulled off the market'.
- **Continuity:** Same screenshot continues in S0105.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0105 — f3943-4032 (164.333-168.042 s, 90 frames, 3.75 s) — shot SH028 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0137.jpg; entry EP0137, exit EP0138; second review: MINOR
- **Objects/placement (OBSERVED):** Article as S0104 (x~0.08-0.52) with cyan highlight on the first body line (x~0.08-0.19,y~0.47); at right three doodle buildings: pink house (x~0.58-0.70,y~0.27-0.50), grey tower with annex (x~0.75-0.90,y~0.16-0.49), small blue house (x~0.70-0.84,y~0.54-0.78).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn buildings with outlines, flat pastel/grey fills.
- **Typography:** Article text tiny.
- **Readable text:** Nearly 45,000 U.S. homes that were delisted; Home Relistings Are on the Rise
- **Unreadable/uncertain text:** Rest.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.861 #bbbebc:0.063 #0b0c0a:0.027 #606764:0.027 #bf2c4f:0.022
- **Hierarchy:** Buildings at right then red bars.
- **Camera/motion:** Static; buildings slide in via EP0137 before the state; **entry/exit:** Begins via EP0137 (ADDITIVE_ENTRY); ends via EP0138 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** back in January alone, the most for any January in Redfin's records.
- **Story function (INFERRED):** INFERRED: houses re-entering the market ('most for any January').
- **Continuity:** Same doodle set as S0121 cluster.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0106 — f4033-4083 (168.083-170.167 s, 51 frames, 2.12 s) — shot SH029 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0138.jpg; entry EP0138, exit EP0140; second review: MINOR
- **Objects/placement (OBSERVED):** Large dark-grey phone with black bezel (x~0.37-0.64,y~0.0-0.93) with a white rounded-square app icon showing a bold black H-like glyph at screen centre (x~0.50,y~0.5); thick black arm curving in from lower left (x~0.27-0.37,y~0.5-1.0).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Black outline, mid-grey screen, white icon with black glyph.
- **Typography:** Icon glyph bold sans black on white.
- **Readable text:** a single H-like glyph on the white icon
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.762 #666666:0.165 #020202:0.048 #252525:0.024 #979797:0.001
- **Hierarchy:** Icon centre of dark screen.
- **Camera/motion:** Icon scales down inside the state (EP0139); **entry/exit:** Begins via EP0138 (FULL_REPLACE); ends via EP0140 (FULL_REPLACE); children: none EP0139
- **Narration (ASR, unverified):** It's the real estate version of deleting hinge,
- **Story function (INFERRED):** INFERRED: dating-app metaphor ('deleting hinge').
- **Continuity:** Same phone as S0109.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state motion intervals:** EP0139

## S0107 — f4084-4110 (170.208-171.292 s, 27 frames, 1.12 s) — shot SH030 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0140.jpg; entry EP0140, exit EP0141; second review: MINOR
- **Objects/placement (OBSERVED):** Stick presenter with round peach head, messy black hair, dot eyes and flat mouth (x~0.20-0.41,y~0.16-0.57), body and hips below; small dark phone in his right hand (x~0.38-0.45,y~0.61-0.80); handwritten 'wait...' at right of head (x~0.43-0.53,y~0.31).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn thick outline; peach fill; thin black body; phone dark grey with camera dot.
- **Typography:** Handwritten marker ~8% height black.
- **Readable text:** wait...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.912 #f4d3b6:0.056 #070504:0.022 #4c4a48:0.008 #9e9894:0.003
- **Hierarchy:** Face first, then text.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0140 (FULL_REPLACE); ends via EP0141 (EXPRESSION_CHANGE); children: none
- **Narration (ASR, unverified):** then re -downloading it a
- **Story function (INFERRED):** INFERRED: self-doubt beat ('then re-downloading it a').
- **Continuity:** Same character as S0108 enlarged.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0108 — f4111-4132 (171.333-172.208 s, 22 frames, 0.92 s) — shot SH030 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0141.jpg; entry EP0141, exit EP0142; second review: MINOR
- **Objects/placement (OBSERVED):** Close-up of presenter: huge round head with spiky black hair, dot eyes and wide open grin with pink tongue (x~0.14-0.46,y~0.09-0.70); small dark phone at lower centre (x~0.31-0.39,y~0.79-1.0); two-line handwritten caption right of head (x~0.48-0.70,y~0.19-0.33).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same drawn style, enlarged ~1.8x vs S0107.
- **Typography:** Handwritten marker ~7% height black.
- **Readable text:** what if the loml is there?!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.823 #f4d2b6:0.107 #060403:0.044 #4e4b4a:0.016 #a98787:0.010
- **Hierarchy:** Face dominates; text second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0141 (EXPRESSION_CHANGE); ends via EP0142 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** it a few months later because
- **Story function (INFERRED):** INFERRED: comic hope ('re-downloading it...').
- **Continuity:** Enlarged version of S0107 (EP0141).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0109 — f4133-4175 (172.250-174.000 s, 43 frames, 1.79 s) — shot SH030 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0142.jpg; entry EP0142, exit EP0144; second review: MINOR
- **Objects/placement (OBSERVED):** Large dark-grey phone with black bezel (x~0.37-0.64,y~0.0-0.93) with a tiny white speck of an icon at screen centre (x~0.50,y~0.5); thick black arm curving in from lower left.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0106 but icon at near-zero size.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.747 #676767:0.182 #020202:0.046 #232323:0.022 #414141:0.002
- **Hierarchy:** Blank dark screen.
- **Camera/motion:** Icon scales up (EP0143) in-state; **entry/exit:** Begins via EP0142 (FULL_REPLACE); ends via EP0144 (FULL_REPLACE); children: none EP0143
- **Narration (ASR, unverified):** because you convinced yourself that,
- **Story function (INFERRED):** INFERRED: re-download animation start (EP0143 icon grows).
- **Continuity:** Same phone as S0106.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state motion intervals:** EP0143

## S0110 — f4176-4191 (174.042-174.667 s, 16 frames, 0.67 s) — shot SH031 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0144.jpg; entry EP0144, exit EP0145; second review: OK
- **Objects/placement (OBSERVED):** Worried figure centred (x~0.46-0.54,y~0.28-1.0 head x~0.46-0.54) small: peach head, black hair, teal tear dots at eyes, wavy frown, hands on hips.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn, small scale (~0.3H head).
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.933 #f4d3b6:0.046 #070404:0.016 #969a92:0.003 #55504c:0.002
- **Hierarchy:** Face centre.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0144 (FULL_REPLACE); ends via EP0145 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** this time,
- **Story function (INFERRED):** INFERRED: regret beat ('this time,').
- **Continuity:** Zoom close-up in S0111.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0111 — f4192-4217 (174.708-175.750 s, 26 frames, 1.08 s) — shot SH031 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0145.jpg; entry EP0145, exit EP0146; second review: MINOR
- **Objects/placement (OBSERVED):** Close-up worried face: very large round peach head with spiky black hair, teal tear dots at the eyes and wavy frown (x~0.34-0.67,y~0.09-0.75); short neck and shoulder lines at the bottom.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0110, larger.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.831 #f4d3b6:0.122 #040302:0.040 #8d9f96:0.004 #4f463f:0.003
- **Hierarchy:** Face fills centre.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0145 (ZOOM_OR_SCALE); ends via EP0146 (EXPRESSION_CHANGE); children: none
- **Narration (ASR, unverified):** it'll be different.
- **Story function (INFERRED):** INFERRED: comic climax ('it'll be different.').
- **Continuity:** Enlargement of S0110 (EP0145).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0112 — f4218-4269 (175.792-177.917 s, 52 frames, 2.17 s) — shot SH031 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0146.jpg; entry EP0146, exit EP0147; second review: MINOR
- **Objects/placement (OBSERVED):** Full-body stick presenter with round peach head, spiky black hair and gentle smile (head x~0.41-0.59,y~0.12-0.40), arms open at sides, legs apart, body centred (x~0.42-0.57,y~0.12-0.85).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same character, relaxed pose.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f3d2b7:0.032 #070404:0.011 #908a86:0.002 #46413d:0.002
- **Hierarchy:** Face and open arms.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0146 (EXPRESSION_CHANGE); ends via EP0147 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** But I know what some of you may be thinking right now,
- **Story function (INFERRED):** INFERRED: pivot to rebuttal ('But I know what some of you may be thinking').
- **Continuity:** Same figure reused S0114+.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0113 — f4301-4315 (179.250-179.833 s, 15 frames, 0.62 s) — shot SH031 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0147.jpg; entry EP0147, exit EP0148; second review: MINOR
- **Objects/placement (OBSERVED):** Green country-shaped cartoon character with two round upturned eyes and short legs at lower left (x~0.09-0.38,y~0.52-0.91); large red zig-zag arrow descending from top left-centre (x~0.21,y~0.0) to arrowhead at lower right (x~0.89,y~0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Map: green flat fill, thick black outline, two round eyes looking up, small legs; arrow: bold red marker zig-zag with arrowhead.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.897 #4a9f51:0.046 #d20c17:0.043 #102711:0.008 #de9a9c:0.006
- **Hierarchy:** Red arrow's diagonal dominates, map character anchors lower left.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0147 (ELEMENT_SWAP); ends via EP0148 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** places.
- **Story function (INFERRED):** INFERRED: 'places' where prices fall.
- **Continuity:** Same map character as S0076, S0124.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: mascot and arrow; arrow draws on in EP0147 before this state

## S0114 — f4316-4374 (179.875-182.292 s, 59 frames, 2.46 s) — shot SH032 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0148.jpg; entry EP0148, exit EP0150; second review: MINOR
- **Objects/placement (OBSERVED):** Line-chart screenshot (x~0.19-0.81,y~0.05-0.88): title top-left, y-axis labels $300K-$650K, x-axis labels 2019 Jan-2026 Jan, light gridlines, empty plot area at first, source and credit lines bottom-left.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real chart capture, thin grey gridlines.
- **Typography:** Sans, title ~2.5% height dark; axis labels ~1.5% grey.
- **Readable text:** Median asking price for the Austin metro area; $650K; $600K; $550K; $500K; $450K; $400K; $350K; $300K; 2019 Jan ... 2026 Jan; Source: Realtor.com
- **Unreadable/uncertain text:** Credit line under source is tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.983 #d1d1d1:0.006 #717171:0.005 #a3a3a3:0.004 #292929:0.002
- **Hierarchy:** Title top, then the drawing line.
- **Camera/motion:** Line draws in (EP0149); **entry/exit:** Begins via EP0148 (FULL_REPLACE); ends via EP0150 (ADDITIVE_ENTRY); children: none EP0149
- **Narration (ASR, unverified):** Just look at Austin. It's about 27 % below
- **Story function (INFERRED):** INFERRED: the city price chart for 'Just look at Austin'.
- **Continuity:** Same chart in S0115, S0140-S0142.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state motion intervals:** EP0149

## S0115 — f4375-4421 (182.333-184.250 s, 47 frames, 1.96 s) — shot SH032 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0150.jpg; entry EP0150, exit EP0151; second review: MINOR
- **Objects/placement (OBSERVED):** Chart as S0114 (x~0.19-0.81) with completed blue line peaking in early 2022 near $630K then declining to ~$460K; smiling spiky-haired presenter at lower centre (head x~0.46-0.61,y~0.45-0.76) with a thin brown pointer toward the right end.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Presenter hand-drawn, peach head, black spiky hair, thin pointer stick brown.
- **Typography:** Chart sans as S0114.
- **Readable text:** Median asking price for the Austin metro area; $650K ... $300K; Source: Realtor.com
- **Unreadable/uncertain text:** Credit line.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.939 #ecd1bc:0.033 #91909c:0.010 #0b0807:0.010 #49455d:0.009
- **Hierarchy:** Blue peak then presenter.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0150 (ADDITIVE_ENTRY); ends via EP0151 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** below its 2022 peak, but
- **Story function (INFERRED):** INFERRED: 'about 27% below its 2022 peak'.
- **Continuity:** Chart from S0114.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0116 — f4422-4446 (184.292-185.292 s, 25 frames, 1.04 s) — shot SH033 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0151.jpg; entry EP0151, exit EP0152; second review: MINOR
- **Objects/placement (OBSERVED):** One tilted yellow price tag with thick black outline, red $$$ marks and a curled black string at upper right (x~0.35-0.70,y~0.13-0.73).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn thick black outline, yellow fill, red marker $.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.943 #e3d933:0.035 #0a0805:0.012 #c32f11:0.008 #8a8964:0.002
- **Hierarchy:** Tag alone.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0151 (FULL_REPLACE); ends via EP0152 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** but it's not because of extreme
- **Story function (INFERRED):** INFERRED: price cuts ('extreme price cuts').
- **Continuity:** Same tag in S0117.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0117 — f4447-4488 (185.333-187.042 s, 42 frames, 1.75 s) — shot SH033 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0152.jpg; entry EP0152, exit EP0153; second review: MINOR
- **Objects/placement (OBSERVED):** Yellow price tag with red dollar marks and curled string, torn across the middle by a diagonal white gap (x~0.29-0.64,y~0.13-0.73).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0116 with ripped white band.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.943 #e3d936:0.035 #0a0906:0.011 #be3412:0.008 #a49d85:0.002
- **Hierarchy:** Tear gap draws eye.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0152 (ELEMENT_SWAP); ends via EP0153 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** extreme price cuts across the city.
- **Story function (INFERRED):** INFERRED: 'extreme price cuts across the city' - not extreme.
- **Continuity:** Variant of S0116 (EP0152).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0118 — f4489-4505 (187.083-187.750 s, 17 frames, 0.71 s) — shot SH034 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0153.jpg; entry EP0153, exit EP0154; second review: MINOR
- **Objects/placement (OBSERVED):** Article screenshot at left (x~0.06-0.49,y~0.0-0.93): serif masthead logo, small topic tags, large serif headline in three lines, short subtitle, author line, share icons and a street-scene photo at the bottom; right half empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real capture; photo.
- **Typography:** Serif title ~3% height.
- **Readable text:** Austin's Surge of New Housing Construction Drove Down Rents; Pew (masthead)
- **Unreadable/uncertain text:** Subtitle, author line and tags are tiny; subtitle seems to mention 120,000 new homes from 2015 to 2024.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfa:0.882 #9ebde3:0.033 #24251c:0.032 #606254:0.027 #9f9d93:0.026
- **Hierarchy:** Title and photo.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0153 (FULL_REPLACE); ends via EP0154 (PAN_OR_SCROLL); children: none
- **Narration (ASR, unverified):** Austin added 30
- **Story function (INFERRED):** INFERRED: source for 'Austin added 30%'.
- **Continuity:** Zooms in EP0154.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0119 — f4536-4611 (189.042-192.167 s, 76 frames, 3.17 s) — shot SH034 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0154.jpg; entry EP0154, exit EP0158; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed article body on a cream page (x~0.09-0.81,y~0.0-0.85), three paragraphs; astonished presenter at right (head x~0.71-0.91,y~0.27-0.64) with open oval mouth, hand under chin, body line down; no highlight visible in this tile.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Presenter: peach head, spiky hair, open oval mouth, hand on chin.
- **Typography:** Body sans ~2% dark; highlight orange appears on one sentence.
- **Readable text:** But starting in 2015, Austin instituted an array of policy reforms; The efforts worked. From 2015 to 2024, Austin added 120,000 units; Rents fell.
- **Unreadable/uncertain text:** Remaining text partly small.
- **Palette (MEASURED, top-5 k-means of representative frame):** #faf9f7:0.819 #e4d2c2:0.084 #9c9794:0.040 #5f5c59:0.040 #0c0807:0.017
- **Hierarchy:** Text block left, face right.
- **Camera/motion:** Scroll/zoom into body (EP0154), static after; **entry/exit:** Begins via EP0154 (PAN_OR_SCROLL); ends via EP0158 (FULL_REPLACE); children: EP0155;EP0156 EP0157
- **Narration (ASR, unverified):** housing supply in about a decade. The rest of the country added about 9%,
- **Story function (INFERRED):** INFERRED: supply growth '30%' vs '9%'.
- **Continuity:** Same document as S0118; highlight grows EP0155-157.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0034 (DRAW_ON_OR_REVEAL, f4549) Red underline stroke is drawn under a line of article text at upper-left (x~0.17-0.5,y~0.09) beside a yellow highlight; EVI0035 (HIGHLIGHT_ADD, f4558) An orange-yellow highlight appears on the first line of a sentence in the article body.; EVI0036 (HIGHLIGHT_ADD, f4563) The highlight extends to the second line of the same sentence.
- **Intra-state motion intervals:** EP0157

## S0120 — f4612-4636 (192.208-193.208 s, 25 frames, 1.04 s) — shot SH034 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0158.jpg; entry EP0158, exit EP0159; second review: MINOR
- **Objects/placement (OBSERVED):** Small smiling stick presenter with round peach head, spiky hair and dot eyes (head x~0.37-0.54,y~0.40-0.76), arms out, body to bottom edge; canvas otherwise empty.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0112.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.951 #f3d2b7:0.035 #080504:0.011 #554d47:0.002 #9b928b:0.002
- **Hierarchy:** Figure only.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0158 (FULL_REPLACE); ends via EP0159 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** 9%, so what happened is a flood
- **Story function (INFERRED):** INFERRED: transition ('what happened is a flood').
- **Continuity:** Same figure.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0121 — f4637-4685 (193.250-195.250 s, 49 frames, 2.04 s) — shot SH034 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0159.jpg; entry EP0159, exit EP0160; second review: MINOR
- **Objects/placement (OBSERVED):** Six building doodles across the upper half: pink house (x~0.12-0.20), grey tower (x~0.22-0.34), blue house (x~0.20-0.31,y~0.4-0.55), large brick mansion with red roof (x~0.45-0.77,y~0.07-0.52), small cream house and dark tower (x~0.69-0.92,y~0.5-0.78); smiling walking presenter (head x~0.37-0.54,y~0.40-0.78).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Hand-drawn buildings, varied pastel fills with black outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.805 #e3d2be:0.060 #0f0a08:0.055 #695049:0.042 #a09986:0.038
- **Hierarchy:** Mansion largest, then presenter.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0159 (ADDITIVE_ENTRY); ends via EP0160 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** a flood of brand new homes hit the market,
- **Story function (INFERRED):** INFERRED: 'a flood of brand new homes'.
- **Continuity:** Cluster again in S0122.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0122 — f4686-4720 (195.292-196.708 s, 35 frames, 1.46 s) — shot SH034 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0160.jpg; entry EP0160, exit EP0162; second review: MINOR
- **Objects/placement (OBSERVED):** Same six building doodles in upper half; small grey hooded stick figure with black sunglasses holding green banknotes (x~0.30-0.42,y~0.54-0.88) below the mansion.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Figure: grey hood, black shades, green bills.
- **Typography:** Bubble handwritten.
- **Readable text:** So many options!
- **Unreadable/uncertain text:** A speech bubble may appear in later frames; no text visible in this tile.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.838 #100b09:0.048 #675149:0.043 #949282:0.036 #cbc6ba:0.035
- **Hierarchy:** Cluster then small figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0160 (ELEMENT_SWAP); ends via EP0162 (ELEMENT_SWAP); children: EP0161
- **Narration (ASR, unverified):** supply demand shifted,
- **Story function (INFERRED):** INFERRED: buyer's view ('supply demand shifted').
- **Continuity:** Cluster from S0121.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0037 (ADDITIVE_ENTRY, f4702) A speech bubble with a short handwritten phrase appears right of the hooded figure.

## S0123 — f4738-4749 (197.458-197.917 s, 12 frames, 0.50 s) — shot SH034 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0162.jpg; entry EP0162, exit EP0163; second review: OK
- **Objects/placement (OBSERVED):** Green dollar sign (x~0.12,y~0.28-0.9) and cream house (x~0.3,y~0.3-0.7) in left half; red zig-zag arrow descending upper right.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Dollar green outline; house cream.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.907 #d10d17:0.046 #ddc4b7:0.018 #0b0f06:0.017 #4c9444:0.012
- **Hierarchy:** Arrow pulls diagonal; dollar/house cluster.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0162 (ELEMENT_SWAP); ends via EP0163 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** fell.
- **Story function (INFERRED):** INFERRED: prices fell.
- **Continuity:** Same arrow as S0113.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0124 — f4750-4788 (197.958-199.542 s, 39 frames, 1.62 s) — shot SH035 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0163.jpg; entry EP0163, exit EP0165; second review: MINOR
- **Objects/placement (OBSERVED):** Wide skyline photo (x~0.21-0.79,y~0.22-0.78) of a small downtown with trees in autumn colour under a cloudy sky; small handwritten photo-credit caption below its lower-left corner (x~0.21-0.33,y~0.80).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** City photograph, cloudy sky, autumn trees.
- **Typography:** Caption handwritten tiny.
- **Readable text:** Image: Wikipedia
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.711 #7798ba:0.122 #a38d73:0.065 #66573e:0.056 #c9c6be:0.047
- **Hierarchy:** Photo.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0163 (FULL_REPLACE); ends via EP0165 (OBJECT_MOTION); children: EP0164
- **Narration (ASR, unverified):** Now look at Hartford, Connecticut,
- **Story function (INFERRED):** INFERRED: place establishing shot ('Now look at Hartford').
- **Continuity:** Same photo S0125.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0038 (ADDITIVE_ENTRY, f4757) A handwritten place-name title appears above the photo.

## S0125 — f4806-4840 (200.292-201.708 s, 35 frames, 1.46 s) — shot SH035 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0165.jpg; entry EP0165, exit EP0168; second review: MINOR
- **Objects/placement (OBSERVED):** Skyline photo at right (x~0.46-1.0,y~0.22-0.78) with credit caption below and handwritten place-name title above (x~0.55-0.95,y~0.10-0.18); green country mascot with round eyes at left (x~0.10-0.40,y~0.37-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Photo; title handwritten ~5%.
- **Typography:** Handwritten black.
- **Readable text:** Hartford, Connecticut; Image: Wikipedia; (small remark above map)
- **Unreadable/uncertain text:** remark small
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.674 #8aa1b8:0.155 #937c61:0.078 #49a052:0.052 #3c3926:0.040
- **Hierarchy:** Title then photo.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0165 (OBJECT_MOTION); ends via EP0168 (FULL_REPLACE); children: EP0166;EP0167
- **Narration (ASR, unverified):** idea of a boom town.
- **Story function (INFERRED):** INFERRED: 'idea of a boom town'.
- **Continuity:** Mascot S0076.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0039 (EXPRESSION_CHANGE, f4820) The map character's pupils change position (look sideways) at lower left.; EVI0040 (ADDITIVE_ENTRY, f4829) A tiny handwritten remark appears above the map character's head.

## S0126 — f4841-4849 (201.750-202.083 s, 9 frames, 0.38 s) — shot SH036 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0168.jpg; entry EP0168, exit EP0169; second review: MINOR
- **Objects/placement (OBSERVED):** One grey tower doodle with window grid and annex (x~0.13-0.27,y~0.10-0.40); rest of canvas blank.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Grey/black building, window grid.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.967 #808d8f:0.013 #4c5556:0.010 #020506:0.008 #282e2f:0.003
- **Hierarchy:** Lone tower at upper left is the only object; large empty canvas around it sets up the scatter that follows.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0168 (FULL_REPLACE); ends via EP0169 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** There's no massive
- **Story function (INFERRED):** INFERRED: 'There's no massive'.
- **Continuity:** S0127-S0130 add towers.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0127 — f4850-4857 (202.125-202.417 s, 8 frames, 0.33 s) — shot SH036 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0169.jpg; entry EP0169, exit EP0170; second review: MINOR
- **Objects/placement (OBSERVED):** Two grey tower doodles: upper left (x~0.13-0.27,y~0.09-0.40) and right (x~0.79-0.93,y~0.21-0.52).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.932 #7e8c8e:0.024 #485151:0.022 #06090a:0.019 #d0d0ca:0.003
- **Hierarchy:** Two similar towers at opposite sides balance each other; eye jumps left to right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0169 (ADDITIVE_ENTRY); ends via EP0170 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** no massive
- **Story function (INFERRED):** INFERRED: count-up beat 'no massive'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0128 — f4858-4863 (202.458-202.667 s, 6 frames, 0.25 s) — shot SH036 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0170.jpg; entry EP0170, exit EP0171; second review: MINOR
- **Objects/placement (OBSERVED):** Three grey towers: upper left (x~0.13-0.27,y~0.09-0.40), lower centre-left (x~0.26-0.39,y~0.50-0.80), right (x~0.79-0.93,y~0.21-0.52).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.898 #7e8c8e:0.036 #495252:0.033 #060a0a:0.029 #cfd0c9:0.004
- **Hierarchy:** Third tower fills the gap in a loose triangle; no tower dominates.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0170 (ADDITIVE_ENTRY); ends via EP0171 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** massive building
- **Story function (INFERRED):** INFERRED: 'massive building'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0129 — f4864-4872 (202.708-203.042 s, 9 frames, 0.38 s) — shot SH036 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0171.jpg; entry EP0171, exit EP0172; second review: MINOR
- **Objects/placement (OBSERVED):** Four grey towers: upper left (x~0.13-0.27,y~0.09-0.40), upper centre-right (x~0.40-0.53,y~0.20-0.50), lower centre-left (x~0.26-0.39,y~0.50-0.80), right (x~0.79-0.93,y~0.21-0.52).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.865 #7d8c8d:0.048 #495252:0.044 #06090a:0.038 #cdcfc7:0.005
- **Hierarchy:** Evenly scattered identical towers read as a growing count; no focal point.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0171 (ADDITIVE_ENTRY); ends via EP0172 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** building wave
- **Story function (INFERRED):** INFERRED: 'building wave'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0130 — f4873-4908 (203.083-204.542 s, 36 frames, 1.50 s) — shot SH036 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0172.jpg; entry EP0172, exit EP0173; second review: MINOR
- **Objects/placement (OBSERVED):** Five grey towers: upper left (x~0.13-0.27,y~0.10-0.40), centre (x~0.40-0.53,y~0.21-0.51), lower left-centre (x~0.26-0.39,y~0.50-0.80), lower centre-right (x~0.61-0.74,y~0.55-0.85), right (x~0.79-0.93,y~0.21-0.52).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.831 #7d8b8d:0.060 #495252:0.054 #06090a:0.048 #cdcfc7:0.007
- **Hierarchy:** Five equal towers form an even scatter; the count, not any one tower, is the point.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0172 (ADDITIVE_ENTRY); ends via EP0173 (ZOOM_OR_SCALE); children: none
- **Narration (ASR, unverified):** wave happening in Connecticut,
- **Story function (INFERRED):** INFERRED: 'wave happening in Connecticut'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0131 — f4964-4990 (206.875-207.958 s, 27 frames, 1.12 s) — shot SH037 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0173.jpg; entry EP0173, exit EP0174; second review: MINOR
- **Objects/placement (OBSERVED):** Table screenshot (x~0.16-0.73,y~0.0-1.0) with a short bullet line above, header row of long column titles, eight ranked rows, blue outline around the first row (x~0.16-0.23,y~0.4); shocked presenter at right (head x~0.70-0.91,y~0.43-0.84) with open mouth and raised brow, small mouse cursor above his head.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real table capture; hand-drawn presenter.
- **Typography:** Sans table text ~1.6%.
- **Readable text:** Shop smart; Hartford, CT; Buffalo, NY; New York, NY; Providence, RI; San Jose, CA; Philadelphia, PA; Boston, MA; Los Angeles, CA; header words Metropolitan Area, Zillow Home Value Index, Heat Index; first-row values $381,760, 4.3 %, 3.9 %, 89.6, -63.0 %
- **Unreadable/uncertain text:** Column values mostly small.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.814 #e2d1c4:0.078 #9f9d9f:0.047 #65686d:0.042 #120e0e:0.019
- **Hierarchy:** Blue-boxed row then face.
- **Camera/motion:** Zoom/scroll (EP0173) before state; **entry/exit:** Begins via EP0173 (ZOOM_OR_SCALE); ends via EP0174 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** the country this year,
- **Story function (INFERRED):** INFERRED: Hartford ranks high.
- **Continuity:** Table from EP0173 zoom.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0132 — f4991-5100 (208.000-212.542 s, 110 frames, 4.58 s) — shot SH038 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0174.jpg; entry EP0174, exit EP0176; second review: MINOR
- **Objects/placement (OBSERVED):** Line chart screenshot (x~0.21-0.79,y~0.10-0.87): bold two-line title, y-axis labels 200-420, x-axis labels 2016-2025, light gridlines, source credit below; only a short teal line segment around 2016-2018 drawn in this frame.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real chart capture.
- **Typography:** Sans title ~4% bold; red handwritten '20%'.
- **Readable text:** Median Sales Price of Existing Single Family Homes, Hartford, CT (Thousands $)
- **Unreadable/uncertain text:** Axis tick labels and source credit are tiny; any later red label or box overlay is not visible in this tile.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.978 #d3d4d4:0.009 #141414:0.005 #9b9f9f:0.005 #5e5f5f:0.003
- **Hierarchy:** Title, red label.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0174 (FULL_REPLACE); ends via EP0176 (FULL_REPLACE); children: EP0175
- **Narration (ASR, unverified):** and Hartford's prices are up more than 20 % above the 2022 peak.
- **Story function (INFERRED):** INFERRED: 'prices up more than 20%'.
- **Continuity:** Chart also S0140.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0041 (ADDITIVE_ENTRY, f5031) A red handwritten '20%' label appears above the right end of the rising line.

## S0133 — f5101-5132 (212.583-213.875 s, 32 frames, 1.33 s) — shot SH039 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0176.jpg; entry EP0176, exit EP0177; second review: MINOR
- **Objects/placement (OBSERVED):** Line chart (x~0.20-0.80,y~0.13-0.82) titled with city name, jagged teal line high in 2016 falling and flattening after 2021; presenter at lower left (head x~0.10-0.21,y~0.57-0.80) with thin pointer toward the x-axis.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Teal line, presenter hand-drawn.
- **Typography:** Sans bold title ~3.2%.
- **Readable text:** Months' Supply in Hartford, CT
- **Unreadable/uncertain text:** Axes.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.952 #efd5c0:0.018 #b0d1d4:0.011 #7c9799:0.010 #1a1716:0.009
- **Hierarchy:** Chart then presenter.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0176 (FULL_REPLACE); ends via EP0177 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** But that's because the supply of
- **Story function (INFERRED):** INFERRED: 'supply of'.
- **Continuity:** S0134.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0134 — f5133-5167 (213.917-215.333 s, 35 frames, 1.46 s) — shot SH039 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0177.jpg; entry EP0177, exit EP0179; second review: MINOR
- **Objects/placement (OBSERVED):** Chart as S0133 (x~0.20-0.80) and presenter at lower left (x~0.10-0.21); red-roofed mansion with bushes at upper right (x~0.61-0.87,y~0.19-0.46).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Mansion cartoon.
- **Typography:** As S0133.
- **Readable text:** Months' Supply in Hartford, CT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.914 #dcd7cc:0.030 #9aa298:0.022 #19100c:0.018 #755a4e:0.015
- **Hierarchy:** Chart then mansion.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0177 (ADDITIVE_ENTRY); ends via EP0179 (FULL_REPLACE); children: EP0178
- **Narration (ASR, unverified):** of homes is constrained.
- **Story function (INFERRED):** INFERRED: 'homes is constrained'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0042 (ELEMENT_SWAP, f5150) The house's lower facade changes tint/pattern slightly (small localised change at the house base).

## S0135 — f5168-5178 (215.375-215.792 s, 11 frames, 0.46 s) — shot SH040 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0179.jpg; entry EP0179, exit EP0180; second review: MINOR
- **Objects/placement (OBSERVED):** Dark rounded news-headline card at top (x~0.10-0.67,y~0.09-0.37) with tiny publisher tag, two-line blue headline, grey summary, timestamp and small house thumbnail at right; green country mascot with round eyes at lower right (x~0.55-0.94,y~0.42-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Dark UI card with blue headline; map mascot.
- **Typography:** Sans card ~1.7%.
- **Readable text:** US mortgage rates brush 7%, weighing on buyers, sellers and further straining a bleak housing market; 21 hours ago
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.752 #1e2225:0.140 #48a350:0.074 #616968:0.017 #a8acb3:0.017
- **Hierarchy:** Card, mascot.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0179 (FULL_REPLACE); ends via EP0180 (TEXT_CHANGE); children: none
- **Narration (ASR, unverified):** It's the same
- **Story function (INFERRED):** INFERRED: same rates.
- **Continuity:** S0136-S0139.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0136 — f5179-5190 (215.833-216.292 s, 12 frames, 0.50 s) — shot SH040 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0180.jpg; entry EP0180, exit EP0181; second review: MINOR
- **Objects/placement (OBSERVED):** Dark rounded headline card at upper left (x~0.10-0.67,y~0.09-0.37) with publisher tag, blue two-line headline, grey summary, timestamp and house thumbnail; green country mascot at lower right (x~0.55-0.93,y~0.42-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** Sans.
- **Readable text:** The New Rules for Selling Your Home With Mortgage Rates Near 7%
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.755 #1f2225:0.140 #48a350:0.074 #5f6464:0.019 #a8a9a8:0.012
- **Hierarchy:** Card headline is the first read; mascot is the large green counterweight lower right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0180 (TEXT_CHANGE); ends via EP0181 (TEXT_CHANGE); children: none
- **Narration (ASR, unverified):** same country with
- **Story function (INFERRED):** INFERRED: 'same country with'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0137 — f5191-5202 (216.333-216.792 s, 12 frames, 0.50 s) — shot SH040 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0181.jpg; entry EP0181, exit EP0182; second review: MINOR
- **Objects/placement (OBSERVED):** Dark rounded headline card at upper left (x~0.10-0.67,y~0.12-0.37) with publisher tag, one-line headline, two-line grey summary, timestamp and for-sale house thumbnail at right; green country mascot lower right (x~0.55-0.93,y~0.42-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** Sans.
- **Readable text:** Selling a home just got harder as mortgage rates hit 7%
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.775 #1e2224:0.119 #49a350:0.074 #5b635d:0.018 #9ea29d:0.014
- **Hierarchy:** Card headline reads first; the green mascot anchors the lower right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0181 (TEXT_CHANGE); ends via EP0182 (TEXT_CHANGE); children: none
- **Narration (ASR, unverified):** country with the same
- **Story function (INFERRED):** INFERRED: 'the same'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0138 — f5203-5215 (216.833-217.333 s, 13 frames, 0.54 s) — shot SH040 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0182.jpg; entry EP0182, exit EP0183; second review: MINOR
- **Objects/placement (OBSERVED):** Dark rounded headline card at upper left (x~0.10-0.67,y~0.09-0.37) with publisher tag, two-line blue headline, grey summary, timestamp and house thumbnail; green country mascot lower right (x~0.55-0.94,y~0.42-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** Sans.
- **Readable text:** Struggling U.S. homebuyers, and market, face new hurdles as mortgage rates brush 7%
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.746 #1f2225:0.147 #48a350:0.074 #5a6361:0.017 #a5a9af:0.017
- **Hierarchy:** Card headline reads first; mascot balances it at lower right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0182 (TEXT_CHANGE); ends via EP0183 (TEXT_CHANGE); children: none
- **Narration (ASR, unverified):** same interest rates,
- **Story function (INFERRED):** INFERRED: 'same interest rates'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0139 — f5216-5229 (217.375-217.917 s, 14 frames, 0.58 s) — shot SH040 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0183.jpg; entry EP0183, exit EP0184; second review: MINOR
- **Objects/placement (OBSERVED):** Dark rounded headline card at upper left (x~0.10-0.67,y~0.09-0.31) with publisher tag, two-line blue headline, two-line grey summary, timestamp and dark house thumbnail; green country mascot lower right (x~0.55-0.93,y~0.42-0.90).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Same.
- **Typography:** Sans.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.757 #1f2225:0.138 #48a350:0.074 #56605b:0.019 #9ba0a6:0.012
- **Hierarchy:** Card headline reads first; mascot anchors the lower right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0183 (TEXT_CHANGE); ends via EP0184 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** rates, but
- **Story function (INFERRED):** INFERRED: 'rates, but'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0140 — f5230-5264 (217.958-219.375 s, 35 frames, 1.46 s) — shot SH041 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0184.jpg; entry EP0184, exit EP0185; second review: OK
- **Objects/placement (OBSERVED):** Two charts: left Hartford chart (x~0.0-0.5) rising; right Austin chart (x~0.52-0.97) peak and fall; smiling presenter centre (x~0.45-0.55,y~0.45-1.0).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Real charts + presenter.
- **Typography:** Sans.
- **Readable text:** Median Sales Price of Existing Single Family Homes, Hartford, CT (Thousands $); Median asking price for the Austin metro area
- **Unreadable/uncertain text:** Axes.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.927 #efd3bd:0.040 #0b0807:0.013 #a8abac:0.012 #605f65:0.008
- **Hierarchy:** Charts then presenter.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0184 (FULL_REPLACE); ends via EP0185 (ELEMENT_SWAP); children: none
- **Narration (ASR, unverified):** but opposite results. Where
- **Story function (INFERRED):** INFERRED: opposite results.
- **Continuity:** S0132, S0114.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0141 — f5265-5323 (219.417-221.833 s, 59 frames, 2.46 s) — shot SH041 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0185.jpg; entry EP0185, exit EP0187; second review: MINOR
- **Objects/placement (OBSERVED):** Same charts; presenter replaced by small cluster of three building doodles lower left (x~0.05-0.2,y~0.65-0.9) and later at S0142 second cluster.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As before.
- **Typography:** Sans.
- **Readable text:** Median Sales Price of Existing Single Family Homes, Hartford, CT (Thousands $); Median asking price for the Austin metro area
- **Unreadable/uncertain text:** Axes.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.959 #cdd0d0:0.016 #9a9d9e:0.011 #565559:0.009 #171815:0.006
- **Hierarchy:** Charts dominate; the small pastel building cluster at lower left is the new element that draws the eye second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0185 (ELEMENT_SWAP); ends via EP0187 (ADDITIVE_ENTRY); children: EP0186
- **Narration (ASR, unverified):** Where supply exploded, prices fell.
- **Story function (INFERRED):** INFERRED: 'where supply exploded, prices fell'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state events:** EVI0043 (ADDITIVE_ENTRY, f5270) A second cluster of three small building doodles appears to the right of the first.

## S0142 — f5324-5380 (221.875-224.208 s, 57 frames, 2.38 s) — shot SH041 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0187.jpg; entry EP0187, exit EP0189; second review: MINOR
- **Objects/placement (OBSERVED):** Hartford chart at left (x~0.09-0.52,y~0.07-0.62) and Austin chart at right (x~0.55-0.95,y~0.45-0.85) with a thick cyan line; two clusters of three building doodles (pink house, tower, blue house) at lower left (x~0.15-0.28 and x~0.33-0.45,y~0.62-0.90); upside-down presenter head at top (x~0.66-0.83,y~0.0-0.28).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As above.
- **Typography:** Sans.
- **Readable text:** Median Sales Price...; Median asking price for the Austin metro area
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.915 #ded0c2:0.039 #7da8ac:0.019 #11100d:0.015 #565550:0.013
- **Hierarchy:** Thick cyan line and the upside-down head draw the eye first; the building clusters read second.
- **Camera/motion:** Static; red line draws via EP0188; **entry/exit:** Begins via EP0187 (ADDITIVE_ENTRY); ends via EP0189 (ELEMENT_SWAP); children: none EP0188
- **Narration (ASR, unverified):** Where it didn't, prices kept climbing.
- **Story function (INFERRED):** INFERRED: 'where it didn't, prices kept climbing'.
- **Continuity:** 
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions
- **Intra-state motion intervals:** EP0188

## S0143 — f5425-5490 (226.083-228.792 s, 66 frames, 2.75 s) — shot SH042 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0189.jpg; entry EP0189, exit EP0190; second review: MINOR
- **Objects/placement (OBSERVED):** Grey curly-haired stick figure, head resting on raised hand (head x~0.70-0.87,y~0.13-0.45), body and legs to the lower area; small blue house with cupola and green trees at left of it (x~0.48-0.70,y~0.33-0.52).
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** As S0098.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.934 #040506:0.028 #666a66:0.016 #bcbebd:0.014 #2a414a:0.008
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0189 (ELEMENT_SWAP); ends via EP0190 (FULL_REPLACE); children: none
- **Narration (ASR, unverified):** doesn't come from the people who already own homes.
- **Story function (INFERRED):** INFERRED: 'doesn't come from the people who already own homes'.
- **Continuity:** S0098.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0144 — f5491-5527 (228.833-230.333 s, 37 frames, 1.54 s) — shot SH043 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0190.jpg; entry EP0190, exit EP0191; second review: OK
- **Objects/placement (OBSERVED):** Tall ponytail-hair figure centre-left (x~0.2-0.27,y~0.1-1.0), worried, beige head.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Dark-brown ponytail swoosh, worried face.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #030202:0.038 #e1d5bc:0.033 #3e3430:0.006 #817e7a:0.003
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0190 (FULL_REPLACE); ends via EP0191 (ADDITIVE_ENTRY); children: none
- **Narration (ASR, unverified):** It comes from the one seller who
- **Story function (INFERRED):** INFERRED: 'one seller who'.
- **Continuity:** 
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0145 — f5528-5561 (230.375-231.750 s, 34 frames, 1.42 s) — shot SH043 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0191.jpg; entry EP0191, exit EP0192; second review: MINOR
- **Objects/placement (OBSERVED):** Ponytail stick figure at left (head x~0.18-0.37,y~0.12-0.50, swoosh hair above) with worried face; hand-drawn wall clock at right of it (x~0.54-0.82,y~0.19-0.72) with numerals 1-12, short hand up toward twelve and long hand toward three.
- **Background:** flat off-white canvas (~#FCFCFC), no texture
- **Illustration:** Clock black outline, numbers, hands pointing two-ish.
- **Typography:** Handwritten clock numerals.
- **Readable text:** 12 1 2 3 4 5 6 7 8 9 10 11 (clock numerals)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.896 #030303:0.053 #dfd4be:0.036 #3c3533:0.008 #83817f:0.006
- **Hierarchy:** Figure then clock.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Begins via EP0191 (ADDITIVE_ENTRY); ends via EP0192 (prior-shard event); children: none
- **Narration (ASR, unverified):** who can't afford to wait,
- **Story function (INFERRED):** INFERRED: 'who can't afford to wait'.
- **Continuity:** S0144.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, legible text from the state sheet; INFERRED: story role and approximate fractions

## S0146 — f5562-5583 (231.792-232.667 s, 22 frames, 0.92 s) — shot SH044 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0192.jpg; entry EP0192, exit EP0193; second review: OK
- **Objects/placement (OBSERVED):** Small topknot builder figure (dark curl of hair, beige head, open smile) centred at x~0.49, head y~0.22-0.46, feet y~0.78 (about 0.55 of frame height); right hand raised holding a small brown hammer at x~0.55,y~0.45. Rest of canvas empty.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** thick black marker outline, flat beige head, thin line body; happy open-mouth face; hammer drawn with grey head, wooden handle
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.978 #070504:0.010 #ded4c0:0.008 #453e3b:0.003 #8c8886:0.002
- **Hierarchy:** Single small figure is the only focal point; high contrast black on white.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0192 (large worried figure + wall clock replaced); hard replace out via EP0193.
- **Narration (ASR, unverified):** the builder.
- **Story function (INFERRED):** INFERRED: introduces the builder character as the subject of the next contrast ('the builder').
- **Continuity:** Same topknot builder as S0150/S0151/S0160 (sad, hammer lowered) and S0165; here smiling and hammer raised.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0147 — f5584-5611 (232.708-233.833 s, 28 frames, 1.17 s) — shot SH045 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0193.jpg; entry EP0193, exit EP0194; second review: OK
- **Objects/placement (OBSERVED):** Large headband character (messy brown hair, red headband, tan face, small smile) at left: head x~0.12-0.39,y~0.15-0.53, curved body cropped by bottom edge; small pink two-storey house with two teal windows and green bushes at right (x~0.67-0.86,y~0.36-0.68).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** thick black outlines, flat tan/brown fill, red band; house flat dusty pink with dark red roof, teal windows, green bush clumps
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.867 #080504:0.049 #d4b5a6:0.036 #9d8368:0.027 #724d43:0.021
- **Hierarchy:** Oversized head dominates; small house is the secondary target at right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0193 (full composition swap); mortgage document is added next via EP0194.
- **Narration (ASR, unverified):** A homeowner can sit on a cheap
- **Story function (INFERRED):** INFERRED: homeowner figure plus house introduces the cheap-mortgage side of the comparison.
- **Continuity:** Headband figure and pink house reused unchanged in S0148 with an added document.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0148 — f5612-5642 (233.875-235.125 s, 31 frames, 1.29 s) — shot SH045 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0194.jpg; entry EP0194, exit EP0195; second review: OK
- **Objects/placement (OBSERVED):** Same large headband character at left (head x~0.12-0.39); stack of cream document pages at upper centre-right (x~0.50-0.66,y~0.17-0.53) with red title and scribbles; pink house with bushes at right (x~0.67-0.86,y~0.36-0.68).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same marker outline style; document is cream paper with red title letters, wavy line text, tick-like signature
- **Typography:** handwritten/marker caps, red, ~7% frame height, bold, left-aligned on page
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** scribbled placeholder lines on the document
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.820 #dcc8b5:0.066 #080504:0.060 #9d846a:0.031 #724d43:0.024
- **Hierarchy:** Large head first, then the red title on the cream document, then house.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive entry via EP0194 (document pops in on one frame); hard replace out via EP0195.
- **Narration (ASR, unverified):** a cheap mortgage for years.
- **Story function (INFERRED):** INFERRED: documents the cheap fixed mortgage a homeowner holds.
- **Continuity:** Extends S0147 by one prop; same layout.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0149 — f5643-5668 (235.167-236.208 s, 26 frames, 1.08 s) — shot SH046 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0195.jpg; entry EP0195, exit EP0196; second review: OK
- **Objects/placement (OBSERVED):** Smiling spiky-black-hair presenter: round peach head x~0.42-0.58,y~0.19-0.49 (about 0.16 of frame width), thin line body with arms bent outwards and legs apart down to y~0.86. Nothing else.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** round peach head, black spiky hair scribble, simple dot eyes and curved smile; single-weight black line body
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f3d2b7:0.032 #060403:0.010 #8b8581:0.002 #403b38:0.002
- **Hierarchy:** Lone figure, centred; face is the focus.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0195; hard replace out via EP0196.
- **Narration (ASR, unverified):** A builder can't.
- **Story function (INFERRED):** INFERRED: neutral narrator beat between homeowner and builder.
- **Continuity:** Same presenter as S0176/S0177 and S0198 family (spiky hair, peach head).
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0150 — f5669-5688 (236.250-237.042 s, 20 frames, 0.83 s) — shot SH047 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0196.jpg; entry EP0196, exit EP0197; second review: OK
- **Objects/placement (OBSERVED):** Small worried topknot builder at x~0.23-0.32, y~0.28-0.80 (about 0.5 of frame height), hammer held low at hip; remaining canvas empty.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline, beige head, worried flat mouth, brown curl of hair; hammer with grey head
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.981 #070504:0.009 #e0d6c0:0.006 #494540:0.003 #9b9893:0.001
- **Hierarchy:** Single small figure, expression is the only cue.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0196; additive prop entry follows via EP0197.
- **Narration (ASR, unverified):** A builder has no 3
- **Story function (INFERRED):** INFERRED: builder presented as worried/constrained ('has no 3...').
- **Continuity:** Same sad builder as S0151, S0160, S0165, S0166, S0211.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0151 — f5689-5724 (237.083-238.542 s, 36 frames, 1.50 s) — shot SH047 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0197.jpg; entry EP0197, exit EP0198; second review: OK
- **Objects/placement (OBSERVED):** Same worried builder at left (x~0.23-0.32,y~0.28-0.80); tall pink document with thick black border and red title at right (x~0.61-0.78,y~0.21-0.64).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline; pink-fill page with dark border; red letters
- **Typography:** handwritten/marker caps, red, ~9% frame height, bold, centred on page
- **Readable text:** LOAN
- **Unreadable/uncertain text:** scribbled lines under the title
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.901 #e5ccc9:0.063 #0a0706:0.023 #6f6664:0.006 #c53030:0.006
- **Hierarchy:** Red LOAN title draws the eye, then the worried builder.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive entry via EP0197; hard replace out via EP0198.
- **Narration (ASR, unverified):** 3 % loan to protect.
- **Story function (INFERRED):** INFERRED: shows the builder's own loan (construction loan) as a burden.
- **Continuity:** S0150 plus a LOAN document; reused in S0212 and S0286.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0152 — f5725-5809 (238.583-242.083 s, 85 frames, 3.54 s) — shot SH048 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0198.jpg; entry EP0198, exit EP0201; second review: MINOR
- **Objects/placement (OBSERVED):** Chart screenshot centred (x~0.16-0.82,y~0.14-0.85): four coloured lines, title at top centre, y axis 0-16 at left, x axis 2018-2026 along bottom, legend lower left (x~0.22-0.40,y~0.60-0.78), logo lower right of plot (x~0.70-0.80,y~0.67-0.77). A magenta horizontal line is animated across it by EP0199-0200.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** white chart image on canvas, thin 1px lines, tiny labels; no hand-drawn element
- **Typography:** clean sans-serif chart text, black, title ~2% frame height bold caps centred over plot; axis/legend labels ~1.5%
- **Readable text:** AVERAGE EFFECTIVE INTEREST RATE; legend: Land Acquisition, Land Development, Single-family Construction: Speculative, Single-family Construction: Pre-sold; x axis 2018-2026; y axis ticks 0-16; NAHB
- **Unreadable/uncertain text:** exact line values; y axis tick labels 0-16 and x years 2018-2026 are legible but unneeded; legend line sample colours
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.937 #dbd9d9:0.030 #b1aba9:0.014 #7f7980:0.014 #393939:0.005
- **Hierarchy:** Chart title then the line cluster peaking ~2024; the magenta overlay line draws attention to the ~12% level.
- **Camera/motion:** STATIC 2D; only the magenta line animates across (EP0199 3f, EP0200 10f); **entry/exit:** Hard replace in via EP0198; two hand-drawn magenta level line animations (EP0199, EP0200) draw across from left to right; hard replace out via EP0201.
- **Narration (ASR, unverified):** Its construction loans run close to 12%, and the whole business depends
- **Story function (INFERRED):** INFERRED: source evidence for builder loan rates near 12% (ASR: construction loans run close to 12%).
- **Continuity:** Third-party chart cut-in like S0162 and S0200; the magenta line is a drawn annotation.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: chart contents, magenta line animating (EP0199-0200). INFERRED: its meaning as a 12% marker.
- **Intra-state events:** EVI0044 (DRAW_ON_OR_REVEAL, f5771) Magenta/red horizontal stroke segment is drawn across the left part of a line chart (x~0.33-0.45,y~0.38) over three frames
- **Intra-state motion intervals:** EP0199;EP0200

## S0153 — f5810-5839 (242.125-243.333 s, 30 frames, 1.25 s) — shot SH049 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0201.jpg; entry EP0201, exit EP0202; second review: OK
- **Objects/placement (OBSERVED):** Two joined teal cartoon houses with dark grey roofs (x~0.16-0.36,y~0.36-0.62) and a red For-Sale sign on a post just right (x~0.37-0.46,y~0.57-0.72); rest empty.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** thick black outline, pale teal fill, dark grey roof, red sign with wooden post
- **Typography:** handwritten/marker caps, white on red, ~3%
- **Readable text:** FOR SALE! (sign)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #b8d9d2:0.018 #0a0909:0.017 #585957:0.008 #b72e2f:0.004
- **Hierarchy:** Houses first, red sign second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0201 (chart gone); additive entry follows via EP0202.
- **Narration (ASR, unverified):** depends on selling this house to
- **Story function (INFERRED):** INFERRED: unsold new house inventory builders must sell to fund next project.
- **Continuity:** Houses + sign reused in S0154.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0154 — f5840-5866 (243.375-244.458 s, 27 frames, 1.12 s) — shot SH049 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0202.jpg; entry EP0202, exit EP0203; second review: OK
- **Objects/placement (OBSERVED):** Teal houses and red sign at left (x~0.16-0.46,y~0.36-0.72); at right (x~0.62-0.88,y~0.42-0.68) two tiny stick builders: dark-haired one holding a saw, blonde one with a hammer, with a terracotta brick pile between them.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same marker outline style; bricks flat terracotta
- **Typography:** handwritten/marker caps white on red
- **Readable text:** FOR SALE! (sign)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.934 #0d0909:0.023 #bad7d0:0.020 #c46f58:0.012 #5a524f:0.011
- **Hierarchy:** Houses with sign first, then the small construction vignette at right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive entry via EP0202 (builders+bricks pop in); hard replace out via EP0203.
- **Narration (ASR, unverified):** to fund the next one.
- **Story function (INFERRED):** INFERRED: next building project funded by selling this house.
- **Continuity:** S0153 plus builders vignette.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0155 — f5867-5898 (244.500-245.792 s, 32 frames, 1.33 s) — shot SH050 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0203.jpg; entry EP0203, exit EP0204; second review: OK
- **Objects/placement (OBSERVED):** Three oversized green banknotes with yellow dollar sign, each held by a thick black arm from a frame edge: tilted top-left bill (x~0.07-0.30,y~0.19-0.63), lower-centre bill (x~0.39-0.62,y~0.52-1.0) with arm from bottom, right bill (x~0.77-0.90,y~0.28-0.69) with arm from the right edge.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** bold black outline, flat mid-green notes, grey-green seal, yellow dollar mark
- **Typography:** none (dollar symbol in notes)
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.842 #7aae71:0.079 #040704:0.040 #6b8961:0.030 #cbd441:0.009
- **Hierarchy:** Bright green bills against white; the three arms form a triangle that leads the eye across.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0203; bills slide away (EP0204 motion) into blank frame.
- **Narration (ASR, unverified):** So when buyers in the market pull
- **Story function (INFERRED):** INFERRED: money / buyers pulling out of the market (ASR: 'when buyers pull back').
- **Continuity:** Money-bill style reused in S0285.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0156 — f5908-5916 (246.208-246.542 s, 9 frames, 0.38 s) — shot SH050 (inferred) — F12:blank canvas pause
- **Evidence:** frames/ep_stable/e0204.jpg; entry EP0204, exit EP0205; second review: MINOR
- **Objects/placement (OBSERVED):** No objects; blank canvas.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** blank
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fdfdfd:1.000 #fdfdfd:0.000 #fdfdfd:0.000 #fdfdfd:0.000 #fdfdfd:0.000
- **Hierarchy:** none; pause frame.
- **Camera/motion:** STATIC 2D (blank); **entry/exit:** Arrives via EP0204 (bills slide out); ended by EP0205 (figure and house appear).
- **Narration (ASR, unverified):** back, builders
- **Story function (INFERRED):** INFERRED: deliberate beat of empty space as buyers 'pull back' (ASR: 'back, builders').
- **Continuity:** Blank canvas matches the normal background of all neighbours.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: blank canvas, 0.38 s. INFERRED: purpose.

## S0157 — f5917-5921 (246.583-246.750 s, 5 frames, 0.21 s) — shot SH050 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0205.jpg; entry EP0205, exit EP0206; second review: OK
- **Objects/placement (OBSERVED):** Green-tie character at left (round beige head x~0.21-0.37,y~0.34-0.50, thick green tie, thin body cropped by bottom edge) and a cream house with red roof, two blue windows and orange door at right (x~0.56-0.79,y~0.28-0.67).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline; tan head; green tie with dark shading; house cream with red roof
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.882 #dcd0ba:0.056 #080605:0.045 #747e60:0.011 #a22722:0.006
- **Hierarchy:** Face then house.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive pop-in via EP0205 onto the empty canvas (S0156); house slides left behind/past the figure (EP0206 motion) and the face turns to a smile, ending the state.
- **Narration (ASR, unverified):** builders don't
- **Story function (INFERRED):** INFERRED: a buyer stand-in considering a house.
- **Continuity:** Green-tie buyer figure continues in S0158, S0159, S0202-S0204.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0158 — f5930-5938 (247.125-247.458 s, 9 frames, 0.38 s) — shot SH050 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0206.jpg; entry EP0206, exit EP0207; second review: MINOR
- **Objects/placement (OBSERVED):** Green-tie character alone: head x~0.22-0.37,y~0.33-0.57, smiling with dot eyes, green tie and body to bottom edge; empty right side.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same marker style; tan head; green tie
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.946 #ddc7b3:0.022 #040403:0.022 #638b58:0.008 #34372f:0.002
- **Hierarchy:** Face and green tie.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Arrives from the EP0206 house-slide-out; speech bubble added via EP0207.
- **Narration (ASR, unverified):** don't delist
- **Story function (INFERRED):** INFERRED: buyer smiling/declining before the speech bubble.
- **Continuity:** Same figure as S0157 and S0159.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0159 — f5939-5956 (247.500-248.208 s, 18 frames, 0.75 s) — shot SH050 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0207.jpg; entry EP0207, exit EP0208; second review: OK
- **Objects/placement (OBSERVED):** Green-tie character at left (head x~0.22-0.37,y~0.33-0.57); speech bubble upper right (x~0.41-0.67,y~0.17-0.50) with a tail pointing left to the head.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** bubble with thick black outline, white fill, tail pointing to the figure
- **Typography:** handwritten marker, black, ~7% of frame height, centred two lines
- **Readable text:** Maybe later!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.930 #040403:0.032 #dac6b4:0.025 #67875e:0.009 #343531:0.004
- **Hierarchy:** Bubble text then face.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive entry via EP0207 (bubble pops in); hard replace out via EP0208.
- **Narration (ASR, unverified):** delist and wait.
- **Story function (INFERRED):** INFERRED: buyers hesitating ('don't delist and wait').
- **Continuity:** S0158 plus bubble; bubble style reused in S0161.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0160 — f5957-5972 (248.250-248.875 s, 16 frames, 0.67 s) — shot SH051 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0208.jpg; entry EP0208, exit EP0209; second review: OK
- **Objects/placement (OBSERVED):** Small worried topknot builder at x~0.22-0.32,y~0.28-0.80; hammer at hip; empty elsewhere.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline, beige head, brown curl
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.981 #070505:0.009 #dfd4c0:0.006 #494440:0.002 #95938f:0.001
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0208; bubble added via EP0209.
- **Narration (ASR, unverified):** They're forced to cut prices.
- **Story function (INFERRED):** INFERRED: builder forced to cut prices (ASR: 'They're forced to cut prices').
- **Continuity:** Identical pose to S0150.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0161 — f5973-5989 (248.917-249.583 s, 17 frames, 0.71 s) — shot SH051 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0209.jpg; entry EP0209, exit EP0210; second review: OK
- **Objects/placement (OBSERVED):** Small worried builder at left (x~0.22-0.32,y~0.28-0.80 of frame) with a large speech bubble to his right (x~0.35-0.66,y~0.26-0.62) holding two lines of text.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same marker style
- **Typography:** handwritten marker, black, ~7%
- **Readable text:** Worse bricks it is...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.964 #060505:0.020 #dad2c3:0.008 #454341:0.005 #8f8f8d:0.003
- **Hierarchy:** Bubble text then figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive via EP0209; hard replace out via EP0210.
- **Narration (ASR, unverified):** cut prices.
- **Story function (INFERRED):** INFERRED: joke on lowered quality (cutting costs/bricks) while cutting prices.
- **Continuity:** S0160 plus bubble; echoes S0159.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0162 — f5990-6124 (249.625-255.208 s, 135 frames, 5.62 s) — shot SH052 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0210.jpg; entry EP0210, exit EP0214; second review: MINOR
- **Objects/placement (OBSERVED):** Chart screenshot centred (x~0.07-0.93,y~0.20-0.80): blue line with a hump, grey recession bands, title strip across top, source note beneath, 'Fullscreen' button lower right; a tiny tooltip box with vertical hairline appears near the right end.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** image of web chart; thin blue line, light grey recession bands
- **Typography:** clean sans-serif chart UI, tiny; logo heading ~2% blue bold
- **Readable text:** FRED; chart title 'New Houses for Sale by Stage of Construction, Completed'; 'Fullscreen'; source line 'Sources: U.S. Census Bureau, U.S. Department of Housing and Urban Development via FRED'; 'Shaded areas indicate U.S. recessions.'; fred.stlouisfed.org
- **Unreadable/uncertain text:** axis numbers, tooltip values
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.757 #e9f0f6:0.189 #ced4d8:0.037 #99a8b3:0.011 #5a7081:0.005
- **Hierarchy:** Blue line peak at 2008 then trough then rise; tooltip catches eye as it moves.
- **Camera/motion:** STATIC 2D; cursor/tooltip micro-motion (EP0211-EP0213); **entry/exit:** Hard replace in via EP0210; micro tooltip animation EP0211-0213 (3f, 7f, 49f); hard replace out via EP0214.
- **Narration (ASR, unverified):** And right now, they're sitting on the most finished, unsold new homes since 2009.
- **Story function (INFERRED):** INFERRED: evidence that new-home inventory is highest since 2009 (ASR).
- **Continuity:** Same screenshot-on-canvas treatment as S0152 and S0200.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: chart and tooltip motion. INFERRED: purpose.
- **Intra-state motion intervals:** EP0211;EP0212;EP0213

## S0163 — f6125-6132 (255.250-255.542 s, 8 frames, 0.33 s) — shot SH053 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0214.jpg; entry EP0214, exit EP0215; second review: OK
- **Objects/placement (OBSERVED):** Article screenshot spanning x~0.25-0.80,y~0.06-0.92 with small contact lines at upper left and small body text; at lower right a presenter with spiky hair and worried line mouth, head x~0.69-0.86,y~0.37-0.74, body cropped by bottom, thin brown pointer to x~0.92.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** article screenshot image; presenter in thick black marker outline
- **Typography:** small sans-serif article text ~1.2% height, black/dark grey; links blue
- **Readable text:** none
- **Unreadable/uncertain text:** dense article paragraphs; contact block upper left
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.867 #e7d4c4:0.060 #afb0b0:0.032 #868686:0.029 #14100f:0.013
- **Hierarchy:** Presenter's face over the dense text; text is background texture.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0214; zoom-in of the article (EP0215 16f) follows.
- **Narration (ASR, unverified):** This month,
- **Story function (INFERRED):** INFERRED: pivot to a source article quote about builders cutting prices.
- **Continuity:** Same screenshot continues in S0164 at larger scale.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0164 — f6149-6272 (256.250-261.375 s, 124 frames, 5.17 s) — shot SH053 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0215.jpg; entry EP0215, exit EP0217; second review: OK
- **Objects/placement (OBSERVED):** Magnified article text block at left and centre (x~0.13-0.77,y~0.06-0.98); presenter head at right (x~0.69-0.87,y~0.38-0.69) with body cropped at bottom and a thin brown pointer running from lower right toward the text at about x~0.72-0.92,y~0.75-0.83.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** magnified article; pointer line brown; yellow-orange marker highlight
- **Typography:** web serif/sans article text ~2% height
- **Readable text:** 'lending conditions and elevated land, labor and construction costs persist,' said NAHB ... 'Notably, 42% of builders rated current lot availability as poor and 38% as fair.' The latest HMI survey found that 38% of builders cut prices in September, up from 35% in August. The average price cut remained at 6% ... 66% of builders reported using sales incentives in September, up from 63%
- **Unreadable/uncertain text:** remaining lower paragraphs of the article
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.816 #e1d3c7:0.082 #737372:0.048 #a4a3a3:0.042 #100c0b:0.012
- **Hierarchy:** Highlighted sentence (38% price cuts) then presenter pointer.
- **Camera/motion:** ZOOM-in just before (EP0215); STATIC after; **entry/exit:** Arrives from zoom EP0215 (16f); inside the state a pointer pose swap (EP0216) and highlights appear; hard replace out via EP0217.
- **Narration (ASR, unverified):** 38 % of builders cut prices, and two -thirds offered incentives just to close deals.
- **Story function (INFERRED):** INFERRED: quoting the key stat (38% cut prices, two-thirds incentives) per ASR.
- **Continuity:** Same article as S0163 after zoom.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: text lines. INFERRED: use.
- **Intra-state events:** EVI0045 (POSE_SWAP, f6207) Presenter's pointer arm changes: the pointer rises from a low line to a diagonal reaching up-left over the article text (checked on native crops).

## S0165 — f6273-6313 (261.417-263.083 s, 41 frames, 1.71 s) — shot SH054 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0217.jpg; entry EP0217, exit EP0218; second review: MINOR
- **Objects/placement (OBSERVED):** Small worried topknot builder at x~0.23-0.32,y~0.28-0.80; empty elsewhere.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline, beige head, brown curl
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.981 #070504:0.009 #ddd4bf:0.006 #423e3a:0.002 #87857f:0.001
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0217; armchair added via EP0218.
- **Narration (ASR, unverified):** So builders have to do something that
- **Story function (INFERRED):** INFERRED: contrast: builder vs relaxed homeowner (ASR: 'something that regular homeowners aren't').
- **Continuity:** Same as S0150/S0160.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0166 — f6314-6354 (263.125-264.792 s, 41 frames, 1.71 s) — shot SH054 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0218.jpg; entry EP0218, exit EP0219; second review: OK
- **Objects/placement (OBSERVED):** Builder at left (x~0.23-0.32,y~0.28-0.80); large dusty-red armchair at right (x~0.55-0.81,y~0.40-0.87) with a small figure lounging across it.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** black outline; chair dusty red with darker folds; lounging figure beige head
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.900 #af5151:0.059 #100504:0.022 #d7cab6:0.010 #543937:0.008
- **Hierarchy:** Large red armchair draws the eye first, then the builder.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive entry via EP0218; hard replace out via EP0219.
- **Narration (ASR, unverified):** that regular homeowners aren't.
- **Story function (INFERRED):** INFERRED: homeowner who can sit and wait versus builder (ASR).
- **Continuity:** S0165 plus armchair.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0167 — f6355-6371 (264.833-265.500 s, 17 frames, 0.71 s) — shot SH055 (inferred) — F7 text card
- **Evidence:** frames/ep_stable/e0219.jpg; entry EP0219, exit EP0220; second review: MINOR
- **Objects/placement (OBSERVED):** Red chunky word PRICES at left-centre (x~0.22-0.62,y~0.44-0.68, ~0.12 of frame height) with an upright kitchen knife, brown handle at bottom, blade pointing up-left, at right (x~0.66-0.87,y~0.12-0.67).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** bold black outline red lettering, chunky; knife grey blade with brown handle
- **Typography:** handwritten marker caps, deep red, ~13% frame height, very bold, left-aligned
- **Readable text:** PRICES
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.906 #0d0303:0.043 #c40921:0.024 #cfcfcf:0.015 #553735:0.012
- **Hierarchy:** Red word first, knife second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0219; knife rotates and cuts the word via EP0220.
- **Narration (ASR, unverified):** They have to cut
- **Story function (INFERRED):** INFERRED: visual pun for cutting prices (ASR: 'They have to cut').
- **Continuity:** Same word-and-knife asset continues in S0168.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0168 — f6372-6393 (265.542-266.417 s, 22 frames, 0.92 s) — shot SH055 (inferred) — F7 text card
- **Evidence:** frames/ep_stable/e0220.jpg; entry EP0220, exit EP0221; second review: OK
- **Objects/placement (OBSERVED):** Red word at left-centre (x~0.16-0.63,y~0.44-0.74) cut by a white diagonal gap through the 'IC'/'E' letters; kitchen knife lying nearly horizontal, handle at right, blade pointing left (x~0.52-0.87,y~0.56-0.82).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same style; cut line white
- **Typography:** handwritten marker caps, deep red, ~13% height, bold, with white slash gap
- **Readable text:** PRICES (letters partly cut: 'PRIC ES')
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.917 #0b0303:0.041 #c40a22:0.023 #532929:0.014 #a2a0a1:0.005
- **Hierarchy:** Cut word then knife.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Entry via EP0220 (knife rotates, cut appears); hard replace out via EP0221.
- **Narration (ASR, unverified):** cut prices.
- **Story function (INFERRED):** INFERRED: payoff of the pun.
- **Continuity:** S0167 variant.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0169 — f6394-6431 (266.458-268.000 s, 38 frames, 1.58 s) — shot SH056 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0221.jpg; entry EP0221, exit EP0222; second review: MINOR
- **Objects/placement (OBSERVED):** Blue wordmark centred (x~0.18-0.83,y~0.43-0.57, ~0.10 of frame height); nothing else.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** vector logo, flat blue
- **Typography:** bold geometric sans caps, blue (~#0B5CA8), ~8% frame height
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.955 #0860a6:0.032 #1b5e91:0.007 #5488af:0.003 #a7cce6:0.002
- **Hierarchy:** Wordmark alone.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0221; hard hat and hammer added via EP0222.
- **Narration (ASR, unverified):** Lenar is the second largest home
- **Story function (INFERRED):** INFERRED: introduces the named public homebuilder (ASR: second largest builder).
- **Continuity:** Same logo reused in S0170, S0182-S0187, S0215-S0218.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0170 — f6432-6461 (268.042-269.250 s, 30 frames, 1.25 s) — shot SH056 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0222.jpg; entry EP0222, exit EP0223; second review: OK
- **Objects/placement (OBSERVED):** Blue wordmark centred (x~0.14-0.84,y~0.45-0.57) with a glossy yellow hard hat on its upper-left (x~0.14-0.30,y~0.31-0.50) and a brown hammer at lower right (x~0.78-0.87,y~0.50-0.60).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** logo + hand-drawn hat (glossy yellow, black outline) and hammer
- **Typography:** bold blue sans caps
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.935 #0c60a2:0.038 #e3db49:0.013 #15120b:0.007 #6d8ea3:0.006
- **Hierarchy:** Wordmark, then the quirky hat.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Additive via EP0222; hard replace out via EP0223.
- **Narration (ASR, unverified):** home builder in the country.
- **Story function (INFERRED):** INFERRED: personifies the builder company.
- **Continuity:** S0169 plus hat/hammer; reused in S0187.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0171 — f6462-6516 (269.292-271.542 s, 55 frames, 2.29 s) — shot SH057 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0223.jpg; entry EP0223, exit EP0227; second review: OK
- **Objects/placement (OBSERVED):** Press-release web page centred-left: tiny wordmark at top-left (x~0.18-0.26,y~0.12), 'Investor Relations' menu (x~0.18-0.32,y~0.20), back link (y~0.31), two-line serif headline (x~0.18-0.78,y~0.33-0.52), date (x~0.18,y~0.62), highlights heading and bullets (y~0.70-0.97); thin scrollbar at x~0.86.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline
- **Typography:** clean web serif headline ~8% frame height dark grey; body sans ~2%
- **Readable text:** Lennar Reports Third Quarter 2026 Results; Investor Relations; Back to Press Releases; Sep 16, 2026; Third Quarter 2026 Highlights
- **Unreadable/uncertain text:** bullet text (net earnings per diluted share, new orders decreased 9%, backlog) too small
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.952 #dadada:0.019 #afafb0:0.014 #888888:0.010 #444646:0.005
- **Hierarchy:** Headline first, date second (blue selection and cursor are animated by EP0224-0226).
- **Camera/motion:** STATIC 2D; cursor and selection micro-motion; **entry/exit:** Hard replace in via EP0223; blue selection and cursor micro-changes EP0224-EP0226; a second page slides in via EP0227.
- **Narration (ASR, unverified):** They reported earnings on September 16,
- **Story function (INFERRED):** INFERRED: shows the earnings release date (ASR: reported earnings Sep 16).
- **Continuity:** Same capture continues into S0172.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0046 (HIGHLIGHT_ADD, f6479) Selection reaches the last digit of the date; the text I-beam cursor shifts slightly at its end (native crop).; EVI0047 (HIGHLIGHT_ADD, f6482) Blue text-selection highlight over the date string 'Sep 16, 202(6)' plus a text I-beam cursor appear in a press-release page; EVI0048 (OTHER, f6484) The mouse cursor at the end of the selected date changes from I-beam to an arrow and nudges.
- **Intra-state motion intervals:** EP0224

## S0172 — f6536-6586 (272.375-274.458 s, 51 frames, 2.12 s) — shot SH057 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0227.jpg; entry EP0227, exit EP0229; second review: MINOR
- **Objects/placement (OBSERVED):** Press-release page remains at left (x~0.0-0.62) with the date now highlighted blue; at upper right a second web page (x~0.42-1.0,y~0.11-0.95) with dark-blue header banner, breadcrumbs, 'Press Release' heading and body text with a yellow highlighted sentence.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline; yellow marker overlay
- **Typography:** web sans/serif small; header white on navy
- **Readable text:** Board of Governors of the Federal Reserve System; Press Release; Federal Reserve issues FOMC statement; Sep 16, 2026
- **Unreadable/uncertain text:** body statement text, menus
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.773 #3b4c5f:0.091 #687788:0.057 #a4a8aa:0.041 #d4d6d4:0.038
- **Hierarchy:** Navy header band of the second page attracts first, then the yellow highlight.
- **Camera/motion:** STATIC 2D (slide-in at start); **entry/exit:** Page slides in via EP0227 (19f); yellow highlight via EP0228; hard replace out via EP0229.
- **Narration (ASR, unverified):** enough the same day the Fed raised rates.
- **Story function (INFERRED):** INFERRED: shows the Fed rate decision made the same day (ASR).
- **Continuity:** Overlay on S0171.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state motion intervals:** EP0228

## S0173 — f6587-6618 (274.500-275.792 s, 32 frames, 1.33 s) — shot SH058 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0229.jpg; entry EP0229, exit EP0230; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling spiky-hair presenter at left (head x~0.07-0.24,y~0.15-0.49, thin body to y~0.95) holding a long pointer stick that runs from lower left to the table; financial table document at right (x~0.48-0.87,y~0.07-0.93) with title lines and columns.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** presenter in thick black marker outline, flat fills, wobbly hand line; table scanned-document look
- **Typography:** document sans/serif tiny black
- **Readable text:** none
- **Unreadable/uncertain text:** all table rows and numbers
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.884 #e5d1c0:0.052 #9e9e9d:0.040 #615e5d:0.013 #090605:0.011
- **Hierarchy:** Presenter first, then table block.
- **Camera/motion:** STATIC then ZOOM-in (EP0230); **entry/exit:** Hard replace in via EP0229; zooms into the table via EP0230.
- **Narration (ASR, unverified):** Lenar's profit per share was
- **Story function (INFERRED):** INFERRED: introduces earnings table (profit per share).
- **Continuity:** Table continues zoomed in S0174.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0174 — f6650-6675 (277.125-278.167 s, 26 frames, 1.08 s) — shot SH058 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0230.jpg; entry EP0230, exit EP0232; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter's head at left (x~0.15-0.33,y~0.15-0.5) with pointer; table zoomed to large type across x~0.34-1.0 (rows 'Net earnings attributable...', 'Basic and diluted ... per share') with a red rectangle (x~0.69-0.88,y~0.27-0.33) around the values 1.19 and 2.29.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** presenter marker line; red hand-drawn box
- **Typography:** financial table sans ~2.5% height black
- **Readable text:** Net earnings attributable to Lennar; Basic and diluted average shares outstanding; Basic and diluted earnings per share; $ 1.19 2.29 3.36; Supplemental information; EBIT
- **Unreadable/uncertain text:** other row values (small)
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.880 #e7d2c1:0.052 #685b5d:0.029 #9c9999:0.024 #120e0e:0.016
- **Hierarchy:** Red box with the two per-share numbers.
- **Camera/motion:** ZOOM end state; STATIC; **entry/exit:** Arrives via zoom EP0230; selection sweep EP0231; hard replace out via EP0232 region swap.
- **Narration (ASR, unverified):** half from a year ago.
- **Story function (INFERRED):** INFERRED: shows profit per share fell by about half (ASR).
- **Continuity:** Zoomed version of S0173.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0049 (DRAW_ON_OR_REVEAL, f6651) Red rectangular outline is drawn around the '$ 1.19' per-share cell of a financial table (x~0.34-0.43,y~0.33-0.42)
- **Intra-state motion intervals:** EP0231

## S0175 — f6702-6766 (279.292-281.958 s, 65 frames, 2.71 s) — shot SH058 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0232.jpg; entry EP0232, exit EP0233; second review: OK
- **Objects/placement (OBSERVED):** Spiky-hair presenter at left (head x~0.23-0.40,y~0.18-0.5) with smile; social-profile card at right (x~0.45-0.88,y~0.14-0.88): large blue wordmark at top, circular portrait photo of a smiling man at left of card, name, title lines, buttons, About section text.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** presenter marker line; card screenshot rounded white panel on light grey
- **Typography:** UI sans small; wordmark bold blue caps ~7%
- **Readable text:** Stuart Miller; Executive Chairman, Chief Executive Officer and President at Lennar; About
- **Unreadable/uncertain text:** About paragraph, activity section
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.915 #e3cdbb:0.046 #817271:0.016 #100c0b:0.014 #16619c:0.009
- **Hierarchy:** Large wordmark and portrait first, presenter second.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Card rises in via EP0232 motion; hard replace out via EP0233.
- **Narration (ASR, unverified):** the CEO Stuart Miller said it out loud.
- **Story function (INFERRED):** INFERRED: introduces the CEO (ASR: the CEO said it).
- **Continuity:** Profile card reused in S0213.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0176 — f6767-6841 (282.000-285.083 s, 75 frames, 3.12 s) — shot SH059 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0233.jpg; entry EP0233, exit EP0234; second review: OK
- **Objects/placement (OBSERVED):** Dark-mode transcript capture centred (x~0.13-0.87,y~0.17-0.80): top bar with purple logo text, search field and green button; speaker name and role at left, timestamp at right, then a dense paragraph of light text.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** UI capture dark charcoal panel, white text; no drawing
- **Typography:** UI sans, light grey/white, body ~1.5% height; speaker name bold
- **Readable text:** Stuart Miller; Executive Chairman, CEO, and President; 0:09:34; quote: 'we are compromising margin in order to maintain volume' (inside paragraph)
- **Unreadable/uncertain text:** most of the paragraph (small light text)
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.540 #111619:0.323 #292f33:0.065 #647674:0.039 #b0b4b7:0.033
- **Hierarchy:** Dark rectangle on white canvas, then the quote line.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0233; hard replace out via EP0234.
- **Narration (ASR, unverified):** We are compromising margin in order to maintain volume.
- **Story function (INFERRED):** INFERRED: source quote of the CEO about price/margin trade-off.
- **Continuity:** Same capture type as S0181, S0214.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0177 — f6842-6870 (285.125-286.292 s, 29 frames, 1.21 s) — shot SH060 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0234.jpg; entry EP0234, exit EP0235; second review: OK
- **Objects/placement (OBSERVED):** Large smiling presenter with squinting eyes (head x~0.38-0.62,y~0.15-0.55) holding open dictionary (brown pages, UK flag on cover, vertical label) at chest (x~0.41-0.58,y~0.63-0.92).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline, peach head, cream/tan book
- **Typography:** spine label tiny caps
- **Readable text:** DICTIONARY
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.878 #f4d3b6:0.064 #090505:0.027 #dbb991:0.024 #715a55:0.008
- **Hierarchy:** Giant face, then book.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace in via EP0234; hard replace out via EP0235.
- **Narration (ASR, unverified):** The translation,
- **Story function (INFERRED):** INFERRED: 'The translation' - presenter acting as translator.
- **Continuity:** Presenter same as S0149/S0176 family.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0178 — f6871-6907 (286.333-287.833 s, 37 frames, 1.54 s) — shot SH061 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0235.jpg; entry EP0235, exit EP0236; second review: OK
- **Objects/placement (OBSERVED):** Neutral presenter at left (head x~0.18-0.34,y~0.18-0.49, body to y~0.85, arms out); three building icons at right: pink house (x~0.52-0.63,y~0.32-0.54), tall grey-cream tower (x~0.68-0.83,y~0.22-0.53), teal double house (x~0.62-0.77,y~0.57-0.78).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; flat pastel building fills
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.876 #e5d6c1:0.049 #090807:0.037 #58574f:0.020 #b7a9a0:0.018
- **Hierarchy:** Presenter then the colourful icon trio.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0235; tags added via EP0236.
- **Narration (ASR, unverified):** we're being forced to sell our houses for
- **Story function (INFERRED):** INFERRED: 'we're being forced to sell our houses for...'.
- **Continuity:** Layout kept in S0179.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0179 — f6908-6976 (287.875-290.708 s, 69 frames, 2.88 s) — shot SH061 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0236.jpg; entry EP0236, exit EP0238; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter at left (head x~0.17-0.34,y~0.18-0.49) with lowered arm; same three buildings (pink house x~0.50-0.63, tower x~0.68-0.83, teal houses x~0.62-0.77) each with a yellow tilted price tag marked $20 attached by a thin string, tags at upper-left of each building.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same plus yellow tag fill with red hand-lettered amount
- **Typography:** handwritten marker red on yellow ~4% height
- **Readable text:** $20 (three tags)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.856 #dacbb9:0.066 #0a0907:0.041 #625b4e:0.024 #e1d03a:0.014
- **Hierarchy:** Yellow tags pop against pastel buildings.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Tags added via EP0236; arm pose changes via EP0237; hard replace out via EP0238.
- **Narration (ASR, unverified):** houses for cheaper, just so we can keep selling houses.
- **Story function (INFERRED):** INFERRED: lowered prices ('houses for cheaper').
- **Continuity:** S0178 plus tags.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0050 (POSE_SWAP, f6929) Presenter's lower left arm drops from a sharp bent raised pose to a lower hanging pose (native crop).

## S0180 — f6977-7009 (290.750-292.083 s, 33 frames, 1.38 s) — shot SH062 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0238.jpg; entry EP0238, exit EP0239; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter alone and smiling, head x~0.42-0.58,y~0.18-0.42, arms out, body to y~0.86; rest empty.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline, peach head
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f4d3b6:0.031 #080605:0.011 #615b57:0.002 #aba59f:0.002
- **Hierarchy:** Single smiling figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0238; hard replace out via EP0239.
- **Narration (ASR, unverified):** Then he explained why.
- **Story function (INFERRED):** INFERRED: transition beat 'Then he explained why'.
- **Continuity:** Same pose family as S0149/S0210.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0181 — f7010-7136 (292.125-297.375 s, 127 frames, 5.29 s) — shot SH063 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0239.jpg; entry EP0239, exit EP0240; second review: MINOR
- **Objects/placement (OBSERVED):** Dark transcript capture at upper left (x~0.18-0.82,y~0.17-0.83): top bar, speaker name, timestamp, long paragraph; at lower right two icons overlap its corner: a small cream house with red roof (x~0.68-0.76,y~0.74-0.90) and a grey tall building (x~0.79-0.91,y~0.62-0.89).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** dark UI capture; marker-outline icons
- **Typography:** UI sans light on dark
- **Readable text:** Stuart Miller; Executive Chairman, CEO, and President; 0:12:45; opening words 'Every home we close retires a homesite that was priced for a market that no longer exists...'; no yellow highlight visible in this tile
- **Unreadable/uncertain text:** most of the paragraph (small light text)
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.553 #13181b:0.329 #42494b:0.043 #768485:0.042 #babcbb:0.032
- **Hierarchy:** Dark panel then icons at its corner.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0239; hard replace out via EP0240.
- **Narration (ASR, unverified):** Every home we close retires a home site that was priced for a market that no longer exists.
- **Story function (INFERRED):** INFERRED: quote about land priced for older market (ASR).
- **Continuity:** Capture type as S0176.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0182 — f7137-7163 (297.417-298.500 s, 27 frames, 1.12 s) — shot SH064 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0240.jpg; entry EP0240, exit EP0241; second review: MINOR
- **Objects/placement (OBSERVED):** Small blue wordmark top-left (x~0.10-0.41,y~0.15-0.22); everything else blank.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** vector logo
- **Typography:** bold blue sans caps ~5%
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.990 #0a60a4:0.005 #1b5a8a:0.003 #9fc4df:0.001 #5b8bb0:0.001
- **Hierarchy:** Logo alone.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0240; land blob appears via EP0241.
- **Narration (ASR, unverified):** Lenar bought much of their
- **Story function (INFERRED):** INFERRED: topic shifts to the builder's land.
- **Continuity:** Logo stays through S0183-S0186.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0183 — f7164-7246 (298.542-301.958 s, 83 frames, 3.46 s) — shot SH064 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0241.jpg; entry EP0241, exit EP0247; second review: OK
- **Objects/placement (OBSERVED):** Wordmark top-left (x~0.10-0.41,y~0.15-0.22); green irregular land blob lower centre (x~0.31-0.68,y~0.60-0.78); dollar sign, notes and check mark appear around it via micro-events EP0242-EP0246 (at right above blob).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** blob dark green flat fill with black outline; dollar sign green outlined; banknotes pale green with yellow coin; bright green check
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.948 #337d31:0.033 #125f99:0.008 #051205:0.007 #8facc0:0.003
- **Hierarchy:** Blob then growing money group.
- **Camera/motion:** STATIC 2D; additive micro pops; **entry/exit:** Blob in via EP0241; dollar, note stack, check via EP0242-0246; exit EP0247.
- **Narration (ASR, unverified):** their land when prices and profit margins were much more favorable.
- **Story function (INFERRED):** INFERRED: land bought earlier when prices and margins were favourable (ASR).
- **Continuity:** S0184 is the same without the money.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0051 (ADDITIVE_ENTRY, f7186) A green dollar sign appears above and right of the land blob.; EVI0052 (ADDITIVE_ENTRY, f7198) A single green banknote appears beside the dollar sign.; EVI0053 (ADDITIVE_ENTRY, f7203) A second banknote overlaps the first, making a small stack.; EVI0054 (ADDITIVE_ENTRY, f7210) A third note is layered into the stack beside the dollar sign.; EVI0055 (ADDITIVE_ENTRY, f7227) A bright green check mark appears at the right end of the land blob.

## S0184 — f7247-7275 (302.000-303.167 s, 29 frames, 1.21 s) — shot SH064 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0247.jpg; entry EP0247, exit EP0248; second review: MINOR
- **Objects/placement (OBSERVED):** Wordmark top-left; only the dark-green land blob lower centre (x~0.31-0.68,y~0.60-0.78).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** same
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.948 #337d31:0.033 #135f99:0.008 #061305:0.007 #8eabbe:0.003
- **Hierarchy:** Blob only.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Money and check removed via EP0247; house added via EP0248.
- **Narration (ASR, unverified):** The only way to get rid of it is
- **Story function (INFERRED):** INFERRED: land bare before building.
- **Continuity:** After S0183, before S0185.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0185 — f7276-7333 (303.208-305.583 s, 58 frames, 2.42 s) — shot SH064 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0248.jpg; entry EP0248, exit EP0250; second review: MINOR
- **Objects/placement (OBSERVED):** Wordmark top-left; land blob with a large red-roofed cream house with two chimneys and bushes on top (house x~0.40-0.61,y~0.46-0.69; blob x~0.31-0.68,y~0.58-0.78).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; red roof, tan wall, green shrubs
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.929 #536d3e:0.031 #151108:0.017 #b3a798:0.014 #17629b:0.008
- **Hierarchy:** House on land.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** House added via EP0248 (and a small sign via micro EP0249); hard exit via EP0250.
- **Narration (ASR, unverified):** is to build on it and sell at today's prices,
- **Story function (INFERRED):** INFERRED: 'build on it and sell'.
- **Continuity:** Same land piece as S0183.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0056 (ADDITIVE_ENTRY, f7296) A small red for-sale sign appears at the right end of the land under the house.

## S0186 — f7334-7371 (305.625-307.167 s, 38 frames, 1.58 s) — shot SH064 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0250.jpg; entry EP0250, exit EP0251; second review: OK
- **Objects/placement (OBSERVED):** Wordmark top-left; spiky-hair smiling presenter at left (head x~0.10-0.26,y~0.44-0.72, body to bottom); land+house group at x~0.31-0.71 with red for-sale sign at its right (x~0.60-0.71,y~0.64-0.80).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** white on red sign small
- **Readable text:** SALE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.881 #e0c7b1:0.042 #386e57:0.033 #150d07:0.028 #a94c46:0.015
- **Hierarchy:** Presenter and sign together read 'selling'.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Presenter added via EP0250; hard replace out via EP0251.
- **Narration (ASR, unverified):** whatever those turn out to be.
- **Story function (INFERRED):** INFERRED: 'sell at today's prices, whatever those turn out to be'.
- **Continuity:** S0185 plus presenter.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0187 — f7372-7408 (307.208-308.708 s, 37 frames, 1.54 s) — shot SH065 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0251.jpg; entry EP0251, exit EP0252; second review: OK
- **Objects/placement (OBSERVED):** Large blue wordmark centred (x~0.14-0.88,y~0.44-0.58) with yellow hard hat at upper-left (x~0.14-0.28,y~0.31-0.50) and brown hammer at lower right (x~0.80-0.88,y~0.50-0.60).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** logo + hand-drawn glossy hat and hammer
- **Typography:** bold blue sans caps ~11% height
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.935 #0c60a2:0.038 #e3db4a:0.013 #14110b:0.007 #7192a8:0.006
- **Hierarchy:** Wordmark and hat.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0251; hard replace out via EP0252.
- **Narration (ASR, unverified):** And it's not just Lenar.
- **Story function (INFERRED):** INFERRED: 'And it's not just Lenar' - company stands for industry.
- **Continuity:** Same asset as S0170.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0188 — f7409-7478 (308.750-311.625 s, 70 frames, 2.92 s) — shot SH066 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0252.jpg; entry EP0252, exit EP0253; second review: OK
- **Objects/placement (OBSERVED):** Association web page capture upper left (x~0.08-0.62,y~0.11-0.44): logo, search field, menu, and a short paragraph with the line about 66% highlighted by a thin left bar; topknot builder with a smile at right (head x~0.66-0.80,y~0.25-0.55, hammer raised, body to y~0.93).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** screenshot + marker figure
- **Typography:** small web sans
- **Readable text:** The latest HMI survey found that 38% of builders cut prices in September...; Meanwhile, 66% of builders reported using sales incentives ... 63% in August and the highest share since 67% posted in December.
- **Unreadable/uncertain text:** menu items
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.914 #d6d1c5:0.035 #050403:0.024 #908c8e:0.015 #4e474e:0.012
- **Hierarchy:** Paragraph then figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0252; hard replace out via EP0253.
- **Narration (ASR, unverified):** Like I said, two -thirds of builders are offering incentives.
- **Story function (INFERRED):** INFERRED: confirms incentives statistic (ASR).
- **Continuity:** Article snippet is the same source as S0164.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0189 — f7479-7483 (311.667-311.833 s, 5 frames, 0.21 s) — shot SH067 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0253.jpg; entry EP0253, exit EP0254; second review: MINOR
- **Objects/placement (OBSERVED):** Spiky-hair presenter holding a long pointer, head x~0.15-0.30,y~0.25-0.53, body to y~0.93; blank elsewhere. State lasts 0.21 s (5 frames), a gap before the card slides in.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.952 #f3d2b7:0.032 #080504:0.011 #534a46:0.004 #918984:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0253; card slides in via EP0254.
- **Narration (ASR, unverified):** The biggest
- **Story function (INFERRED):** INFERRED: very short beat 'The biggest'.
- **Continuity:** Same presenter as S0190.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0190 — f7502-7530 (312.625-313.792 s, 29 frames, 1.21 s) — shot SH067 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0254.jpg; entry EP0254, exit EP0256; second review: OK
- **Objects/placement (OBSERVED):** Presenter at left (head x~0.15-0.30,y~0.25-0.53) with pointer; blue card at right (x~0.42-0.94,y~0.18-0.81): title text, phonetic line, definition, bent arrow and hand illustration and small coins at left of card.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** blue flat panel with pale illustration, white and black text
- **Typography:** bold sans ~5% title, definition ~3%
- **Readable text:** Buydown; [ˈbi-ˌdaun]; A mortgage financing technique where the buyer tries to get a lower interest rate for at least the mortgage's first few years and possibly for its lifetime.
- **Unreadable/uncertain text:** tiny source logo at bottom
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.631 #8fb7f6:0.284 #f2d2b7:0.033 #121c32:0.030 #546a8d:0.022
- **Hierarchy:** Blue card is largest; presenter's pointer leads to it.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Slides in via EP0254; pointer pose change via EP0255; hard replace out via EP0256.
- **Narration (ASR, unverified):** is the rate buydown.
- **Story function (INFERRED):** INFERRED: defines rate buydown.
- **Continuity:** Same card used in S0296 region (next shard).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0057 (POSE_SWAP, f7508) Presenter's pointer arm shifts so the pointer swings up toward the blue card.

## S0191 — f7531-7650 (313.833-318.792 s, 120 frames, 5.00 s) — shot SH068 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0256.jpg; entry EP0256, exit EP0257; second review: MINOR
- **Objects/placement (OBSERVED):** Trade-publication article capture at upper left (x~0.05-0.59,y~0.08-0.63): black masthead bar, nav items, paragraph with orange highlight 'Over 70%' and a second paragraph; bottom right a smiling figure reading a newspaper (head x~0.72-0.87,y~0.47-0.72; paper x~0.66-0.90,y~0.65-1.0).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** screenshot + marker figure; paper cream with scribbles
- **Typography:** serif article ~2%
- **Readable text:** THE BUILDER'S DAILY; Technology Architecture Capital Land Homebuilder Rankings Policy; 'Over 70% of builder mortgage originations now carry some form of rate buydown. Even more notable — 55% of those loans price at least 100 bps below market.'
- **Unreadable/uncertain text:** second paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.655 #f4f2f1:0.166 #d5c9b3:0.096 #171615:0.053 #787672:0.030
- **Hierarchy:** Masthead and highlighted quote.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0256; hard replace out via EP0257.
- **Narration (ASR, unverified):** More than 70 % of builder mortgage originations now carry some form of a rate buydown.
- **Story function (INFERRED):** INFERRED: source for the >70% buydown stat (ASR).
- **Continuity:** Reader figure unique to this state.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0192 — f7651-7714 (318.833-321.458 s, 64 frames, 2.67 s) — shot SH069 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0257.jpg; entry EP0257, exit EP0258; second review: MINOR
- **Objects/placement (OBSERVED):** Navy wordmark with script tagline centred (x~0.25-0.75,y~0.36-0.67): bold serif caps top line with registered mark and handwritten italic tagline below.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** vector logo navy
- **Typography:** bold condensed serif caps ~12% height; script tagline ~9%
- **Readable text:** D.R.HORTON; America's Builder
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.936 #091e4d:0.046 #d9e5f3:0.008 #9ba6be:0.005 #53607b:0.004
- **Hierarchy:** Wordmark.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0257; PDF viewer grows in via EP0258.
- **Narration (ASR, unverified):** D .R. Horton, the largest builder in the country,
- **Story function (INFERRED):** INFERRED: names the largest builder (ASR).
- **Continuity:** Unique wordmark.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0193 — f7755-7758 (323.167-323.292 s, 4 frames, 0.17 s) — shot SH069 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0258.jpg; entry EP0258, exit EP0259; second review: MINOR
- **Objects/placement (OBSERVED):** PDF-viewer capture (x~0.25-0.74,y~0.08-0.95): dark toolbar with filename text, dark thumbnail rail at left with page thumbnails, white transcript page at right with small text.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline; dark UI
- **Typography:** tiny UI sans
- **Readable text:** Q3 2026 - Earnings Call Tra... (toolbar)
- **Unreadable/uncertain text:** page text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.770 #292929:0.145 #dbdbdb:0.038 #b0b1b2:0.033 #6e6f6f:0.013
- **Hierarchy:** Dark frame around white page.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Grows in via EP0258; micro page swap via EP0259.
- **Narration (ASR, unverified):** at
- **Story function (INFERRED):** INFERRED: earnings-call transcript source.
- **Continuity:** State 0.17 s; near-twin S0194.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0194 — f7759-7769 (323.333-323.750 s, 11 frames, 0.46 s) — shot SH069 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0259.jpg; entry EP0259, exit EP0260; second review: MINOR
- **Objects/placement (OBSERVED):** Same viewer capture (x~0.25-0.73,y~0.08-0.95), a different transcript page showing in the right pane, thumbnail 15 highlighted in blue border.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline; dark UI
- **Typography:** tiny UI sans
- **Readable text:** Q3 2026 - Earnings Call Tra... (toolbar)
- **Unreadable/uncertain text:** page text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.770 #292a29:0.148 #b2b3b4:0.037 #dededf:0.033 #6f6f70:0.012
- **Hierarchy:** same.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Page swap via EP0259; zoom via EP0260.
- **Narration (ASR, unverified):** at 4 .9
- **Story function (INFERRED):** INFERRED: finds the quote page.
- **Continuity:** Near-duplicate of S0193 (0.46 s).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0058 (PAN_OR_SCROLL, f7768) Single-frame change inside a document-viewer capture: page canvas and thumbnail rail differ between f7768 and f7774, consistent with a page flip or scroll starting; precursor of an adjacent change

## S0195 — f7784-7810 (324.375-325.458 s, 27 frames, 1.12 s) — shot SH069 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0260.jpg; entry EP0260, exit EP0261; second review: MINOR
- **Objects/placement (OBSERVED):** Transcript page zoomed to fill x~0.04-0.62,y~0.06-0.99 with bold underlined speaker names and paragraphs, a red underline segment near the top; dark vertical bar right of page x~0.63-0.67; a mouse arrow at x~0.63,y~0.55.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline with red marker underline
- **Typography:** tiny bold underlined speaker lines ~1.2%
- **Readable text:** Jessica Hansen - Senior Vice President, Communications, D.R. Horton, Inc.; Michael Murray - Executive Vice President and Chief Operating Officer, D.R. Horton, Inc.; Thank you.
- **Unreadable/uncertain text:** paragraph text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.785 #272727:0.074 #cecdcd:0.063 #a0a0a0:0.057 #6f6c6d:0.021
- **Hierarchy:** Red underline and bold names.
- **Camera/motion:** ZOOM-in just before (EP0260); STATIC; **entry/exit:** Zoom via EP0260; underline draws via EP0262-EP0263; presenter appears via EP0261.
- **Narration (ASR, unverified):** % this summer,
- **Story function (INFERRED):** INFERRED: transcript of D.R. Horton's rate quote.
- **Continuity:** Same transcript as S0196-S0198.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0059 (OBJECT_MOTION, f7785) Screen-recording mouse arrow appears at far right edge (x~0.99,y~0.57) while a red underline starts on the transcript and the presenter's head enters at lower right

## S0196 — f7811-7872 (325.500-328.042 s, 62 frames, 2.58 s) — shot SH069 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0261.jpg; entry EP0261, exit EP0265; second review: OK
- **Objects/placement (OBSERVED):** Zoomed transcript at left (x~0.0-0.62); presenter at right (head x~0.65-0.83,y~0.28-0.60, bent arms, body to bottom) on a dark vertical bar at x~0.62-0.67; red underlines extend over phrase 'slightly to 16%' and further sentences.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline + marker presenter
- **Typography:** tiny
- **Readable text:** none
- **Unreadable/uncertain text:** document text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.709 #e5d3c4:0.104 #222121:0.091 #abaaaa:0.063 #7d7576:0.033
- **Hierarchy:** Presenter's face vs underlined line.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Presenter pops in via EP0261; underlines drawn via EP0262/EP0263; micro EP0264 no change; hard replace out via EP0265.
- **Narration (ASR, unverified):** while the market rate was around six and a half, which
- **Story function (INFERRED):** INFERRED: 'at 4.9% this summer, while the market rate was around six and a half'.
- **Continuity:** S0195 plus presenter.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0060 (DRAW_ON_OR_REVEAL, f7813) Red underline stroke is drawn under a line of transcript text (x~0.26-0.40,y~0.21); EVI0061 (DRAW_ON_OR_REVEAL, f7817) A red underline stroke extends rightward beneath a phrase in the upper left transcript (native crop).; EVI0062 (DRAW_ON_OR_REVEAL, f7819) Red underline/box stroke continues in the left part of the transcript text (x~0.10-0.35,y~0.18-0.24); EVI0063 (DRAW_ON_OR_REVEAL, f7830) The red underline continues, with a bracket-like turn under the next phrases (native crop).; EVI0064 (DRAW_ON_OR_REVEAL, f7833) Long red rectangular outline is extended across a transcript line (x~0.14-0.76,y~0.34-0.46) over 27 frames; EVI0065 (CODEC_ARTIFACT, f7861) No visible content change at the document's right edge near the presenter (native crop identical).

## S0197 — f7873-7921 (328.083-330.083 s, 49 frames, 2.04 s) — shot SH070 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0265.jpg; entry EP0265, exit EP0266; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling presenter centred (head x~0.42-0.58,y~0.19-0.49, thin body to y~0.86, arms out).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f3d2b7:0.032 #080505:0.011 #554e4a:0.002 #9c9590:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0265; hard replace out via EP0266.
- **Narration (ASR, unverified):** which is how we end up in a situation that
- **Story function (INFERRED):** INFERRED: beat 'which is how we end up in a situation'.
- **Continuity:** Same pose as S0149.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0198 — f7922-7953 (330.125-331.417 s, 32 frames, 1.33 s) — shot SH070 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0266.jpg; entry EP0266, exit EP0267; second review: MINOR
- **Objects/placement (OBSERVED):** Frowning presenter at left (head x~0.17-0.33,y~0.25-0.54, arm holding a long diagonal pointer); green chalkboard with brown frame at right (x~0.38-0.95,y~0.11-0.78) lettered in white chalk.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; board green with brown frame
- **Typography:** handwritten chalk white, ~13% height
- **Readable text:** NOT great
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.624 #38843f:0.182 #6f544a:0.085 #060503:0.072 #ebd1b7:0.037
- **Hierarchy:** Board lettering is the focus, then frown.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0266; hard replace out via EP0267.
- **Narration (ASR, unverified):** that shouldn't be happening. In
- **Story function (INFERRED):** INFERRED: 'a situation that shouldn't be happening'.
- **Continuity:** Unique board.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0199 — f7954-8112 (331.458-338.042 s, 159 frames, 6.62 s) — shot SH071 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0267.jpg; entry EP0267, exit EP0269; second review: OK
- **Objects/placement (OBSERVED):** Blog article capture at left (x~0.08-0.52,y~0.15-0.85): logo, search bar, heading and article text with yellow highlight; cartoon tan-red mansion at right (x~0.56-0.89,y~0.2-0.55); red -$25,000 text added later (EP0268) above house.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** screenshot + marker house
- **Typography:** small web sans; heading bold blue ~3%
- **Readable text:** Eye On Housing; New vs. Existing Home Prices: What the National Median Misses; In the second quarter of 2026, the national median price for a new single-family home was $410,700, $25,000 lower than ... existing home ($435,700)
- **Unreadable/uncertain text:** rest of body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfb:0.886 #726159:0.036 #aea08d:0.028 #19181a:0.027 #c9cfd0:0.023
- **Hierarchy:** Heading, highlight, red amount.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0267; micro EP0268; hard replace out via EP0269.
- **Narration (ASR, unverified):** In the second quarter, the typical new home sold for about $25 ,000 less than the typical existing home,
- **Story function (INFERRED):** INFERRED: evidence that new homes are $25k cheaper.
- **Continuity:** Article continues S0206-S0209.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0066 (ADDITIVE_ENTRY, f8023) A red handwritten negative dollar amount appears above the house at right.

## S0200 — f8113-8201 (338.083-341.750 s, 89 frames, 3.71 s) — shot SH072 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0269.jpg; entry EP0269, exit EP0271; second review: OK
- **Objects/placement (OBSERVED):** Two-line price chart (x~0.18-0.82,y~0.08-0.91): red and blue lines rising 2010-2026, legend, y axis $0-$500; small cream house doodle with red roof within plot (x~0.65-0.75,y~0.48-0.65); logo lower right; second small dark house added at EP0270.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** chart image + marker house
- **Typography:** chart sans tiny; title bold ~2.5%
- **Readable text:** Median Sales Price of U.S. Single-Family Homes; New Home Price; Existing Home Price; Sales Price (thousands, NSA)
- **Unreadable/uncertain text:** axis values, source line
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.936 #ddd9d6:0.031 #9b9498:0.012 #6b434a:0.012 #121011:0.008
- **Hierarchy:** Red and blue lines crossing at right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0269; house addition EP0270; zoom into the chart via EP0271.
- **Narration (ASR, unverified):** which means the brand new house is now cheaper than the used one. It's
- **Story function (INFERRED):** INFERRED: new home price now below existing (ASR).
- **Continuity:** Same chart reused in S0201.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0067 (ADDITIVE_ENTRY, f8180) A second smaller dark-roofed house appears right of the small house on the chart.

## S0201 — f8229-8299 (342.917-345.833 s, 71 frames, 2.96 s) — shot SH072 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0271.jpg; entry EP0271, exit EP0273; second review: OK
- **Objects/placement (OBSERVED):** Chart zoomed so only its right/middle part shows (x~0.0-0.57, partly cropped; heading text cut at left), lines crossing; presenter at right (head x~0.74-0.92,y~0.31-0.64) with long pointer reaching chart; a red hand-lettered word near pointer (EP0272).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** chart + marker figure
- **Typography:** chart sans ~3%; red marker word ~3%
- **Readable text:** '... of U.S. Single-Family Homes'; Existing Home Price; 'ever!' (red)
- **Unreadable/uncertain text:** axis scale
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.915 #efd2bb:0.042 #080707:0.017 #593641:0.016 #958f95:0.009
- **Hierarchy:** Pointer tip on crossing lines.
- **Camera/motion:** ZOOM-in at start (EP0271); **entry/exit:** Zoom via EP0271; red word EP0272; hard replace out via EP0273.
- **Narration (ASR, unverified):** the Home Builders Association has ever measured.
- **Story function (INFERRED):** INFERRED: 'cheaper than used... ever measured'.
- **Continuity:** Continuation of S0200.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0068 (TEXT_CHANGE, f8270) A short red hand-lettered word with exclamation appears near the chart's right edge by the pointer tip.

## S0202 — f8300-8357 (345.875-348.250 s, 58 frames, 2.42 s) — shot SH073 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0273.jpg; entry EP0273, exit EP0275; second review: MINOR
- **Objects/placement (OBSERVED):** Single green-tie figure at left (head x~0.22-0.33,y~0.24-0.40, body to y~0.83); empty rest.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.971 #dbc6b4:0.013 #050504:0.012 #6e8566:0.003 #42433d:0.001
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0273; pose change via EP0274.
- **Narration (ASR, unverified):** It's like walking onto a car lot and finding the
- **Story function (INFERRED):** INFERRED: introduces the car-lot analogy.
- **Continuity:** Same figure as S0157-S0159.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0069 (POSE_SWAP, f8343) Green-tie figure's arms/pose change: right arm raised, mouth changes.

## S0203 — f8358-8429 (348.292-351.250 s, 72 frames, 3.00 s) — shot SH073 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0275.jpg; entry EP0275, exit EP0277; second review: MINOR
- **Objects/placement (OBSERVED):** Green-tie figure at left (head x~0.22-0.33,y~0.25-0.49, arms bent out, surprised mouth); red sports car at right (x~0.43-0.91,y~0.45-0.78) with cyan windows.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; car red, black wheels
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.857 #ac2125:0.057 #170909:0.040 #a9d0c4:0.032 #4b4841:0.015
- **Hierarchy:** Car then figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Pose via EP0274, car via EP0275; hard exit later via EP0277 pan.
- **Narration (ASR, unverified):** the new model of your favorite car costs less than the one with 90
- **Story function (INFERRED):** INFERRED: 'the new model of your favorite car'.
- **Continuity:** Car reused in S0204.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0070 (ADDITIVE_ENTRY, f8400) A yellow price tag with a dollar amount appears above the car's front.

## S0204 — f8446-8470 (351.958-352.958 s, 25 frames, 1.04 s) — shot SH073 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0277.jpg; entry EP0277, exit EP0278; second review: OK
- **Objects/placement (OBSERVED):** Scene panned right: small blue compact car at left (x~0.05-0.43,y~0.35-0.74) with $99 tag above; green-tie figure at centre (x~0.48-0.66); red sports car cropped at right (x~0.72-1.0) with $20 tag. 1.04 s state.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; blue car, yellow tags
- **Typography:** handwritten red on yellow
- **Readable text:** $99; $20
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.766 #5674a3:0.089 #151116:0.076 #aa2424:0.037 #ded070:0.031
- **Hierarchy:** Blue car then tags.
- **Camera/motion:** PAN just before (EP0277); **entry/exit:** Pan via EP0277 (16f); hard replace out via EP0278.
- **Narration (ASR, unverified):** ,000 miles on it.
- **Story function (INFERRED):** INFERRED: new car cheaper than used one.
- **Continuity:** Extension of S0203.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0205 — f8471-8496 (353.000-354.042 s, 26 frames, 1.08 s) — shot SH074 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0278.jpg; entry EP0278, exit EP0279; second review: MINOR
- **Objects/placement (OBSERVED):** Large red-roofed tan mansion with white columns, chimney, tall right wing, bushes at both sides, centred (x~0.20-0.80,y~0.19-0.78).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; red roof, tan wall
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfc:0.816 #0e0706:0.062 #c0a181:0.054 #5d7355:0.036 #a9433e:0.032
- **Hierarchy:** House.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0278; hard replace to a smaller house via EP0279.
- **Narration (ASR, unverified):** Part of that is builders shrinking
- **Story function (INFERRED):** INFERRED: 'builders shrinking the product' - big house before shrinking.
- **Continuity:** S0205 then S0206 house is smaller.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0206 — f8497-8522 (354.083-355.125 s, 26 frames, 1.08 s) — shot SH074 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0279.jpg; entry EP0279, exit EP0280; second review: MINOR
- **Objects/placement (OBSERVED):** Smaller version of the house (single gable, no wing), x~0.31-0.66,y~0.31-0.77, centred-left.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.887 #0e0706:0.034 #cbaa87:0.027 #d7e3e6:0.027 #8a4a45:0.025
- **Hierarchy:** House.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Swap via EP0279; hard replace out via EP0280 (article scroll).
- **Narration (ASR, unverified):** shrinking the product.
- **Story function (INFERRED):** INFERRED: shrinking the product.
- **Continuity:** Shrunken version of S0205.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0207 — f8546-8556 (356.125-356.542 s, 11 frames, 0.46 s) — shot SH075 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0280.jpg; entry EP0280, exit EP0281; second review: MINOR
- **Objects/placement (OBSERVED):** Article capture centred (x~0.06-0.76,y~0.06-0.71) cropped at top at the end of a chart axis, two paragraphs: 'There are several factors...' and 'Meanwhile, new home pricing is more volatile...' with blue links.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline
- **Typography:** web sans ~2.4% grey, blue links
- **Readable text:** There are several factors for this new trend. Tight inventory continues to push prices for existing homes...; Meanwhile, new home pricing is more volatile ... challenges ... smaller lots ... incentives
- **Unreadable/uncertain text:** bottom lines
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.920 #d9dadb:0.027 #abaeb0:0.018 #484848:0.017 #7c7f81:0.017
- **Hierarchy:** Body text.
- **Camera/motion:** SCROLL up just before; **entry/exit:** Scrolls in via EP0280; hard small scroll EP0281.
- **Narration (ASR, unverified):** to affordability
- **Story function (INFERRED):** INFERRED: reason for shrinking product.
- **Continuity:** Same page S0208/S0209.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0208 — f8560-8678 (356.708-361.625 s, 119 frames, 4.96 s) — shot SH075 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0281.jpg; entry EP0281, exit EP0282; second review: MINOR
- **Objects/placement (OBSERVED):** Same article page (x~0.06-0.76) scrolled a bit further; orange highlight around 'home builders' in second paragraph.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline; orange highlight
- **Typography:** web sans ~2.4%
- **Readable text:** ... Despite various challenges facing the industry, home builders are adapting to affordability challenges by building on smaller lots, constructing smaller homes, and offering incentives.
- **Unreadable/uncertain text:** remaining text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.840 #e8eaea:0.093 #b2b3af:0.027 #807f78:0.021 #4a4845:0.020
- **Hierarchy:** Highlight.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Scroll EP0281 ends; hard replace/overlay via EP0282.
- **Narration (ASR, unverified):** affordability challenges, and the starter home is being rebuilt on smaller lots in smaller homes and
- **Story function (INFERRED):** INFERRED: 'builders shrinking the product' (ASR).
- **Continuity:** S0207 -> S0209.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0209 — f8679-8805 (361.667-366.917 s, 127 frames, 5.29 s) — shot SH075 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0282.jpg; entry EP0282, exit EP0283; second review: MINOR
- **Objects/placement (OBSERVED):** Same article with orange highlight extended over 'home builders are adapting ... building on smaller lots, constructing smaller homes,'; three building icons at right (pink house x~0.66-0.74,y~0.57-0.67, tower x~0.78-0.90,y~0.47-0.76, teal houses x~0.74-0.87,y~0.78-0.90).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** third-party web-page screenshot cut in as a flat rectangle, no hand-drawn outline; icons marker outline
- **Typography:** web sans ~2.5%
- **Readable text:** home builders are adapting to affordability challenges by building on smaller lots, constructing smaller homes, and offering incentives. According to NAHB's Home Building Geography Index, new homes are also shifting away from dense population centers
- **Unreadable/uncertain text:** remaining text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.863 #b9bab7:0.052 #615e57:0.041 #dda42a:0.025 #1d1710:0.020
- **Hierarchy:** Highlight, then icons.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Icons added via EP0282; hard replace out via EP0283.
- **Narration (ASR, unverified):** and being moved from dense population areas that are more expensive to less expensive smaller metro areas.
- **Story function (INFERRED):** INFERRED: smaller homes in less dense metros.
- **Continuity:** S0208 plus icons; icons same as S0178.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0210 — f8806-8831 (366.958-368.000 s, 26 frames, 1.08 s) — shot SH076 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0283.jpg; entry EP0283, exit EP0284; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling presenter alone centred (head x~0.41-0.59,y~0.18-0.50, arms out to bent legs).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f4d3b7:0.031 #080504:0.011 #56504c:0.002 #a09a95:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0283; hard replace out via EP0284.
- **Narration (ASR, unverified):** But even that has a limit because
- **Story function (INFERRED):** INFERRED: 'But even that has a limit'.
- **Continuity:** Same as S0149/S0180.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0211 — f8832-8924 (368.042-371.875 s, 93 frames, 3.88 s) — shot SH077 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0284.jpg; entry EP0284, exit EP0286; second review: MINOR
- **Objects/placement (OBSERVED):** Worried topknot builder at left (x~0.22-0.31,y~0.28-0.80) and a hooded grey figure with sunglasses holding a green bill at right (x~0.73-0.88,y~0.36-0.78).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; hoodie flat grey
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.957 #090606:0.015 #d8c8b7:0.012 #898d85:0.011 #43423d:0.005
- **Hierarchy:** Two small figures.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0284; dollar sign appears via EP0285.
- **Narration (ASR, unverified):** because the thing standing between a builder and a sale isn't always the price.
- **Story function (INFERRED):** INFERRED: builder vs buyer.
- **Continuity:** Buyer reused in S0212.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0071 (ADDITIVE_ENTRY, f8892) A green dollar sign appears between the two figures.

## S0212 — f8925-8959 (371.917-373.333 s, 35 frames, 1.46 s) — shot SH077 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0286.jpg; entry EP0286, exit EP0287; second review: MINOR
- **Objects/placement (OBSERVED):** Builder at left (x~0.20-0.31), pink LOAN document in the middle (x~0.46-0.60,y~0.26-0.60) with red title, hooded buyer at right (x~0.73-0.88).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** handwritten red caps ~7%
- **Readable text:** LOAN
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.910 #e2cbc6:0.045 #0b0807:0.024 #918d86:0.013 #74403d:0.008
- **Hierarchy:** Doc at centre.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Dollar sign swapped for LOAN doc via EP0286; hard replace out via EP0287 profile card.
- **Narration (ASR, unverified):** Sometimes it's the loan.
- **Story function (INFERRED):** INFERRED: 'Sometimes it's the loan'.
- **Continuity:** S0151 loan doc.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0213 — f8988-9035 (374.542-376.500 s, 48 frames, 2.00 s) — shot SH078 (inferred) — F4 full-bleed screenshot
- **Evidence:** frames/ep_stable/e0287.jpg; entry EP0287, exit EP0288; second review: OK
- **Objects/placement (OBSERVED):** Profile card (x~0.15-0.85,y~0.10-1.0, cropped at bottom): big wordmark at top, round portrait at left, name, role, buttons, About text, light grey surround.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** card screenshot
- **Typography:** UI sans; wordmark bold blue
- **Readable text:** Stuart Miller; Executive Chairman, Chief Executive Officer and President at Lennar; About
- **Unreadable/uncertain text:** About paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.783 #ededeb:0.145 #a29697:0.027 #1663a1:0.025 #5c4a48:0.020
- **Hierarchy:** Wordmark and portrait.
- **Camera/motion:** SCROLL/rise at start; **entry/exit:** Rises via EP0287 (28f); hard replace out via EP0288.
- **Narration (ASR, unverified):** call, the Lenar CEO said,
- **Story function (INFERRED):** INFERRED: CEO call quote.
- **Continuity:** Same card as S0175.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0214 — f9036-9258 (376.542-385.792 s, 223 frames, 9.29 s) — shot SH079 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0288.jpg; entry EP0288, exit EP0289; second review: OK
- **Objects/placement (OBSERVED):** Dark transcript capture at top-left (x~0.06-0.61,y~0.08-0.55) with a yellow highlight at start of text; bespectacled figure at laptop (head x~0.54-0.69,y~0.49-0.76) on brown desk (x~0.54-0.97,y~0.80-1.0), laptop screen with a letter mark.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** UI capture + marker figure; desk brown
- **Typography:** small light text; laptop mark bold
- **Readable text:** Stuart Miller; 0:04:08; 'Fewer families can afford to both produce a down payment and qualify for a mortgage...'
- **Unreadable/uncertain text:** rest of quote
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.621 #121618:0.234 #7d7571:0.078 #dbc8b8:0.035 #425651:0.032
- **Hierarchy:** Quote then figure.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0288; hard replace out via EP0289.
- **Narration (ASR, unverified):** fewer families can afford to produce a down payment and qualify for a mortgage, as in many of our markets, almost 50 % of our visitors cannot immediately qualify. In
- **Story function (INFERRED):** INFERRED: CEO quote on affordability.
- **Continuity:** Capture type S0176.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0215 — f9259-9299 (385.833-387.500 s, 41 frames, 1.71 s) — shot SH080 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0289.jpg; entry EP0289, exit EP0291; second review: MINOR
- **Objects/placement (OBSERVED):** Blue wordmark at upper centre (x~0.30-0.71,y~0.17-0.26); blank below.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** logo
- **Typography:** bold blue caps ~6%
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.978 #0e5f9f:0.014 #e3fafe:0.004 #9ec5df:0.002 #5788ad:0.002
- **Hierarchy:** Logo.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Hard replace in via EP0289; figure appears via EP0290.
- **Narration (ASR, unverified):** In many of Lenar's markets, about
- **Story function (INFERRED):** INFERRED: 'In many of the builder's markets'.
- **Continuity:** Logo reused through S0218.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0072 (ADDITIVE_ENTRY, f9296) A first small standing figure (brown skin, blue tie, waving) appears centre.

## S0216 — f9300-9307 (387.542-387.833 s, 8 frames, 0.33 s) — shot SH080 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0291.jpg; entry EP0291, exit EP0292; second review: OK
- **Objects/placement (OBSERVED):** Wordmark top centre; one small figure with brown skin, dark hair, blue tie, waving arm (x~0.47-0.57,y~0.42-0.88) plus second figure (grey bob, closed-eye smile, purple tie; x~0.63-0.77) appears at the end. 0.33 s.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; flat skin tones
- **Typography:** bold blue caps
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.944 #6a625c:0.016 #16619f:0.016 #0b090a:0.015 #b6bbc6:0.009
- **Hierarchy:** Figures.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Figure via EP0290; second via EP0291.
- **Narration (ASR, unverified):** about half
- **Story function (INFERRED):** INFERRED: visitors of sales office.
- **Continuity:** S0217 adds third.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0217 — f9308-9358 (387.875-389.958 s, 51 frames, 2.12 s) — shot SH080 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0292.jpg; entry EP0292, exit EP0295; second review: OK
- **Objects/placement (OBSERVED):** Wordmark top centre; three figures at x~0.46-0.91,y~0.40-0.86: brown-skin blue-tie waver, grey-bob purple tie, curly-brown-hair figure with a worried face.
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline
- **Typography:** bold blue caps
- **Readable text:** LENNAR
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.922 #6e5d54:0.027 #0c0809:0.022 #17619f:0.016 #bab8bd:0.012
- **Hierarchy:** Trio.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Third figure via EP0292; hat figures via EP0293/EP0294 then exit; hard replace later via EP0296 outside shard.
- **Narration (ASR, unverified):** half the people walking into the sales office can't
- **Story function (INFERRED):** INFERRED: potential buyers (ASR: half the visitors cannot qualify).
- **Continuity:** S0216 plus one, then S0218.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.
- **Intra-state events:** EVI0073 (ADDITIVE_ENTRY, f9317) A small figure with a brown hat appears at far left of the trio.; EVI0074 (ADDITIVE_ENTRY, f9331) Another figure with a reddish headband hat appears further left.

## S0218 — f9359-9398 (390.000-391.625 s, 40 frames, 1.67 s) — shot SH080 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0295.jpg; entry EP0295, exit EP0296; second review: OK
- **Objects/placement (OBSERVED):** Wordmark top centre (x~0.30-0.71,y~0.17-0.26); red handwritten word at left (x~0.18-0.27,y~0.53-0.61); trio at x~0.46-0.91,y~0.39-0.88 (hands folded in the middle figure).
- **Background:** flat white/off-white canvas (~#FCFCFC), no texture
- **Illustration:** marker outline; red lettering
- **Typography:** handwritten red ~4% height
- **Readable text:** Nope
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #725a53:0.029 #0c0809:0.022 #17619f:0.016 #bcb6bc:0.013
- **Hierarchy:** Red word at left reads as an answer; trio right.
- **Camera/motion:** STATIC 2D (no camera move inside the state); **entry/exit:** Word replaces two left figures via EP0295; hard replace out via EP0296 (next shard).
- **Narration (ASR, unverified):** can't qualify for a mortgage,
- **Story function (INFERRED):** INFERRED: 'can't qualify for a mortgage'.
- **Continuity:** S0217 variant.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions, colours, readable text. INFERRED: narrative role from unverified ASR.

## S0219 — f9399-9450 (391.667-393.792 s, 52 frames, 2.17 s) — shot SH081 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0296.jpg; entry EP0296, exit EP0297; second review: MINOR
- **Objects/placement (OBSERVED):** Pale-blue definition card at x0.23-0.77 y0.12-0.80 (title top-left, falling-arrow-and-percent icon with a small house at left, definition paragraph at right, source mark bottom); worried presenter head x0.0-0.22 y0.10-0.60 with a shoulder line leaving the frame at left.
- **Background:** flat off-white whiteboard canvas with a cut-in rectangle in light cornflower blue
- **Illustration:** Presenter drawn in thick black marker outline, beige skin, scruffy curly black hair, furrowed brow and small frown; card is a clean vector-style graphic image, not hand drawn.
- **Typography:** Card title sans bold about 4% of frame height, black on blue; body sans about 2.2% height left aligned.
- **Readable text:** Buydown; [bi-'daun] (pronunciation); A mortgage financing technique where the buyer tries to get a lower interest rate for at least the mortgage's first few years and possibly for its lifetime.; Investopedia (source mark at card bottom)
- **Unreadable/uncertain text:** Tiny coin and note icons inside the card illustration.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.604 #8eb7f5:0.309 #f2d1b6:0.037 #3c5378:0.028 #070c1a:0.021
- **Hierarchy:** Eye goes to the blue card (colour mass) then the peeking worried face reacting to it at left.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace at EP0296; exits by hard replace at EP0297.
- **Narration (ASR, unverified):** even with all those incentives on the table.
- **Story function (INFERRED):** INFERRED: shows the term for the incentive being discussed (ASR: incentives on the table) as a dictionary-like source plate with a reacting presenter.
- **Continuity:** Card is a third-party graphic; presenter peek-in reused in other reaction beats such as S0224.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0220 — f9451-9467 (393.833-394.500 s, 17 frames, 0.71 s) — shot SH082 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0297.jpg; entry EP0297, exit EP0298; second review: OK
- **Objects/placement (OBSERVED):** Red outlined block lettering reading PRICES at x0.22-0.62 y0.41-0.66; vertical kitchen knife with brown handle at x0.66-0.87 y0.07-0.65.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Marker-style bold red letters with black outline and slight wobble; knife with grey steel blade and dark brown handle, black outline, flat fill.
- **Typography:** Display hand-lettered caps, about 18% of frame height, red fill with black outline.
- **Readable text:** PRICES
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.906 #0c0303:0.043 #c60921:0.023 #cfcfcf:0.015 #573231:0.013
- **Hierarchy:** Lettering is largest and reddest, knife poised above it second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace from EP0297; exit at EP0298 when the knife swings.
- **Narration (ASR, unverified):** A price cut can't
- **Story function (INFERRED):** INFERRED: sets up a price-cut metaphor (ASR: a price cut can't) with a knife about to cut the word.
- **Continuity:** Same lettering and knife continue in S0221; knife returns at S0226.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0221 — f9468-9498 (394.542-395.792 s, 31 frames, 1.29 s) — shot SH082 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0298.jpg; entry EP0298, exit EP0299; second review: MINOR
- **Objects/placement (OBSERVED):** PRICES lettering x0.16-0.64 y0.40-0.66 sliced by a white gap near x0.27 (PRI | ES); knife lying nearly horizontal x0.52-0.87 y0.52-0.80 with blade pointing left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Same marker lettering with a clean diagonal-ish white cut; knife redrawn at slicing angle.
- **Typography:** Display red caps with black outline, same size as S0220.
- **Readable text:** PRIC ES (the word PRICES split by a white diagonal gap, a fragment of the C visible on the right piece)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.905 #0d0303:0.043 #c30a22:0.024 #cfcfcf:0.015 #573635:0.013
- **Hierarchy:** Cut gap in the word draws the eye first, knife second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0298 (single-frame swap of knife and text); exit EP0299 hard replace.
- **Narration (ASR, unverified):** can't fix that.
- **Story function (INFERRED):** INFERRED: visual punchline for 'can't fix that' - the cut is shown literally.
- **Continuity:** Continues S0220 composition.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0222 — f9499-9547 (395.833-397.833 s, 49 frames, 2.04 s) — shot SH083 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0299.jpg; entry EP0299, exit EP0302; second review: MINOR
- **Objects/placement (OBSERVED):** Blue LENNAR wordmark at x0.17-0.58 y0.15-0.23; small pink two-storey house with green bushes x0.27-0.46 y0.40-0.75 below it; a yellow price tag with a red dollar sign tied to the house's left side x0.14-0.27 y0.55-0.77 which is absent in the first frame and appears later in the state.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** House: terracotta-pink fill with grey roof, black outline, rounded green shrubs; tag yellow rhombus with red scribbled dollar sign and a thin string.
- **Typography:** Wordmark is a bold geometric sans in solid blue, about 4.5% height, wide letterspacing.
- **Readable text:** LENNAR (blue wordmark)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.943 #c7a9ad:0.017 #13619e:0.015 #090605:0.013 #61584c:0.012
- **Hierarchy:** Wordmark first by colour, then the house with the tag.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0299; micro events EP0300 (tag appears) and EP0301 (tag text goes single dollar); exits EP0302 additive.
- **Narration (ASR, unverified):** Knock another 10 ,000 off the house,
- **Story function (INFERRED):** INFERRED: identifies the homebuilder and illustrates its price cut with a tagged house (ASR: knock another 10,000 off the house).
- **Continuity:** Same house and wordmark in S0223; wordmark returns S0226.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0075 (ADDITIVE_ENTRY, f9516) A yellow price tag with red dollar signs, tied by a string, appears on the left of the pink house.; EVI0076 (NUMBER_OR_LABEL_CHANGE, f9534) Text on the yellow tag shrinks from a triple-dollar mark to a single red dollar sign; tag outline unchanged.

## S0223 — f9548-9630 (397.875-401.292 s, 83 frames, 3.46 s) — shot SH083 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0302.jpg; entry EP0302, exit EP0304; second review: MINOR
- **Objects/placement (OBSERVED):** Wordmark x0.17-0.58 y0.15-0.23; pink house with yellow tag x0.18-0.46 y0.40-0.75; worried character with red headband x0.66-0.83 y0.38-1.0 cropped by bottom edge; tiny red caption left of its head x0.57-0.65 y0.52-0.58.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Character head larger than torso, two dot eyes and a downturned mouth, brown spiky hair, red headband; thin black stick body.
- **Typography:** Wordmark bold sans blue; tiny red handwritten caption under 1.5% height.
- **Readable text:** LENNAR (blue wordmark)
- **Unreadable/uncertain text:** Tiny red caption beside the worried character (looks like 'still too broke').
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.885 #d5be81:0.038 #0d0907:0.033 #836754:0.029 #16639e:0.015
- **Hierarchy:** Left half wordmark and house; right half the worried character reacting.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0302 (character enters); micro EP0303 caption; exit EP0304.
- **Narration (ASR, unverified):** and the buyer who can't qualify still can't qualify.
- **Story function (INFERRED):** INFERRED: shows the buyer who still cannot afford it after a cut (ASR: the buyer who can't qualify still can't qualify).
- **Continuity:** Same house/tag as S0222; character is new.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0077 (ADDITIVE_ENTRY, f9589) A tiny red handwritten caption (looks like 'still too broke') appears just left of the worried character's head.

## S0224 — f9631-9658 (401.333-402.458 s, 28 frames, 1.17 s) — shot SH084 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0304.jpg; entry EP0304, exit EP0305; second review: OK
- **Objects/placement (OBSERVED):** Huge black-haired character x0.55-0.94 y0.0-1.0 (head about 0.3w); green dollar bill held at x0.39-0.56 y0.56-0.88.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Thick black outline, flat beige skin, solid black hair mass, worried eyebrows and tiny dot eyes; bill is green with yellow dollar mark in a grey circle.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.762 #22211f:0.087 #020201:0.068 #d8ccaf:0.059 #7ba06d:0.024
- **Hierarchy:** Giant face first, bill second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0304; additive bubble EP0305 ends the state.
- **Narration (ASR, unverified):** And when price cuts stop bringing
- **Story function (INFERRED):** INFERRED: reaction beat as the buyer weighs a tiny budget (ASR: when price cuts stop bringing...).
- **Continuity:** Same character continues in S0225.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0225 — f9659-9685 (402.500-403.583 s, 27 frames, 1.12 s) — shot SH084 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0305.jpg; entry EP0305, exit EP0306; second review: OK
- **Objects/placement (OBSERVED):** Close-up character x0.56-0.92 y0.05-1.0; speech bubble x0.16-0.55 y0.20-0.54 with two lines of handwriting; green bill x0.38-0.55 y0.55-0.90.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Bubble has a thick black outline with a pointed tail toward the character; handwritten black marker.
- **Typography:** Handwritten marker, about 4% height, black, centre aligned in bubble.
- **Readable text:** What can I get for $2?
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.738 #232220:0.090 #020202:0.083 #d7cbb0:0.062 #7a9c6e:0.026
- **Hierarchy:** Text bubble pulls the eye first, then the face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive entry EP0305; hard replace exit EP0306.
- **Narration (ASR, unverified):** stop bringing in buyers,
- **Story function (INFERRED):** INFERRED: dramatises small buying power; the quoted joke is not in the ASR.
- **Continuity:** Continues S0224.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0226 — f9686-9715 (403.625-404.833 s, 30 frames, 1.25 s) — shot SH085 (inferred) — F7 text card
- **Evidence:** frames/ep_stable/e0306.jpg; entry EP0306, exit EP0308; second review: MINOR
- **Objects/placement (OBSERVED):** Large blue wordmark spanning x0.17-0.82 y0.41-0.55; small knife attached at its right end x0.83-0.91 y0.38-0.55.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Wordmark flat blue; knife small, grey blade, brown handle, outline black.
- **Typography:** Heavy geometric sans, about 7% of frame height, blue, wide tracking.
- **Readable text:** LENNAR (blue wordmark)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.949 #0b5fa2:0.039 #5b87a9:0.005 #c2d7e4:0.004 #1b1816:0.003
- **Hierarchy:** Wordmark dominates; knife tiny as accent.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0306; EP0307 knife flies away inside the state; exit EP0308.
- **Narration (ASR, unverified):** builders stop cutting.
- **Story function (INFERRED):** INFERRED: 'builders stop cutting' - the knife leaves the company name.
- **Continuity:** Same wordmark as S0222 scaled up.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state motion intervals:** EP0307

## S0227 — f9716-9770 (404.875-407.125 s, 55 frames, 2.29 s) — shot SH086 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0308.jpg; entry EP0308, exit EP0309; second review: MINOR
- **Objects/placement (OBSERVED):** Scatter spanning x0.10-0.89 y0.12-0.82: three small cream houses with red roofs (left, upper centre, lower right), three grey apartment blocks, and three red FOR SALE! signs on brown posts beside the blocks.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Houses cream fill red roof, blocks grey with white windows, signs red with white caps text and brown posts; all black outlined.
- **Typography:** Sign text small sans caps white on red, about 2% height.
- **Readable text:** FOR SALE! (on three red signs)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfb:0.878 #848e8d:0.039 #100a09:0.039 #4b4d4c:0.028 #b42e30:0.017
- **Hierarchy:** Red signs pop; clustered houses read as inventory.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0308; hard replace exit EP0309.
- **Narration (ASR, unverified):** While they still have to sell the homes they've already built,
- **Story function (INFERRED):** INFERRED: unsold built-homes inventory (ASR: homes they've already built).
- **Continuity:** Houses echo S0233 icon set.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0228 — f9771-9796 (407.167-408.208 s, 26 frames, 1.08 s) — shot SH087 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0309.jpg; entry EP0309, exit EP0310; second review: OK
- **Objects/placement (OBSERVED):** Left builder with saw x0.23-0.44 y0.22-0.78; stack of three orange bricks x0.45-0.58 y0.55-0.80; right blonde builder with hammer x0.65-0.79 y0.33-0.80.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Stick bodies with black lines, round heads with small smile; bricks terracotta with black outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #0c0706:0.036 #d48c5c:0.029 #cabaac:0.008 #685a54:0.008
- **Hierarchy:** Two figures balanced either side of the brick stack.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0309; red X added at EP0310.
- **Narration (ASR, unverified):** they no longer have to keep building
- **Story function (INFERRED):** INFERRED: builders actively building; will be negated (ASR: no longer have to keep building).
- **Continuity:** Same drawing continues in S0229 under a red X.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0229 — f9797-9827 (408.250-409.500 s, 31 frames, 1.29 s) — shot SH087 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0310.jpg; entry EP0310, exit EP0311; second review: MINOR
- **Objects/placement (OBSERVED):** Builders and bricks as S0228 with a thick crimson X spanning x0.21-0.77 y0.15-0.90 over all three subjects.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Marker X in crimson with slightly uneven stroke, painted over the scene.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.872 #b72032:0.050 #100a09:0.035 #c98961:0.033 #d8bab2:0.010
- **Hierarchy:** The X is the dominant red mark; the scene beneath is secondary.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive entry EP0310; exit EP0311 transition.
- **Narration (ASR, unverified):** building the next ones.
- **Story function (INFERRED):** INFERRED: negation of building (ASR: building the next ones).
- **Continuity:** Layer on top of S0228.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0230 — f9844-9906 (410.208-412.792 s, 63 frames, 2.62 s) — shot SH088 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0311.jpg; entry EP0311, exit EP0312; second review: OK
- **Objects/placement (OBSERVED):** Light news-article screenshot x0.06-0.59 y0.05-0.95 (masthead top, small grey portrait at upper left, name heading, paragraphs, red Subscribe button at top right); bow-tie character with dark hair x0.67-0.99 y0.35-1.0.
- **Background:** flat off-white whiteboard canvas with white article page
- **Illustration:** Screenshot photographic grey portrait; character: small head, dot eyes, worried brow, dark hair, red bow tie, black stick body.
- **Typography:** Masthead sans bold black with red subscribe chip; headline name about 2.4% height; body serif/sans tiny.
- **Readable text:** Paul Romanowski (heading); masthead 'THE REAL DEAL'
- **Unreadable/uncertain text:** Article body paragraphs about a homebuilder and housing market; small red Subscribe button.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.851 #d2d1d1:0.048 #14100e:0.044 #a89b94:0.043 #725252:0.013
- **Hierarchy:** Name and portrait first, then the character reacting at right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Transition EP0311 (page slides up) then hold; hard replace exit EP0312.
- **Narration (ASR, unverified):** Horton CEO Paul Romanowski said, we
- **Story function (INFERRED):** INFERRED: introduces the executive being quoted (ASR: Horton CEO ... said).
- **Continuity:** Reaction character resembles S0231 presenter family but different skin/outfit.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0231 — f9907-10001 (412.833-416.750 s, 95 frames, 3.96 s) — shot SH088 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0312.jpg; entry EP0312, exit EP0314; second review: OK
- **Objects/placement (OBSERVED):** Dark PDF viewer x0.05-0.82 y0.0-1.0 (thumbnail strip left, white page centre with a yellow highlighted phrase); presenter x0.76-0.93 y0.40-1.0 with a diagonal pointer stick to the page.
- **Background:** flat off-white whiteboard canvas with a dark UI screenshot occupying the left 0.82
- **Illustration:** UI screenshot is real; presenter uses thick black outline, beige skin, flat frown dash mouth.
- **Typography:** Document body serif small about 1.2% height, black on white; toolbar tiny white on grey.
- **Readable text:** Title bar text partially: 'Q3 2026 - Earnings Call Trans...'
- **Unreadable/uncertain text:** Body of earnings call transcript, speaker lines; highlight text reads approximately 'We did make' (small).
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.593 #292a29:0.281 #c7c7c7:0.053 #91908f:0.040 #f5d3b5:0.035
- **Hierarchy:** Page centre is brightest and yellow highlight draws focus, presenter and pointer second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0312; micro highlight EP0313; hard replace exit EP0314.
- **Narration (ASR, unverified):** we did make the decision to hold margin a little more than push into the units.
- **Story function (INFERRED):** INFERRED: source evidence for the quote (ASR: we did make the decision to hold margin).
- **Continuity:** Related quote cards in S0235-S0238.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0078 (HIGHLIGHT_ADD, f9922) Tiny yellow highlight mark appears on a phrase of PDF body text slightly above page centre.; EVI0079 (HIGHLIGHT_ADD, f9927) Yellow highlight and two small red marks extend on a transcript sentence at centre-right (x~0.41-0.69,y~0.39-0.49); mouse arrow near top; EVI0080 (HIGHLIGHT_ADD, f9944) Red tick marks and yellow highlight extension on the same transcript sentence; text-insertion cursor present; EVI0081 (HIGHLIGHT_ADD, f9959) Small red mark appears at the left end of the highlighted phrase 'more than push' (x~0.39-0.43,y~0.55-0.60); EVI0082 (HIGHLIGHT_ADD, f9969) Yellow highlight extends along the phrase 'more than push' with small red marks at its left end; EVI0083 (HIGHLIGHT_ADD, f9981) Yellow highlight extends over 'more than push into the units' and a mouse arrow appears over the text

## S0232 — f10002-10029 (416.792-417.917 s, 28 frames, 1.17 s) — shot SH089 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0314.jpg; entry EP0314, exit EP0315; second review: OK
- **Objects/placement (OBSERVED):** Giant smiling head x0.34-0.65 y0.03-0.68; open dictionary book x0.38-0.62 y0.62-1.0 with a small flag at its lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Thick black outline, peach skin, closed-eye smile, spiky black hair; open book beige pages with light brown cover.
- **Typography:** Tiny handwritten word on book cover (rotated).
- **Readable text:** DICTIONARY (on book spine)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.788 #f4d3b6:0.126 #060403:0.048 #dbb990:0.030 #63514c:0.008
- **Hierarchy:** Giant face first; book at bottom second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0314; hard replace exit EP0315.
- **Narration (ASR, unverified):** The translation here,
- **Story function (INFERRED):** INFERRED: 'The translation here' - a dictionary prop sets up a plain-language translation of the quote.
- **Continuity:** Face style matches S0233/S0234 presenter.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0233 — f10030-10076 (417.958-419.875 s, 47 frames, 1.96 s) — shot SH090 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0315.jpg; entry EP0315, exit EP0317; second review: OK
- **Objects/placement (OBSERVED):** Pink house x0.11-0.26 y0.30-0.56; cream tower with grey annex x0.30-0.46 y0.18-0.60; small cream house x0.62-0.72 y0.47-0.62 (red sign appears mid-state); grey apartment block x0.74-0.88 y0.25-0.65.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Doodle buildings with black outlines, muted fills, green shrubs on pink house.
- **Typography:** Tiny sign text under 1% height.
- **Readable text:** none
- **Unreadable/uncertain text:** Small red sign lettering (likely SOLD).
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.894 #080807:0.032 #55524c:0.027 #d7c9bf:0.025 #8e9690:0.021
- **Hierarchy:** Left pair and right pair are balanced; sign adds a red accent.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0315; micro EP0316 sign appears; additive EP0317 exit.
- **Narration (ASR, unverified):** he'd rather sell fewer houses than cut prices
- **Story function (INFERRED):** INFERRED: fewer houses sold rather than price cuts (ASR: he'd rather sell fewer houses).
- **Continuity:** Same house icons reused under the knife character in S0234.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0084 (ADDITIVE_ENTRY, f10053) A small red sign (SOLD) appears on the front of the small cream house at right-centre.

## S0234 — f10077-10110 (419.917-421.292 s, 34 frames, 1.42 s) — shot SH090 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0317.jpg; entry EP0317, exit EP0318; second review: MINOR
- **Objects/placement (OBSERVED):** Knife-wielding smiling character x0.19-0.52 y0.15-1.0 in front of the pink house and tower (x0.12-0.30, partly hidden); small cream house with red sign x0.62-0.72 y0.47-0.65; grey block x0.74-0.88 y0.35-0.65.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Character thick black line with knife grey blade; buildings behind partly hidden.
- **Typography:** none
- **Readable text:** SOLD (red sign on the small cream house)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.830 #efd1b8:0.080 #080605:0.047 #584946:0.025 #878f8d:0.017
- **Hierarchy:** Character with knife dominates left; buildings secondary.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive entry EP0317; hard replace exit EP0318.
- **Narration (ASR, unverified):** cut prices any further.
- **Story function (INFERRED):** INFERRED: 'cut prices any further' - the knife character is the price-cutter.
- **Continuity:** Same building set as S0233.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0235 — f10111-10177 (421.333-424.083 s, 67 frames, 2.79 s) — shot SH091 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0318.jpg; entry EP0318, exit EP0319; second review: OK
- **Objects/placement (OBSERVED):** Dark transcript card x0.07-0.69 y0.06-0.53 (speaker name and title top-left, timestamp top-right, five-line paragraph with one yellow phrase); rest of frame blank white.
- **Background:** flat off-white whiteboard canvas with a near-black rounded card
- **Illustration:** UI capture, rounded corners, white body text on dark.
- **Typography:** UI sans, about 1.5% height body white, yellow phrase.
- **Readable text:** Header name 'Stuart Miller' with title line and timestamp '0:09:34'
- **Unreadable/uncertain text:** Paragraph of transcript; yellow highlighted phrase begins 'means we are compromising margin...'.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfdfd:0.722 #13171a:0.216 #a8abae:0.024 #6d7072:0.021 #424648:0.017
- **Hierarchy:** Yellow phrase is the focal point on the dark card.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0318; additive EP0319 at end.
- **Narration (ASR, unverified):** So the one seller that has to sell is already cutting,
- **Story function (INFERRED):** INFERRED: second executive quote showing the same stance (ASR: one seller that has to sell is already cutting).
- **Continuity:** Same card reused in S0236-S0238.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0236 — f10178-10235 (424.125-426.500 s, 58 frames, 2.42 s) — shot SH091 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0319.jpg; entry EP0319, exit EP0320; second review: MINOR
- **Objects/placement (OBSERVED):** Dark transcript card x0.07-0.69 y0.06-0.53; light-theme excerpt text block x0.33-0.93 y0.63-0.85 with a yellow highlighted phrase.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Dark card plus plain black text on white.
- **Typography:** UI sans small; excerpt serif/sans about 1.3% height black with yellow highlight.
- **Readable text:** Speaker 'Stuart Miller' in header
- **Unreadable/uncertain text:** Excerpt text begins 'on what we see quarter to quarter...' and highlight 'We did make'.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.682 #13181a:0.220 #5a5c59:0.036 #bdbeba:0.031 #8e8f89:0.031
- **Hierarchy:** Two separate text sources contrast dark vs light.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0319; additive EP0320 at the end.
- **Narration (ASR, unverified):** and the biggest of them is starting to hit its limit.
- **Story function (INFERRED):** INFERRED: pairs the two quotes side by side.
- **Continuity:** Excerpt repeated in S0237.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0237 — f10236-10261 (426.542-427.583 s, 26 frames, 1.08 s) — shot SH091 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0320.jpg; entry EP0320, exit EP0321; second review: OK
- **Objects/placement (OBSERVED):** Dark card x0.07-0.69 y0.06-0.53; excerpt block x0.33-0.93 y0.63-0.85; smiling presenter x0.12-0.30 y0.42-1.0 overlapping the card's lower left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Character thick line, peach, smile, spiky hair; arms bent.
- **Typography:** Same as S0236.
- **Readable text:** none
- **Unreadable/uncertain text:** Transcript body text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.635 #131719:0.223 #f2d396:0.053 #6b6a5d:0.048 #acaeae:0.041
- **Hierarchy:** Character's face first, then the yellow phrases.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0320; additive EP0321 exit.
- **Narration (ASR, unverified):** At the same time,
- **Story function (INFERRED):** INFERRED: presenter introduces both quotes ('at the same time').
- **Continuity:** Same cards in S0236/S0238.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0238 — f10262-10335 (427.625-430.667 s, 74 frames, 3.08 s) — shot SH091 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0321.jpg; entry EP0321, exit EP0322; second review: OK
- **Objects/placement (OBSERVED):** First dark card x0.07-0.69 y0.06-0.53; second dark card with search bar x0.36-0.93 y0.19-0.72 overlapping it; excerpt block x0.33-0.93 y0.63-0.85; presenter x0.12-0.30 y0.42-1.0.
- **Background:** flat off-white whiteboard canvas with overlapping dark UI cards
- **Illustration:** UI capture, second card has a purple logo bar and a green search button.
- **Typography:** UI sans body about 1.3% height; logo wordmark purple/white.
- **Readable text:** Search bar placeholder 'Search for news, tickers or companies'; card header 'Stuart Miller' with title
- **Unreadable/uncertain text:** Dense paragraph in the second card with a red underline; excerpt text below.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.470 #15191b:0.376 #d9c7b6:0.071 #6b736f:0.067 #e0c437:0.016
- **Hierarchy:** Newest card overlaying draws attention; presenter lower left is anchor.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0321; hard replace exit EP0322.
- **Narration (ASR, unverified):** fewer households qualify to borrow money to purchase a home.
- **Story function (INFERRED):** INFERRED: a further quote illustrating buyers priced out (ASR: fewer households qualify to borrow).
- **Continuity:** Cards continue from S0237.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0239 — f10336-10341 (430.708-430.917 s, 6 frames, 0.25 s) — shot SH092 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0322.jpg; entry EP0322, exit EP0323; second review: MINOR
- **Objects/placement (OBSERVED):** Single thoughtful character x0.43-0.60 y0.40-1.0 (head about 0.16w at y0.40-0.72, one arm raised to chin); rest of frame blank white.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Peach head, spiky black hair, slight frown; thin black body with one arm bent upward.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.955 #f2d2b7:0.032 #080403:0.010 #86807c:0.002 #3c352f:0.002
- **Hierarchy:** The single figure is the whole focus.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0322; additive EP0323 at the end.
- **Narration (ASR, unverified):** And when
- **Story function (INFERRED):** INFERRED: brief pause 'And when' before the debt list builds - very short state (6 frames = 0.25 s).
- **Continuity:** Character reused S0240-S0244.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0240 — f10342-10353 (430.958-431.417 s, 12 frames, 0.50 s) — shot SH092 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0323.jpg; entry EP0323, exit EP0324; second review: OK
- **Objects/placement (OBSERVED):** Left DEBT document x0.10-0.23 y0.40-0.74; thoughtful presenter x0.43-0.59 y0.40-1.0 (head about 0.16w), one hand raised to chin.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; furrowed brow, flat mouth. Document cream with grey border, red hand-lettered title, wavy scribble lines and a small chart arrow.
- **Typography:** Hand-lettered red caps for the document title, about 4% height.
- **Readable text:** DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.914 #f0cfb5:0.034 #e9e4db:0.029 #0c0807:0.017 #775d5c:0.006
- **Hierarchy:** Red title on the doc first, then the character's face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0323 (doc appears); exit EP0324 (second doc added).
- **Narration (ASR, unverified):** when Americans can't
- **Story function (INFERRED):** INFERRED: first of several debt documents building up (ASR: when Americans can't...). Very short state (0.5 s).
- **Continuity:** Same character and doc style across S0239-S0244.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0241 — f10354-10360 (431.458-431.708 s, 7 frames, 0.29 s) — shot SH092 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0324.jpg; entry EP0324, exit EP0325; second review: MINOR
- **Objects/placement (OBSERVED):** Left doc x0.10-0.23 y0.40-0.74; second doc x0.28-0.41 y0.10-0.44; presenter x0.43-0.59 y0.40-1.0.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; same worried look. Two cream documents with red titles.
- **Typography:** Hand-lettered red caps about 4% height on each doc.
- **Readable text:** DEBT (on both docs)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.872 #e9e4db:0.057 #edcdb5:0.036 #0b0806:0.024 #7a595a:0.010
- **Hierarchy:** Docs form a diagonal rising toward upper centre, leading to the face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0324; exit EP0325. 7 frames (0.29 s).
- **Narration (ASR, unverified):** can't
- **Story function (INFERRED):** INFERRED: a count-up of debt items under rapid narration ('can't').
- **Continuity:** Continues S0240.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0242 — f10361-10371 (431.750-432.167 s, 11 frames, 0.46 s) — shot SH092 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0325.jpg; entry EP0325, exit EP0326; second review: MINOR
- **Objects/placement (OBSERVED):** Docs at left x0.10-0.23 y0.40-0.74, upper centre-left x0.28-0.40 y0.10-0.44, upper right x0.61-0.74 y0.12-0.46; presenter x0.43-0.59.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes. Three cream documents tilted slightly.
- **Typography:** Red hand-lettered caps about 4% height.
- **Readable text:** DEBT (on three docs)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.831 #e9e4db:0.086 #ebcbb5:0.039 #0b0807:0.031 #7c595a:0.013
- **Hierarchy:** Triangle of documents around the face; eye lands on the face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0325; exit EP0326. 11 frames (0.46 s).
- **Narration (ASR, unverified):** can't borrow enough,
- **Story function (INFERRED):** INFERRED: the pile of debt grows as the narrator lists 'can't borrow enough'.
- **Continuity:** Continues S0241.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0243 — f10372-10379 (432.208-432.500 s, 8 frames, 0.33 s) — shot SH092 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0326.jpg; entry EP0326, exit EP0327; second review: MINOR
- **Objects/placement (OBSERVED):** Four docs: left x0.11-0.23, upper-left x0.28-0.41, upper-right x0.61-0.74, lower right x0.77-0.90 y0.44-0.78; presenter x0.43-0.59 y0.40-1.0.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes. Four tilted cream documents.
- **Typography:** Red hand-lettered caps about 4% height.
- **Readable text:** DEBT (on four docs)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.791 #ebdfd2:0.147 #090605:0.036 #6e4749:0.014 #b09a98:0.011
- **Hierarchy:** Evenly spread documents frame the face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0326; exit EP0327. 8 frames (0.33 s).
- **Narration (ASR, unverified):** enough,
- **Story function (INFERRED):** INFERRED: completes the 'debt' set before the question 'who steps in?'.
- **Continuity:** Same four docs as S0244; two near-identical states differ only by presenter mood.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0244 — f10380-10406 (432.542-433.625 s, 27 frames, 1.12 s) — shot SH092 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0327.jpg; entry EP0327, exit EP0328; second review: MINOR
- **Objects/placement (OBSERVED):** Same four docs; presenter x0.43-0.60 y0.40-1.0 now smiling with arms out in a shrug.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; smile arc, both arms flung outward at the sides. Four tilted cream documents.
- **Typography:** Red hand-lettered caps about 4% height.
- **Readable text:** DEBT (four docs)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.790 #e9e4db:0.115 #e8c8b3:0.042 #0a0806:0.037 #7c5557:0.016
- **Hierarchy:** Face smile and open arms; documents second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0327 (pose swap); hard replace exit EP0328.
- **Narration (ASR, unverified):** who steps in?
- **Story function (INFERRED):** INFERRED: shrug as the narrator asks 'who steps in?'.
- **Continuity:** Same docs as S0243; only the pose differs.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0245 — f10407-10455 (433.667-435.667 s, 49 frames, 2.04 s) — shot SH093 (inferred) — F9 full-bleed drawn scene
- **Evidence:** frames/ep_stable/e0328.jpg; entry EP0328, exit EP0329; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed starry night scene; circular spotlight x0.62-0.93 y0.0-0.57 with a pale grey fill; diagonal translucent grey beam from the circle down-left to x0.15-0.55 at the bottom; single cream DEBT document inside the circle x0.72-0.82 y0.12-0.47.
- **Background:** Deep navy night sky with small white star dots
- **Illustration:** Flat vector scene: translucent grey beam, soft grey disc, dots for stars; document keeps the hand-drawn style.
- **Typography:** Red hand-lettered caps on the document, about 3.5% height.
- **Readable text:** DEBT (on the single document)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #1f273b:0.505 #5a6373:0.196 #212f49:0.169 #858b95:0.109 #dad7d5:0.022
- **Hierarchy:** The lit disc with the document at upper right; beam leads the eye there.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0328; hard replace exit EP0329.
- **Narration (ASR, unverified):** Who do you call when you need more debt? The
- **Story function (INFERRED):** INFERRED: spotlight on one remaining borrower ('Who do you call when you need more debt?').
- **Continuity:** Document reused from S0240-S0244.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0246 — f10456-10489 (435.708-437.083 s, 34 frames, 1.42 s) — shot SH094 (inferred) — F9 full-bleed drawn scene
- **Evidence:** frames/ep_stable/e0329.jpg; entry EP0329, exit EP0330; second review: OK
- **Objects/placement (OBSERVED):** Green country-map silhouette filling the frame; huge pixelated black sunglasses with white eyes at x0.15-0.69 y0.31-0.50; thick black curved arms below at x0.20-0.76 y0.55-0.85.
- **Background:** Full-bleed flat green map with white sea gaps and lakes
- **Illustration:** Marker-drawn map with black outlines; eyes white ovals with small black pupils; sunglasses in blocky 8-bit style.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #47a44f:0.767 #020502:0.113 #fcfcfc:0.105 #2e4f31:0.011 #a1a0a1:0.004
- **Hierarchy:** The sunglasses are the unmistakable focal point.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0329; hard replace exit EP0330.
- **Narration (ASR, unverified):** The United States government.
- **Story function (INFERRED):** INFERRED: personifies the country as the lender-of-last-resort with a 'cool' attitude (ASR: The United States government).
- **Continuity:** Map is the same eyed green silhouette seen in S0255, S0271.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0247 — f10490-10518 (437.125-438.292 s, 29 frames, 1.21 s) — shot SH095 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0330.jpg; entry EP0330, exit EP0331; second review: MINOR
- **Objects/placement (OBSERVED):** Single full-body stick presenter centred x0.41-0.59 y0.13-0.88 with a sweat drop at his right temple; arms folded at chest.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; closed-eye grin and small sweat drop; thin black stick limbs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.032 #070504:0.011 #92908a:0.002 #4c4643:0.002
- **Hierarchy:** One centred figure; sweat drop draws a micro focus.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0330; EP0331 transition exits.
- **Narration (ASR, unverified):** But before I get into that,
- **Story function (INFERRED):** INFERRED: slightly nervous pivot to the sponsor ('But before I get into that').
- **Continuity:** Same figure as S0239; used again S0257.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0248 — f10532-10553 (438.875-439.750 s, 22 frames, 0.92 s) — shot SH096 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0331.jpg; entry EP0331, exit EP0332; second review: OK
- **Objects/placement (OBSERVED):** Grey laptop with thick black bezel x0.13-0.88 y0.06-1.0 sitting on a brown desk; white video-player window x0.20-0.78 y0.17-0.75 with a tiny character in its centre x0.45-0.55 and a black play triangle over the character; red progress line at y0.77 x0.21-0.55 with a red dot.
- **Background:** White canvas with brown desk strip at the bottom corners
- **Illustration:** Flat vector laptop with grey bezels and black outlines; player white with black border; tiny stick character inside.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfbfb:0.640 #030303:0.151 #867872:0.131 #565655:0.071 #ac091a:0.007
- **Hierarchy:** Laptop frame, then the play triangle at centre.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0331 (13-frame animation); hard replace exit EP0332.
- **Narration (ASR, unverified):** a quick pause. I
- **Story function (INFERRED):** INFERRED: introduces a video-style pause (ASR: a quick pause).
- **Continuity:** Laptop reused S0284.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0249 — f10554-10559 (439.792-440.000 s, 6 frames, 0.25 s) — shot SH097 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0332.jpg; entry EP0332, exit EP0333; second review: MINOR
- **Objects/placement (OBSERVED):** Dark channel-page screenshot x0.33-0.95 y0.04-0.82 with city skyline banner and a handwritten Subscribe word, avatar, buttons, three thumbnail cards; presenter at left x0.04-0.32 y0.30-1.0 with grin and one hand lifted.
- **Background:** White canvas with a dark UI screenshot at right
- **Illustration:** Presenter thick outline, peach face with a closed-eye wide smile; screenshot is real UI with illustrated thumbnail art.
- **Typography:** Banner word is a handwritten display font about 7% height, white; UI sans tiny.
- **Readable text:** Subscribe (handwritten banner word); Casual Finance (channel name); thumbnail titles It's Just Starting., Nobody's Reacting., Nobody Can Stop It.
- **Unreadable/uncertain text:** Subscriber count, handle, button labels and video stats under thumbnails.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.556 #0d0d0d:0.231 #e1d3c3:0.105 #84877b:0.065 #4e4b43:0.043
- **Hierarchy:** Dark screenshot first by contrast, presenter smile second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0332; scroll motion EP0333 exits.
- **Narration (ASR, unverified):** I started
- **Story function (INFERRED):** INFERRED: self-promotion beat; ASR 'I started' (the host's own channel).
- **Continuity:** Same screenshot scrolls in S0250-S0251.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0250 — f10571-10583 (440.500-441.000 s, 13 frames, 0.54 s) — shot SH097 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0333.jpg; entry EP0333, exit EP0334; second review: MINOR
- **Objects/placement (OBSERVED):** Same dark screenshot after scroll x0.33-0.94 y0.04-0.82 now showing two rows of thumbnails; presenter at left x0.09-0.25 y0.30-1.0 with open-mouth grin.
- **Background:** White canvas with a dark UI screenshot
- **Illustration:** Presenter's grin widened with a pink open mouth; thumbnails are illustrated chart scenes.
- **Typography:** UI sans tiny; thumbnail titles in handwritten script.
- **Readable text:** Thumbnail titles partly legible: 'It's Just Starting.', 'Nobody's Reacting.', 'Nobody Can Stop It.'
- **Unreadable/uncertain text:** Subtitle stats under thumbnails.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.650 #0e0e0d:0.205 #ebd1bc:0.074 #64685a:0.040 #a49c99:0.031
- **Hierarchy:** Thumbnail grid and presenter's mouth.
- **Camera/motion:** STATIC 2D; **entry/exit:** After EP0333 scroll; exit EP0334 scroll.
- **Narration (ASR, unverified):** channel because I
- **Story function (INFERRED):** INFERRED: shows the channel's catalogue as credibility.
- **Continuity:** Same screenshot as S0249 mid-scroll.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0251 — f10593-10595 (441.417-441.500 s, 3 frames, 0.12 s) — shot SH097 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0334.jpg; entry EP0334, exit EP0335; second review: MINOR
- **Objects/placement (OBSERVED):** Dark thumbnail grid screenshot x0.33-0.93 y0.05-0.85 now three rows deep; presenter at left x0.09-0.26 y0.30-1.0 open-mouth smile. State lasts only 3 frames.
- **Background:** White canvas with a dark UI screenshot
- **Illustration:** As S0250.
- **Typography:** Thumbnail titles handwritten script; UI sans tiny.
- **Readable text:** Thumbnail titles such as 'Guess Who Paid.', 'History Is Repeating.'
- **Unreadable/uncertain text:** Remaining titles and view counts.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.671 #0e0d0d:0.179 #e9d1bc:0.075 #655653:0.039 #989b99:0.036
- **Hierarchy:** Grid first.
- **Camera/motion:** STATIC 2D; **entry/exit:** Follows scroll EP0334; hard replace exit EP0335.
- **Narration (ASR, unverified):** wanted business
- **Story function (INFERRED):** INFERRED: final frames of the scroll before the cut; animation tail only (0.125 s).
- **Continuity:** End of S0249-S0250 scroll.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0252 — f10596-10601 (441.542-441.750 s, 6 frames, 0.25 s) — shot SH098 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0335.jpg; entry EP0335, exit EP0336; second review: OK
- **Objects/placement (OBSERVED):** Reader x0.30-0.69 y0.29-1.0: large smiling head x0.40-0.59 y0.29-0.65 above an open newspaper marked NEWS at the bottom; sliver of yellow progress bar at bottom-left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; wide dot eyes, curved smile, beige newspaper with wavy text scribbles and NEWS lettering.
- **Typography:** Hand-lettered NEWS caps on the paper about 9% height, black/dark red outline.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.798 #ccc8a9:0.073 #f4d3b6:0.072 #080604:0.048 #666156:0.008
- **Hierarchy:** Face first, newspaper second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0335; additive EP0336.
- **Narration (ASR, unverified):** business
- **Story function (INFERRED):** INFERRED: introduces news-consumption pain (ASR: business and finance news).
- **Continuity:** Reader reused S0253-S0256.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0253 — f10602-10608 (441.792-442.042 s, 7 frames, 0.29 s) — shot SH098 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0336.jpg; entry EP0336, exit EP0337; second review: OK
- **Objects/placement (OBSERVED):** Reader as S0252 plus dark-brown briefcase with tan clasp at left x0.07-0.23 y0.37-0.60; yellow progress strip bottom-left about 2% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; briefcase flat brown with black outline.
- **Typography:** Newspaper lettering as S0252.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.767 #e5d1b4:0.128 #070402:0.052 #494135:0.032 #b4ae8e:0.021
- **Hierarchy:** Face first; briefcase small accent left.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0336; additive EP0337 at the end. 7 frames.
- **Narration (ASR, unverified):** business and finance
- **Story function (INFERRED):** INFERRED: 'business' signified by briefcase.
- **Continuity:** Continues S0252.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0254 — f10609-10628 (442.083-442.875 s, 20 frames, 0.83 s) — shot SH098 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0337.jpg; entry EP0337, exit EP0340; second review: OK
- **Objects/placement (OBSERVED):** Reader, briefcase left, plus framed line chart (red, green, blue zigzags with dotted baseline) at upper right x0.71-0.92 y0.06-0.38; yellow strip bottom-left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; chart in light-blue frame with black border.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfc:0.745 #e0ceb1:0.148 #060403:0.057 #4c3f35:0.035 #71a77d:0.015
- **Hierarchy:** Reader first; chart and briefcase balance either side.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0337; micro EP0338-0339 add bills; additive EP0340 exit.
- **Narration (ASR, unverified):** and finance news that
- **Story function (INFERRED):** INFERRED: 'finance news' signified by chart.
- **Continuity:** Chart prop reused S0255, S0266, S0271.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0085 (ADDITIVE_ENTRY, f10619) A small green dollar bill appears at right of the reader's head.; EVI0086 (ELEMENT_SWAP, f10624) Single small green bill is replaced by a larger pair of overlapping bills at right.

## S0255 — f10629-10661 (442.917-444.250 s, 33 frames, 1.38 s) — shot SH098 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0340.jpg; entry EP0340, exit EP0342; second review: OK
- **Objects/placement (OBSERVED):** Reader, briefcase left x0.07-0.23 y0.37-0.60, chart upper right x0.71-0.92 y0.06-0.38, green bills x0.74-0.91 y0.50-0.70, green eyed country-map doodle upper left x0.20-0.41 y0.06-0.31 (tiny house and block icons join at the end).
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; map doodle green with big white eyes.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfc:0.696 #dfceb0:0.152 #060603:0.062 #60a363:0.051 #494035:0.039
- **Hierarchy:** Reader central; four props orbit.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0340 (map), micro EP0341 (house/block icons), hard exit EP0342.
- **Narration (ASR, unverified):** that gave me the whole picture, but
- **Story function (INFERRED):** INFERRED: 'whole picture' - businesses, finance, housing, country in one orbit.
- **Continuity:** Same prop set returns in S0262 and S0271.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0087 (ADDITIVE_ENTRY, f10637) A tiny house and apartment-block icon pair appears just right of the map doodle at top.

## S0256 — f10662-10697 (444.292-445.750 s, 36 frames, 1.50 s) — shot SH098 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0342.jpg; entry EP0342, exit EP0343; second review: MINOR
- **Objects/placement (OBSERVED):** Reader at bottom centre with a frowning face x0.37-0.63 y0.20-0.60 and NEWS paper below; all props gone.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; downturned mouth, flat brows.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.797 #cdc8a8:0.074 #f4d3b6:0.073 #080604:0.048 #676155:0.008
- **Hierarchy:** One figure; sad mouth is the cue.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard exit EP0342 (props out, frown) and EP0343 replace.
- **Narration (ASR, unverified):** but I couldn't find it anywhere.
- **Story function (INFERRED):** INFERRED: frustration ('I couldn't find it anywhere').
- **Continuity:** Same reader as S0252 with a mood change.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0257 — f10698-10713 (445.792-446.417 s, 16 frames, 0.67 s) — shot SH098 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0343.jpg; entry EP0343, exit EP0345; second review: MINOR
- **Objects/placement (OBSERVED):** Small full-body presenter x0.42-0.58 y0.13-0.85 with a smile and hands on hips.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; open smile, arms bent at sides, thin legs apart.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.951 #f2d2b6:0.033 #090706:0.012 #726c68:0.003 #f6f11d:0.001
- **Hierarchy:** Lone figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0343; hard replace EP0345. 16 frames.
- **Narration (ASR, unverified):** Instead,
- **Story function (INFERRED):** INFERRED: transition 'Instead,'.
- **Continuity:** Same body as S0247.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0088 (POSE_SWAP, f10704) Only a thin arm or hand line near the character's right side changes slightly; no other element differs.

## S0258 — f10714-10734 (446.458-447.292 s, 21 frames, 0.88 s) — shot SH099 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0345.jpg; entry EP0345, exit EP0346; second review: OK
- **Objects/placement (OBSERVED):** Large head in a checkered detective cap x0.18-0.47 y0.09-0.69 at upper left, magnifying glass x0.34-0.49 y0.70-0.93 at lower centre, thin body line toward lower left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes plus brown-tan checked deerstalker cap; round magnifier with grey frame and blue lens.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.844 #f2d2b3:0.094 #050303:0.036 #766d5a:0.017 #363330:0.009
- **Hierarchy:** Cap and face first, magnifier second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0345; hard replace EP0346.
- **Narration (ASR, unverified):** what I found was biased
- **Story function (INFERRED):** INFERRED: investigative framing ('what I found was biased').
- **Continuity:** Detective returns S0282-S0283.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0259 — f10735-10743 (447.333-447.667 s, 9 frames, 0.38 s) — shot SH100 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0346.jpg; entry EP0346, exit EP0347; second review: OK
- **Objects/placement (OBSERVED):** Host x0.10-0.30 y0.12-0.55 head, body to bottom; microphone x0.30-0.35; two small arms-crossed characters at upper right x0.66-0.76 and x0.81-0.91 y0.12-0.65, one with blue tie, one with red tie.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Host: brown hair, open smile, brown-tan skin; the pair: stern brows, arms crossed, blue and red neckties.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.872 #080606:0.054 #d7c2a7:0.037 #83634e:0.024 #ab9a89:0.012
- **Hierarchy:** Host first, the opposing pair second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0346; additive EP0347.
- **Narration (ASR, unverified):** biased coverage,
- **Story function (INFERRED):** INFERRED: partisan messengers ('biased coverage').
- **Continuity:** Same trio in S0260.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0260 — f10744-10759 (447.708-448.333 s, 16 frames, 0.67 s) — shot SH100 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0347.jpg; entry EP0347, exit EP0348; second review: OK
- **Objects/placement (OBSERVED):** Same trio plus speech bubble x0.34-0.57 y0.09-0.44 with red handwriting; host x0.09-0.30; pair x0.66-0.91.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** As S0259; bubble has thick black outline and a tail to the host.
- **Typography:** Handwritten red marker, about 4.5% height, centre aligned.
- **Readable text:** So you should vote for...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.855 #080606:0.062 #d7bfae:0.039 #835e50:0.030 #bda578:0.013
- **Hierarchy:** Bubble first (colour), then host.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0347; hard replace EP0348.
- **Narration (ASR, unverified):** coverage,
- **Story function (INFERRED):** INFERRED: media pushing opinions as facts (ASR: coverage,).
- **Continuity:** Continues S0259.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0261 — f10760-10772 (448.375-448.875 s, 13 frames, 0.54 s) — shot SH101 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0348.jpg; entry EP0348, exit EP0349; second review: MINOR
- **Objects/placement (OBSERVED):** Pieces of flat-pack furniture: tall brown board x0.28-0.37 y0.10-0.45, flat board x0.38-0.50 y0.45-0.55; small seated builder with dark hair x0.52-0.65 y0.04-0.47 holding a board; loose planks x0.69-0.83 y0.42-0.55; small cardboard box with tiny logo and handwritten note above it x0.85-0.95 y0.28-0.48; grey folded BREAKING NEWS!!! newspaper at lower left x0.07-0.38 y0.53-0.88.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Builder dark-haired, bewildered mouth; boards brown flat with black outline; newspaper grey with darker header band and wiggly lines.
- **Typography:** Handwritten, note about 1.3% height black; newspaper title about 6% height black caps.
- **Readable text:** BREAKING NEWS!!! (newspaper); *box missing instructions* (note above box)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.853 #c1b8a7:0.061 #927e66:0.036 #0a0604:0.034 #433d35:0.016
- **Hierarchy:** Newspaper at lower left first (largest), then the builder.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0348; additive EP0349 at end.
- **Narration (ASR, unverified):** missing context,
- **Story function (INFERRED):** INFERRED: mocking sensational headlines (ASR: missing context).
- **Continuity:** Newspaper prop reused S0282.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0262 — f10773-10786 (448.917-449.458 s, 14 frames, 0.58 s) — shot SH101 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0349.jpg; entry EP0349, exit EP0350; second review: MINOR
- **Objects/placement (OBSERVED):** Pieces of flat-pack furniture: tall brown board x0.28-0.37 y0.10-0.45, flat board x0.38-0.50 y0.45-0.55; small seated builder x0.52-0.65 y0.04-0.47; loose planks x0.69-0.83 y0.42-0.55; small box with note x0.85-0.95 y0.28-0.48; grey BREAKING NEWS!!! newspaper at lower left x0.07-0.38 y0.53-0.88 with a white speech bubble x0.39-0.65 y0.58-0.89 holding red handwriting.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** As S0261; bubble round with black outline.
- **Typography:** Handwritten red marker, about 4% height, two lines, centre aligned.
- **Readable text:** LOCAL MAN STUPID! (bubble); BREAKING NEWS!!! (newspaper); *box missing instructions*
- **Unreadable/uncertain text:** Small note in the corner still tiny.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.837 #c2b7a7:0.064 #090604:0.042 #947c66:0.038 #4f3b37:0.019
- **Hierarchy:** Bubble first; newspaper second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0349; hard replace EP0350.
- **Narration (ASR, unverified):** context,
- **Story function (INFERRED):** INFERRED: satirical headline.
- **Continuity:** Continues S0261.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0263 — f10787-10799 (449.500-450.000 s, 13 frames, 0.54 s) — shot SH102 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0350.jpg; entry EP0350, exit EP0351; second review: MINOR
- **Objects/placement (OBSERVED):** Small smiling presenter x0.20-0.36 y0.06-0.80 with a folded NEWS paper under one arm x0.15-0.29 y0.60-0.90.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; paper beige with scribbled lines and rotated NEWS lettering.
- **Typography:** Rotated hand-lettered NEWS about 5% height.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.931 #e5ceb2:0.046 #0d0a06:0.016 #716c62:0.005 #f9ef1f:0.002
- **Hierarchy:** Face first, paper second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0350; EP0351 changes expression.
- **Narration (ASR, unverified):** and no clear
- **Story function (INFERRED):** INFERRED: 'no clear understanding' lead-in.
- **Continuity:** Same body in S0264.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0264 — f10800-10847 (450.042-452.000 s, 48 frames, 2.00 s) — shot SH102 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0351.jpg; entry EP0351, exit EP0355; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter x0.19-0.35 y0.15-0.60 with frowning face and raised arm, folded NEWS paper under arm x0.15-0.33 y0.62-0.91; three bold red question marks with black outline appear in a row at x0.38-0.52 y0.32-0.55 later in the state (absent in the first frame).
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; skeptical brow. Question marks drawn in bold dark-red marker.
- **Typography:** Bright red hand-drawn question marks with black outline, about 12% of frame height.
- **Readable text:** ???
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.931 #e5ceb2:0.045 #100c08:0.017 #7c776c:0.005 #f8f01b:0.002
- **Hierarchy:** Question marks first (colour and size), then face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0351; micro EP0352-0354 add question marks; hard replace exit EP0355.
- **Narration (ASR, unverified):** clear understanding of what I'd just read. And
- **Story function (INFERRED):** INFERRED: confusion after the news (ASR: clear understanding of what I'd just read).
- **Continuity:** Same body as S0263.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0089 (ADDITIVE_ENTRY, f10813) A first red question mark appears to the right of the character.; EVI0090 (ADDITIVE_ENTRY, f10822) A second red question mark appears beside the first.; EVI0091 (ADDITIVE_ENTRY, f10831) A third red question mark appears, completing a row of three.

## S0265 — f10848-10889 (452.042-453.750 s, 42 frames, 1.75 s) — shot SH103 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0355.jpg; entry EP0355, exit EP0356; second review: MINOR
- **Objects/placement (OBSERVED):** Large reader x0.38-0.61 y0.13-0.82 with an open NEWS paper in front, smiling over the top, centred.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; paper held open to show scribbled columns and NEWS lettering.
- **Typography:** NEWS lettering about 6% height.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.890 #dfd0b3:0.067 #0b0805:0.024 #c0bb7b:0.013 #656154:0.007
- **Hierarchy:** One centred figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0355; hard replace EP0356.
- **Narration (ASR, unverified):** And trying to understand the news shouldn't
- **Story function (INFERRED):** INFERRED: 'trying to understand the news'.
- **Continuity:** Similar to S0252 but smaller and offset.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0266 — f10890-10958 (453.792-456.625 s, 69 frames, 2.88 s) — shot SH104 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0356.jpg; entry EP0356, exit EP0358; second review: MINOR
- **Objects/placement (OBSERVED):** Desk scene x0.07-0.91 y0.09-0.94: seated presenter head x0.45-0.56 y0.22-0.65, desktop monitor with chart x0.21-0.33 y0.18-0.33 with keyboard and mouse below, gold bar left x0.11-0.20, green bills x0.25-0.34 y0.70-0.84, loose papers, closed laptop x0.56-0.70, framed zigzag chart upper right x0.66-0.88 y0.05-0.38, brown briefcase right x0.77-0.88, paper plane and green dollar sign at lower right x0.85-0.93.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes plus colourful flat props with black outlines: gold bar yellow, bills green, papers off-white.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfb:0.869 #473f3d:0.036 #0a0b0a:0.036 #e2d59f:0.030 #6e9b76:0.029
- **Hierarchy:** Chart and presenter first; props radiate around.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0356; micro EP0357; regional animation EP0358 exits.
- **Narration (ASR, unverified):** shouldn't require a research project in itself. Which
- **Story function (INFERRED):** INFERRED: 'research project' - a desk full of work.
- **Continuity:** Briefcase/chart/bills reused S0255, S0271.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0092 (OTHER, f10913) No clear content change visible in the left-centre region of the desk scene; difference is a fraction of a percent and may be a tiny monitor or hand tweak.

## S0267 — f11016-11040 (459.042-460.042 s, 25 frames, 1.04 s) — shot SH105 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0358.jpg; entry EP0358, exit EP0359; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter at left x0.05-0.33 y0.15-1.0 holding a long pointer toward a brown-framed green board x0.38-0.95 y0.06-0.85 with large cream stylised block lettering and a smaller word beneath; yellow bar bottom-left about 24% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Presenter smiling open mouth, thick outline; board green with brown wooden frame; letters blocky light cream.
- **Typography:** Board lettering condensed sans caps about 22% height cream, subtitle sans about 8%.
- **Readable text:** GROUND News (board text)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfb:0.643 #3a8441:0.156 #70544b:0.085 #070504:0.074 #e6d4a6:0.042
- **Hierarchy:** Board lettering first, presenter and pointer second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Reveal by EP0358; hard/transition exit EP0359. 25 frames.
- **Narration (ASR, unverified):** Ground News.
- **Story function (INFERRED):** INFERRED: sponsor product reveal (ASR: Ground News).
- **Continuity:** Presenter style matches neighbouring states S0258-S0266; board appears only here and in the EP0358 reveal.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0268 — f11105-11121 (462.750-463.417 s, 17 frames, 0.71 s) — shot SH106 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0359.jpg; entry EP0359, exit EP0360; second review: MINOR
- **Objects/placement (OBSERVED):** Charcoal panel filled with a collage of overlapping news-page screenshots x0.06-0.89 y0.05-0.93 (photo of cooling towers with fire, politician portrait, many headlines, site mastheads); QR code x0.88-0.97 y0.80-0.96; yellow bar bottom-left about 24% wide.
- **Background:** Charcoal dark panel
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn; many tiny tiles of varying size and colour.
- **Typography:** Mixed headline serif/sans, tiny; one panel masthead red.
- **Readable text:** Mastheads VOA, AMERICAN WIRE, Newsweek; headlines Senate GOP Leader Casts Doubt on Trump's Dep...; Passenger in Waymo self-driving car gets stuck circling parking lot while trying to make flight
- **Unreadable/uncertain text:** Article body copy and most other headlines in the collage.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafafa:0.629 #201c1d:0.154 #bfbcba:0.087 #67505c:0.085 #af936c:0.044
- **Hierarchy:** Photo tiles with bright imagery draw the eye; QR is a high-contrast corner mark.
- **Camera/motion:** STATIC 2D; **entry/exit:** Assembled by EP0359; shrinks via EP0360.
- **Narration (ASR, unverified):** into one place,
- **Story function (INFERRED):** INFERRED: shows many sources aggregated in one place (ASR: into one place).
- **Continuity:** Same QR and bar appear until S0291.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0269 — f11130-11148 (463.792-464.542 s, 19 frames, 0.79 s) — shot SH106 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0360.jpg; entry EP0360, exit EP0361; second review: MINOR
- **Objects/placement (OBSERVED):** Phone mockup centred x0.38-0.63 y0.02-0.98 with a white summary screen (small heading, photo thumbnail, bullet lines, bias bar); QR code at lower right x0.88-0.97 y0.80-0.96.
- **Background:** Charcoal dark panel
- **Illustration:** Phone with white screen showing a headline, a photo, bullet text, a bias-bar graphic.
- **Typography:** UI sans tiny; heading about 2% height.
- **Readable text:** Ground Summary (heading); Immigration agents arrest Palestinian student who helped lead Columbia University protests (headline); Summary / Bias Comparison tabs
- **Unreadable/uncertain text:** Bullet paragraphs, bias percentages and the bottom nav labels.
- **Palette (MEASURED, top-5 k-means of representative frame):** #252425:0.602 #fcfcfc:0.213 #e8e9e5:0.149 #908f8d:0.029 #f6f12c:0.006
- **Hierarchy:** Phone screen centre is brightest.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0360; hard replace exit EP0361.
- **Narration (ASR, unverified):** so you get the context
- **Story function (INFERRED):** INFERRED: product demo of a story summary ('the context you need').
- **Continuity:** Same dark panel as S0268.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0270 — f11149-11178 (464.583-465.792 s, 30 frames, 1.25 s) — shot SH107 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0361.jpg; entry EP0361, exit EP0362; second review: OK
- **Objects/placement (OBSERVED):** Presenter reading open NEWS paper at bottom centre, head x0.35-0.58 y0.12-0.55, paper x0.30-0.69 y0.55-1.0; QR lower right; yellow bar about 24% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes with an open newspaper.
- **Typography:** NEWS lettering about 7% height.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.782 #e4d0b3:0.135 #0c0a08:0.056 #9c9883:0.023 #faef20:0.005
- **Hierarchy:** Face then paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0361; additive EP0362.
- **Narration (ASR, unverified):** the context you need to understand
- **Story function (INFERRED):** INFERRED: context lead-in.
- **Continuity:** Same reader as S0252/S0265.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0271 — f11179-11209 (465.833-467.083 s, 31 frames, 1.29 s) — shot SH107 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0362.jpg; entry EP0362, exit EP0363; second review: OK
- **Objects/placement (OBSERVED):** Reader at bottom centre with orbiting props: briefcase left x0.12-0.28 y0.44-0.65, green map doodle with eyes x0.14-0.40 y0.03-0.30, house and tower icons x0.45-0.58 y0.05-0.22, framed chart x0.72-0.97 y0.05-0.35, green bills x0.69-0.88 y0.48-0.68; QR lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; props flat with black outlines.
- **Typography:** NEWS lettering as S0270.
- **Readable text:** NEWS
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfb:0.662 #dfcfac:0.162 #070604:0.070 #659f68:0.059 #494237:0.046
- **Hierarchy:** Reader central, props orbit.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0362; hard transition EP0363.
- **Narration (ASR, unverified):** understand the bigger picture. Take
- **Story function (INFERRED):** INFERRED: 'bigger picture' as many topics.
- **Continuity:** Same set as S0255 plus QR.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0272 — f11227-11255 (467.833-469.000 s, 29 frames, 1.21 s) — shot SH108 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0363.jpg; entry EP0363, exit EP0364; second review: MINOR
- **Objects/placement (OBSERVED):** Dark article screenshot x0.23-0.98 y0.03-0.97 with large white headline at top-left and sidebar cards at right (stats table and a grid of circular source icons); small walking character at lower left x0.0-0.14 y0.65-1.0; QR lower right.
- **Background:** Dark charcoal-mode news-aggregator capture, real UI, not hand drawn
- **Illustration:** UI capture; character thick black outline, smiling, mid-stride.
- **Typography:** Headline sans bold about 4.5% height white; body about 1.3%.
- **Readable text:** Trump says he's banning MS NOW, CNN and Politico from White House (headline); sidebar Total News Sources 1099, Leaning Left 182, Leaning Right 157, Center 261, Last Updated 2 days ago, Bias Distribution 44% Center; tabs Left / Center / Right / Bias Comparison
- **Unreadable/uncertain text:** Bullet summary body text, podcast list entries and source-icon labels.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.442 #222222:0.231 #3a3836:0.192 #e2ccab:0.069 #847c7f:0.067
- **Hierarchy:** Large headline first, then the grid of icons.
- **Camera/motion:** STATIC 2D; **entry/exit:** Slide-in EP0363 then zoom EP0364.
- **Narration (ASR, unverified):** this story, for example.
- **Story function (INFERRED):** INFERRED: shows the example story (ASR: this story, for example).
- **Continuity:** Same article in S0273-S0275.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0093 (OTHER, f11254) Two-frame lead-in (f11254-11255, 25-47 px at contrast >=150) immediately before the large motion transition that starts at f11256; stick-figure presenter and dark-UI capture are about to move, small elements already shift

## S0273 — f11279-11292 (470.000-470.542 s, 14 frames, 0.58 s) — shot SH108 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0364.jpg; entry EP0364, exit EP0366; second review: OK
- **Objects/placement (OBSERVED):** Dark story page now larger x0.0-1.0 y0.0-1.0 with headline x0.06-0.70 y0.07-0.22, tab row, bullets, right stats panel x0.78-1.0; QR at lower right.
- **Background:** Full-bleed charcoal capture
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn; text larger after zoom.
- **Typography:** Headline sans bold about 6.5% height white; bullets about 1.8%.
- **Readable text:** Trump says he's banning MS NOW, CNN and Politico from White House
- **Unreadable/uncertain text:** Bullets about the ban; stats panel numbers; podcast list at bottom.
- **Palette (MEASURED, top-5 k-means of representative frame):** #242424:0.481 #383735:0.280 #f6f6f6:0.107 #b6b19e:0.071 #766e71:0.061
- **Hierarchy:** Headline dominates.
- **Camera/motion:** ZOOM (EP0364 scale-up, ends at this state); **entry/exit:** Zoom EP0364 into this state; micro EP0365; EP0366 additive.
- **Narration (ASR, unverified):** announced he's banning certain
- **Story function (INFERRED):** INFERRED: ASR 'announced he's banning certain...' - reading the story.
- **Continuity:** Same page as S0272 enlarged.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0094 (OTHER, f11282) No visible content change; a very small difference near the right-hand sidebar of the screenshot, possibly a cursor or hover state.

## S0274 — f11311-11355 (471.333-473.167 s, 45 frames, 1.88 s) — shot SH108 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0366.jpg; entry EP0366, exit EP0368; second review: MINOR
- **Objects/placement (OBSERVED):** Same dark story page full-bleed, plus a scowling blond character in a red tie holding a notepad rising from the bottom edge at x0.54-0.72 y0.55-1.0 over the lower part of the bullet text.
- **Background:** Full-bleed charcoal capture
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn; character thick outline, orange-tan skin, blond tousled hair, red tie.
- **Typography:** As S0273.
- **Readable text:** Trump says he's banning MS NOW, CNN and Politico from White House
- **Unreadable/uncertain text:** Bullets and sidebar.
- **Palette (MEASURED, top-5 k-means of representative frame):** #2a2928:0.728 #f5f5f5:0.108 #a9a7a9:0.069 #6a5f62:0.065 #d8af52:0.030
- **Hierarchy:** Headline first, scowling character second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entry EP0366; micro EP0367; exit EP0368 pan.
- **Narration (ASR, unverified):** publications from having White House press access.
- **Story function (INFERRED):** INFERRED: a character standing in for the person named in the story.
- **Continuity:** Page as S0273.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0095 (OBJECT_MOTION, f11312) Small red specks near the presenter's torso and mouse-arrow movement over a dark-UI news capture; yellow progress bar visible along the bottom edge; EVI0096 (OBJECT_MOTION, f11332) Mouse arrow moves a few pixels over the dark-UI article capture near the presenter's hand (x~0.52-0.54,y~0.72-1.0); EVI0097 (OBJECT_MOTION, f11350) Mouse arrow moves again over the same dark-UI capture (x~0.55-0.57); progress bar slightly longer
- **Intra-state motion intervals:** EP0367

## S0275 — f11396-11470 (474.875-477.958 s, 75 frames, 3.12 s) — shot SH109 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0368.jpg; entry EP0368, exit EP0370; second review: OK
- **Objects/placement (OBSERVED):** Presenter at centre-right x0.58-0.80 y0.15-0.95 holding a long pointer toward the left; partly slid-out story page at left x0.0-0.40 y0.0-0.93 showing a sidebar with source icon grid; QR lower right; yellow bar about 38%.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Presenter smiling, thin pointer stick.
- **Typography:** UI sans tiny.
- **Readable text:** Fragments: 'NN', 'Bias Distribution', 'Total News Sources'
- **Unreadable/uncertain text:** Sidebar numbers.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.559 #2e2d2d:0.310 #eed4a4:0.053 #a09ba1:0.039 #775b62:0.038
- **Hierarchy:** Presenter and pointer then the sidebar.
- **Camera/motion:** STATIC 2D; **entry/exit:** Pan EP0368; micro EP0369; hard replace EP0370.
- **Narration (ASR, unverified):** how many outlets are covering this story, where each one leans and
- **Story function (INFERRED):** INFERRED: ASR 'how many outlets are covering this story, where each one leans'.
- **Continuity:** Sidebar panel continues from S0274.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0098 (POSE_SWAP, f11439) Presenter's pointer stick swings from a lower angle to a more upright diagonal angle toward the screenshot at left.

## S0276 — f11471-11494 (478.000-478.958 s, 24 frames, 1.00 s) — shot SH109 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0370.jpg; entry EP0370, exit EP0372; second review: OK
- **Objects/placement (OBSERVED):** Presenter at left x0.06-0.28 y0.20-1.0 pointing; dark article list at right x0.35-0.94 y0.0-1.0 with tab row (All selected), five article rows; QR lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn; presenter calm face.
- **Typography:** UI sans; row headlines about 1.7% height white.
- **Readable text:** 1099 Articles; tabs All, Left, Center, Right; headlines such as 'Trump 'overreacted' with press ban, says Newsmax media CEO'
- **Unreadable/uncertain text:** Source chips, bias labels and dates.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.415 #232323:0.332 #3c3b3b:0.142 #e2d2ab:0.070 #7e7b80:0.041
- **Hierarchy:** List then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0370; micro EP0371; additive/tab switch EP0372.
- **Narration (ASR, unverified):** and lets you compare headlines
- **Story function (INFERRED):** INFERRED: ASR 'lets you compare headlines'.
- **Continuity:** List continues S0277-S0279.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0099 (OBJECT_MOTION, f11473) Mouse arrow and red marks appear in a dark-UI news-search results list (x~0.49-0.54,y~0.14-1.0); EVI0100 (OBJECT_MOTION, f11478) Mouse arrow shifts over the dark-UI results list with small red/orange spots near the list top; EVI0101 (OTHER, f11484) Cursor-sized difference near the top of the list screenshot; no content change is visibly distinguishable.; EVI0102 (OBJECT_MOTION, f11487) Mouse arrow shifts over the dark-UI results list (x~0.16-0.6 region of the capture)

## S0277 — f11495-11553 (479.000-481.417 s, 59 frames, 2.46 s) — shot SH109 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0372.jpg; entry EP0372, exit EP0375; second review: OK
- **Objects/placement (OBSERVED):** Same layout; tab Left selected with a cursor on it; list now Left-leaning rows; presenter at left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn.
- **Typography:** UI sans as S0276.
- **Readable text:** Rows include 'Trump 'overreacted' with press ban...', 'The Press Finally Stands Up To Trump! Courage Is Contagious', 'Jon Stewart slams Trump media ban'
- **Unreadable/uncertain text:** Source chips.
- **Palette (MEASURED, top-5 k-means of representative frame):** #292928:0.462 #fcfcfc:0.411 #dccdbe:0.068 #717174:0.050 #f7f31e:0.008
- **Hierarchy:** List then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Tab switch EP0372; micro EP0373-0374; transition EP0375.
- **Narration (ASR, unverified):** headlines to see how differently they're framing the same thing.
- **Story function (INFERRED):** INFERRED: comparing the same story across sides.
- **Continuity:** Sibling of S0276, S0278.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0103 (OBJECT_MOTION, f11527) Mouse arrow and a red mark move near a result headline in the dark-UI list (x~0.42-0.69,y~0.09-1.0); EVI0104 (OTHER, f11529) One-frame cursor or underline tweak near the top of the list; nothing else changes.; EVI0105 (OBJECT_MOTION, f11531) Mouse arrow moves over result headlines in the dark-UI list (x~0.52-0.69)
- **Intra-state motion intervals:** EP0373

## S0278 — f11557-11602 (481.583-483.458 s, 46 frames, 1.92 s) — shot SH109 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0375.jpg; entry EP0375, exit EP0377; second review: OK
- **Objects/placement (OBSERVED):** Same layout; Center tab selected with cursor; rows changed; presenter flat-faced at left with pointer extended.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn; presenter flat mouth.
- **Typography:** UI sans as S0276.
- **Readable text:** Rows include 'Trump Criticizes the Press for Not Reporting False Achievements', 'The banning season', 'CNN, MS NOW & Politico Banned From White House...'
- **Unreadable/uncertain text:** Chips.
- **Palette (MEASURED, top-5 k-means of representative frame):** #292928:0.470 #fcfcfc:0.413 #decebd:0.065 #747170:0.043 #f7f11f:0.009
- **Hierarchy:** List then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Transition EP0375; micro EP0376; transition EP0377.
- **Narration (ASR, unverified):** And as you can see, the framing is all over
- **Story function (INFERRED):** INFERRED: ASR 'the framing is all over'.
- **Continuity:** Sibling of S0277, S0279.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0106 (OBJECT_MOTION, f11584) Mouse arrow moves toward the right of the result list (x~0.16-0.79); presenter's pointer stick overlaps the capture
- **Intra-state motion intervals:** EP0376

## S0279 — f11606-11722 (483.625-488.458 s, 117 frames, 4.88 s) — shot SH109 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0377.jpg; entry EP0377, exit EP0381; second review: OK
- **Objects/placement (OBSERVED):** Presenter at left x0.07-0.30; dark list at right x0.35-0.94 showing Right tab rows, first headline in larger bold; QR lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn.
- **Typography:** UI sans as S0276.
- **Readable text:** Rows include 'Banned At The Gate: Trump Boots Major Networks From White House As Obama Unleashes Blistering Warning', 'Lots of MSM Crying About White House Banning'
- **Unreadable/uncertain text:** Chips.
- **Palette (MEASURED, top-5 k-means of representative frame):** #292828:0.462 #fcfcfc:0.411 #decebf:0.074 #7c7a79:0.044 #f7f31f:0.009
- **Hierarchy:** List first, presenter second.
- **Camera/motion:** STATIC 2D; **entry/exit:** Transition EP0377; micro EP0378-0380; hard replace EP0381.
- **Narration (ASR, unverified):** the place. Some make it sound like it's a done deal, others make it sound like it's just getting started.
- **Story function (INFERRED):** INFERRED: 'done deal' vs 'just getting started' framing.
- **Continuity:** Sibling of S0278.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0107 (POSE_SWAP, f11618) Presenter's pointer tip moves up the list; red mark in diff follows the pointer and arm only.; EVI0108 (OTHER, f11641) Tiny difference near the right edge of the list (possible scrollbar or cursor); not distinguishable.; EVI0109 (OTHER, f11666) Tiny difference near the pointer tip over the list; not clearly visible.

## S0280 — f11723-11770 (488.500-490.458 s, 48 frames, 2.00 s) — shot SH110 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0381.jpg; entry EP0381, exit EP0382; second review: MINOR
- **Objects/placement (OBSERVED):** Single smiling full-body stick presenter centred x0.41-0.59 y0.15-0.95 with arms out in a relaxed shrug; QR code lower right; yellow bar at bottom-left.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; open smile.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.931 #f0d3b5:0.036 #0c0a09:0.016 #f7ef1c:0.010 #757271:0.007
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0381; additive EP0382.
- **Narration (ASR, unverified):** And sometimes the bigger issue isn't how a
- **Story function (INFERRED):** INFERRED: pause between points.
- **Continuity:** Same body as S0257/S0294.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0281 — f11771-11797 (490.500-491.583 s, 27 frames, 1.12 s) — shot SH110 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0382.jpg; entry EP0382, exit EP0384; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling presenter x0.41-0.59 y0.15-0.95 with arms out; tan NEWS paper tilted at upper left x0.08-0.34 y0.12-0.55; a red outlined word with a question mark appears at right x0.64-0.90 y0.25-0.40 late in the state; QR lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; paper beige with scribble columns.
- **Typography:** NEWS lettering about 6% height.
- **Readable text:** NEWS (on paper); Context? (red outlined word, appears late in the state)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.859 #dbcdaf:0.083 #0b0906:0.035 #6d6a63:0.012 #f7ef1b:0.011
- **Hierarchy:** Presenter then paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0382; additive EP0383 (Context? added).
- **Narration (ASR, unverified):** a story is framed, but
- **Story function (INFERRED):** INFERRED: 'a story is framed'.
- **Continuity:** Paper reused in S0289.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0110 (ADDITIVE_ENTRY, f11784) A dark-red outlined word with question mark (Context?) appears at right of the presenter.

## S0282 — f11798-11821 (491.625-492.583 s, 24 frames, 1.00 s) — shot SH111 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0384.jpg; entry EP0384, exit EP0385; second review: WRONG
- **Objects/placement (OBSERVED):** Huge smiling head in a checkered brown detective cap x0.10-0.43 y0.0-0.76 with a body line leaving the bottom left, magnifying glass x0.45-0.56 y0.51-0.84; grey folded BREAKING NEWS!!! newspaper at upper right x0.59-0.91 y0.19-0.53; QR lower right; yellow bar bottom-left about 66% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn thick black marker outline, beige skin, brown tweed-textured detective cap, glass lens in pale blue; newspaper in flat grey with wavy squiggle lines.
- **Typography:** Hand-lettered BREAKING NEWS!!! caps about 7% of frame height, dark grey outlined, left aligned on the paper.
- **Readable text:** BREAKING NEWS!!!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.694 #f5d6a8:0.129 #090706:0.076 #b9b2ab:0.065 #635c4f:0.036
- **Hierarchy:** Eye goes first to the huge detective head, then to the magnifying glass, then to the BREAKING NEWS paper at right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0383; hard replace EP0384.
- **Narration (ASR, unverified):** but whether you see it at
- **Story function (INFERRED):** INFERRED: raising the missing-context point.
- **Continuity:** Detective cap character recurs from S0258; newspaper removed in S0283 while the detective stays.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0283 — f11831-11838 (493.000-493.292 s, 8 frames, 0.33 s) — shot SH111 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0385.jpg; entry EP0385, exit EP0386; second review: WRONG
- **Objects/placement (OBSERVED):** Huge smiling head in a checkered brown detective cap x0.10-0.43 y0.0-0.76, magnifying glass x0.45-0.56 y0.51-0.84, body line leaving the bottom left; no other objects; QR lower right; yellow bar bottom-left about 68% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes plus checkered cap and magnifier.
- **Typography:** none
- **Readable text:** BREAKING NEWS!!!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.776 #f2d2b5:0.125 #0d0b0a:0.060 #716959:0.028 #f7f01b:0.011
- **Hierarchy:** Eye goes to the huge detective head and then the magnifying glass; empty right half gives a pause.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0384; paper exits via EP0385.
- **Narration (ASR, unverified):** all. Ground
- **Story function (INFERRED):** INFERRED: searching for hidden stories.
- **Continuity:** Direct continuation of S0282 with the BREAKING NEWS paper dropped; next state S0284 cuts to a laptop.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0284 — f11839-11887 (493.333-495.333 s, 49 frames, 2.04 s) — shot SH112 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0386.jpg; entry EP0386, exit EP0387; second review: WRONG
- **Objects/placement (OBSERVED):** Grey laptop with thick black bezel x0.13-0.88 y0.06-1.0 on a brown desk; screen shows a light news page with a logo and nav bar at top, a Blindspot banner, then two columns each with two photo cards (Capitol dome, man in suit speaking, woman at rally, crowd) and headlines with small percentage bars; QR lower right x0.88-0.97; yellow bar bottom-left about 68% wide.
- **Background:** White canvas with a brown desk strip across the lower corners
- **Illustration:** Hand-drawn laptop with thick black outline and grey body; the screen is a real website screenshot, not hand drawn.
- **Typography:** Page headings sans bold about 1.5% frame height; card headlines sans about 1.2%; very small.
- **Readable text:** For the Left; For the Right; Cost of Federal Regulations Hit Record High in 2023, Report Says; Acting Secret Service Chief's Role Limiting Trump Resources; Harris is calibrating her policy pitch for going to battle with Trump; Harris' views on key issues over the years
- **Unreadable/uncertain text:** Navigation labels, topic chips, source counts and percentage values.
- **Palette (MEASURED, top-5 k-means of representative frame):** #f1f2ef:0.574 #8a7e79:0.161 #080706:0.153 #534b4b:0.098 #f1e824:0.013
- **Hierarchy:** Eye goes to the bright screen content and the four photo cards, with the desk and bezel framing it.
- **Camera/motion:** STATIC 2D; **entry/exit:** After EP0385 paper exit; hard replace EP0386.
- **Narration (ASR, unverified):** Ground News has a blind spot feed that highlights
- **Story function (INFERRED):** INFERRED: 'all.' pause.
- **Continuity:** Follows the detective close-ups S0282 and S0283; the same laptop zooms into card detail in S0285 to S0287.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0285 — f11905-11910 (496.083-496.292 s, 6 frames, 0.25 s) — shot SH112 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0387.jpg; entry EP0387, exit EP0388; second review: WRONG
- **Objects/placement (OBSERVED):** Grey laptop x0.13-0.88 y0.06-1.0 on a brown desk, screen zoomed into a row of four news cards: building photo, glass tower with logo, woman before flags, woman portrait, each with headline and thin percentage bars; a partly cut lower row with a bold KAMALA banner; QR lower right.
- **Background:** White canvas, brown desk strip
- **Illustration:** Hand-drawn laptop shell; the screen is a real website screenshot, not hand drawn.
- **Typography:** Card headlines sans bold about 1.5% height, tiny; labels tiny.
- **Readable text:** America is not ready for a major war, says a bipartisan commission; Microsoft lays off internal DEI team, says diversity is 'no longer business critical'; Conservatives Accuse Kamala Harris of Being 'DEI Hire'; About 8 in 10 Democrats are satisfied with Harris in stark shift after Biden drops out
- **Unreadable/uncertain text:** Source counts, bias labels and percentage values.
- **Palette (MEASURED, top-5 k-means of representative frame):** #f3f3f1:0.510 #8c837c:0.177 #070707:0.157 #4f4b4a:0.142 #f1e823:0.014
- **Hierarchy:** Eye scans the four photo cards left to right, with the faces drawing most attention.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0386; scroll EP0387; EP0388 pop.
- **Narration (ASR, unverified):** stories one
- **Story function (INFERRED):** INFERRED: introducing a blind-spot feed (ASR: Ground News has a blind spot feed).
- **Continuity:** Zoom continuation from S0284; S0286 blurs three cards and enlarges the second.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0286 — f11919-11929 (496.667-497.083 s, 11 frames, 0.46 s) — shot SH112 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0388.jpg; entry EP0388, exit EP0389; second review: OK
- **Objects/placement (OBSERVED):** Laptop with page blurred; second card enlarged x0.28-0.52 y0.28-0.80 (building photo, headline, bars); others blurred; QR lower right.
- **Background:** White canvas, brown desk
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn with depth blur.
- **Typography:** Headline sans bold about 2.3% height.
- **Readable text:** Microsoft lays off internal DEI team, says diversity is 'no longer business critical'
- **Unreadable/uncertain text:** Small bars and counts.
- **Palette (MEASURED, top-5 k-means of representative frame):** #f3f4f1:0.491 #786f6a:0.194 #040505:0.144 #bcbe9e:0.091 #403b40:0.080
- **Hierarchy:** Sharp enlarged card first.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0388; exit EP0389.
- **Narration (ASR, unverified):** side of the political
- **Story function (INFERRED):** INFERRED: highlighting a one-sided story.
- **Continuity:** Same screen as S0285.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0287 — f11939-12052 (497.500-502.208 s, 114 frames, 4.75 s) — shot SH112 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0389.jpg; entry EP0389, exit EP0394; second review: MINOR
- **Objects/placement (OBSERVED):** Laptop screen with two enlarged cards: left building photo x0.26-0.45, right portrait with flags x0.46-0.66; others blurred; highlights on headlines.
- **Background:** White canvas, brown desk
- **Illustration:** Dark-mode news-aggregator capture, real UI, not hand drawn.
- **Typography:** Headline sans about 2.3% height.
- **Readable text:** Microsoft lays off internal DEI team...; Conservatives Accuse Kamala Harris of Being 'DEI Hire'
- **Unreadable/uncertain text:** Bars.
- **Palette (MEASURED, top-5 k-means of representative frame):** #f4f4f1:0.482 #706462:0.236 #0f0c0f:0.184 #b2b3b1:0.083 #eee325:0.015
- **Hierarchy:** Two sharp cards.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0389-0393.
- **Narration (ASR, unverified):** spectrum is barely covering, so you can catch what might be missing from your usual news feed.
- **Story function (INFERRED):** INFERRED: ASR 'stories one side... barely covering'.
- **Continuity:** Continues S0286.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0111 (HIGHLIGHT_ADD, f11964) Highlight band extends onto a further line of the right card's headline.; EVI0112 (HIGHLIGHT_ADD, f11968) A small red or highlighted fragment appears in the percentage bar region under the right card.
- **Intra-state motion intervals:** EP0390;EP0391

## S0288 — f12053-12088 (502.250-503.708 s, 36 frames, 1.50 s) — shot SH113 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0394.jpg; entry EP0394, exit EP0395; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling full-body stick presenter standing x0.41-0.59 y0.15-0.85 with hands on hips, eyes closed in a grin; QR lower right; yellow bar bottom-left about 80% wide.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes; closed-eye smile.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.925 #f0d6b5:0.039 #0d0b0a:0.016 #f7f31f:0.013 #757371:0.007
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0394; EP0395.
- **Narration (ASR, unverified):** That's why I like Ground News. You
- **Story function (INFERRED):** INFERRED: wrap with a positive line.
- **Continuity:** Same pose as S0280.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0289 — f12099-12101 (504.167-504.250 s, 3 frames, 0.12 s) — shot SH113 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0395.jpg; entry EP0395, exit EP0396; second review: MINOR
- **Objects/placement (OBSERVED):** Small presenter x0.42-0.55 y0.45-0.95 arms up; NEWS paper left x0.07-0.27 y0.40-0.70; green map x0.30-0.54 y0.03-0.35; BREAKING NEWS x0.60-0.82 y0.10-0.30. 3 frames.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes.
- **Typography:** Hand-lettered titles.
- **Readable text:** NEWS; BREAKING NEWS!!!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.846 #cdc3ad:0.064 #548e57:0.044 #10110b:0.033 #f7f31f:0.014
- **Hierarchy:** Map top.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0395 entry; EP0396.
- **Narration (ASR, unverified):** the full
- **Story function (INFERRED):** INFERRED: animation tail.
- **Continuity:** As S0290.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0290 — f12102-12162 (504.292-506.792 s, 61 frames, 2.54 s) — shot SH113 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0396.jpg; entry EP0396, exit EP0398; second review: MINOR
- **Objects/placement (OBSERVED):** As S0289 plus green money bag x0.77-0.95 y0.45-0.80.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Hand-drawn stick character, thick black marker outline, flat peach fill, spiky black hair, dot eyes.
- **Typography:** Hand-lettered.
- **Readable text:** NEWS; BREAKING NEWS!!!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.827 #cdc3ad:0.064 #5a8d5a:0.056 #10110b:0.039 #f5f122:0.015
- **Hierarchy:** Map.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0396; EP0397; EP0398.
- **Narration (ASR, unverified):** full picture, and you get to decide what to make of it.
- **Story function (INFERRED):** INFERRED: 'decide what to make of it'.
- **Continuity:** S0289.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.
- **Intra-state events:** EVI0113 (POSE_SWAP, f12118) The character's raised arms drop to a relaxed stance and the mouth changes slightly; props stay.

## S0291 — f12163-12187 (506.833-507.833 s, 25 frames, 1.04 s) — shot SH114 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0398.jpg; entry EP0398, exit EP0399; second review: MINOR
- **Objects/placement (OBSERVED):** Grey-haired character with purple tie x0.68-0.89 y0.12-1.0; speech bubble x0.19-0.62 y0.20-0.72; QR lower right.
- **Background:** flat off-white whiteboard canvas
- **Illustration:** Grey hair, tan skin, purple tie; bubble black outline.
- **Typography:** Handwritten about 5%.
- **Readable text:** Sounds interesting!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.857 #060506:0.065 #beb7ac:0.048 #756282:0.016 #f6f11e:0.014
- **Hierarchy:** Bubble.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0398; EP0399.
- **Narration (ASR, unverified):** If you're interested,
- **Story function (INFERRED):** INFERRED: viewer voice for CTA.
- **Continuity:** None.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, colours and any quoted text from the state tile. INFERRED: story role from ASR wording only.

## S0292 — f12188-12305 (507.875-512.750 s, 118 frames, 4.92 s) — shot SH115 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0399.jpg; entry EP0399, exit EP0401; second review: OK
- **Objects/placement (OBSERVED):** Stick presenter left (x .07-.3, y .12-.95) holding a long thin pointer stick; heading text top (x .34-.92, y .06-.18); large black-and-white QR code with centre logo (x .49-.75, y .27-.73); yellow bar at bottom edge about 87% of width.
- **Background:** Flat near-white canvas (#FCFCFC) with a thin yellow bar along the bottom edge.
- **Illustration:** Black wobbly marker outlines, peach flat-filled round head, spiky black hair, dot eyes, curved smile; thin stick body; QR is a clean vector graphic. Face widens to open grin about 2.4 s in.
- **Typography:** Handwritten marker script for the heading plus a condensed bold wordmark; about 7% of frame height; black; left-aligned inline.
- **Readable text:** Want to check out [GROUND News wordmark] ?
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.843 #0c0c0b:0.073 #e9d3b9:0.048 #6d6b6a:0.020 #f7f11d:0.014
- **Hierarchy:** Heading across the top first, then the QR as the largest dark mass, then the presenter pointing at it.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace from a speech-bubble scene (EP0399); one micro expression change (EP0400); exits by typed-text swap (EP0401). Entry EP0399, exit EP0401.
- **Narration (ASR, unverified):** you can get 40 % off the Ground News vantage plan by scanning the QR code on screen, or
- **Story function (INFERRED):** Sponsor call to action: invites viewer to scan the code (inferred from ASR about scanning the QR code).
- **Continuity:** Same QR/presenter layout continues in S0293; yellow bar continues to S0295.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0114 (EXPRESSION_CHANGE, f12260) Presenter's face changes from closed small smile to wide open-mouth grin with arched eyes (left); pointer arm slightly shifts. Rest of QR scene unchanged.

## S0293 — f12324-12374 (513.542-515.625 s, 51 frames, 2.12 s) — shot SH115 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0401.jpg; entry EP0401, exit EP0404; second review: OK
- **Objects/placement (OBSERVED):** Presenter left (x .06-.3); typed URL text top centre (x .4-.57, y .05-.13, grows rightward); QR centre (x .49-.75, y .27-.7); green handwritten offer line below QR (x .34-.62, y .78-.88); yellow bar bottom.
- **Background:** Flat near-white canvas (#FCFCFC) with a thin yellow bar along the bottom edge.
- **Illustration:** Same presenter as S0292 with closed smile; green marker lettering with slight wobble.
- **Typography:** Handwritten marker; black URL about 7%, green offer text about 6% height; centred under QR.
- **Readable text:** ground. (typed on; later 'ground.news/casual'); 40% off the Vantage Plan!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.847 #090908:0.064 #e4d5b8:0.049 #668b6a:0.024 #f7f11a:0.016
- **Hierarchy:** Typed URL catches the eye as it grows, then green offer line, then QR.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Begins as typed-text replacement of the heading (EP0401); URL keeps typing (EP0402, EP0403); hard cut out (EP0404). Entry EP0401, exit EP0404.
- **Narration (ASR, unverified):** ground .news .casual. Thank
- **Story function (INFERRED):** Shows the discount code and web address (inferred from ASR 'ground .news .casual').
- **Continuity:** Layout follows S0292; green line is new.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state motion intervals:** EP0402;EP0403

## S0294 — f12375-12403 (515.667-516.833 s, 29 frames, 1.21 s) — shot SH116 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0404.jpg; entry EP0404, exit EP0405; second review: OK
- **Objects/placement (OBSERVED):** Presenter centre-left (x .24-.37, y .12-.95) hands on hips, smiling; large wordmark creature at right (x .5-.86, y .48-.85) formed from heavy condensed black letters with curved arms and two legs and small 'News' subtext; yellow bar bottom.
- **Background:** Flat near-white canvas (#FCFCFC) with a thin yellow bar along the bottom edge.
- **Illustration:** Peach head, spiky hair, dot eyes, wide smile; logo drawn as condensed black block letters with marker arms/legs.
- **Typography:** Condensed bold sans wordmark about 20% of frame height, black; small sans 'News' about 3%.
- **Readable text:** GROUND News
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.900 #1b1a1a:0.039 #efd3b5:0.038 #f7ef1c:0.016 #787675:0.007
- **Hierarchy:** The wordmark creature is the heaviest dark shape; eye then goes to the presenter.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace from QR layout (EP0404); next pose change EP0405. Entry EP0404, exit EP0405.
- **Narration (ASR, unverified):** Thank you to Ground News for sponsoring
- **Story function (INFERRED):** Sponsor brand introduction, thanks (inferred from ASR 'Thank you to Ground News').
- **Continuity:** Same wordmark creature reappears in S0295.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0295 — f12404-12437 (516.875-518.250 s, 34 frames, 1.42 s) — shot SH116 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0405.jpg; entry EP0405, exit EP0406; second review: OK
- **Objects/placement (OBSERVED):** Presenter centre-left (x .15-.4) eyes closed in a happy smile, one arm stretched toward the wordmark creature; wordmark creature right (x .55-.83, y .42-.9) tilted; yellow bar bottom.
- **Background:** Flat near-white canvas (#FCFCFC) with a thin yellow bar along the bottom edge.
- **Illustration:** Same drawing style; presenter eyes drawn as arcs; arm raised in high-five.
- **Typography:** Same condensed wordmark, about 20% of height.
- **Readable text:** GROUND News
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.899 #1b1a19:0.040 #efd3b5:0.038 #f7ef1c:0.016 #7c7978:0.006
- **Hierarchy:** Presenter-logo contact point in the middle draws the eye.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Pose swap from S0294 (EP0405); exits through map slide-in (EP0406). Entry EP0405, exit EP0406.
- **Narration (ASR, unverified):** for sponsoring this video.
- **Story function (INFERRED):** Warm thank-you to the sponsor (inferred).
- **Continuity:** Pose variant of S0294.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0296 — f12470-12477 (519.625-519.917 s, 8 frames, 0.33 s) — shot SH117 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0406.jpg; entry EP0406, exit EP0407; second review: OK
- **Objects/placement (OBSERVED):** Green map-of-the-country character left to centre (x .11-.56, y .12-.86) with two big round eyes, curved legs, islands scattered bottom-left; empty white right half.
- **Background:** Flat near-white canvas, no bottom bar.
- **Illustration:** Flat green fill with thick black outline; eyes white with black pupils; legs are curved black lines.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.847 #48a350:0.125 #041205:0.018 #345136:0.007 #a0a6a1:0.003
- **Hierarchy:** Single green mass centre-left; large empty space to the right.
- **Camera/motion:** STATIC 2D; settles after slide-in (EP0406); **entry/exit:** Slides in from the left edge during EP0406; exits by small icons popping in (EP0407). Entry EP0406, exit EP0407.
- **Narration (ASR, unverified):** stepped into the
- **Story function (INFERRED):** Transitions from sponsor to main topic: the country as a character (inferred from ASR 'stepped into the housing market').
- **Continuity:** Same map character in S0297, S0304, S0308.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0297 — f12478-12501 (519.958-520.917 s, 24 frames, 1.00 s) — shot SH117 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0407.jpg; entry EP0407, exit EP0408; second review: OK
- **Objects/placement (OBSERVED):** Map character left (x .11-.56); three small doodles right: pink house (x .62-.68, y .26-.36), tall grey apartment building (x .7-.78, y .22-.4), blue duplex (x .66-.74, y .44-.55).
- **Background:** Flat near-white canvas.
- **Illustration:** Same green map; icons in flat pastel fills with thin outlines, small scale (~12% of height).
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.800 #49a351:0.125 #081108:0.034 #c1c2bb:0.023 #4b5547:0.018
- **Hierarchy:** Map first by size, then the icon trio at right.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive pop-in of icons (EP0407); replaced by sliding LAW document (EP0408). Entry EP0407, exit EP0408.
- **Narration (ASR, unverified):** into the housing market.
- **Story function (INFERRED):** Shows housing stock the map 'stepped into' (inferred).
- **Continuity:** Map from S0296; icons reappear in S0305 as tiny stack.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0298 — f12516-12546 (521.542-522.792 s, 31 frames, 1.29 s) — shot SH118 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0408.jpg; entry EP0408, exit EP0409; second review: OK
- **Objects/placement (OBSERVED):** Large paper labelled LAW (x .14-.44, y .13-.77) tilted slightly; small cream house with red roof overlapping its lower right (x .33-.44, y .55-.77); teal-grey tall building (x .46-.61, y .45-.77).
- **Background:** Flat near-white canvas.
- **Illustration:** Paper in cream-grey fill with black wobbly lines of fake text and a white oval behind the title; building with dark windows grid.
- **Typography:** Hand-lettered capitals, black, about 10% height, centred on the paper top.
- **Readable text:** LAW
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.849 #d7d0cb:0.077 #090706:0.035 #818b8b:0.020 #504d4d:0.019
- **Hierarchy:** Document first (largest, high contrast heading), then buildings.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Slides in from left (EP0408); head enters at right (EP0409). Entry EP0408, exit EP0409.
- **Narration (ASR, unverified):** housing policy tends to do one
- **Story function (INFERRED):** Policy topic: housing law (inferred from ASR 'housing policy').
- **Continuity:** Building and house icons echo S0297 style.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0299 — f12547-12578 (522.833-524.125 s, 32 frames, 1.33 s) — shot SH118 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0409.jpg; entry EP0409, exit EP0410; second review: MINOR
- **Objects/placement (OBSERVED):** LAW paper and buildings left (x .14-.61); huge tilted presenter head right cropped at the edge (x .67-1.0, y .14-.55) with raised hand/arm lines below.
- **Background:** Flat near-white canvas.
- **Illustration:** Peach head, wild black hair, dot eyes, smile; tilted about 20 degrees as peeking.
- **Typography:** Hand-lettered black capitals LAW about 10% height centred on the paper top, as in the previous state.
- **Readable text:** LAW
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.776 #e2d1c3:0.128 #080605:0.052 #848c8b:0.022 #4f4c4b:0.022
- **Hierarchy:** Head is the biggest warm shape; then LAW.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry (EP0409); replaced by hoodie figure (EP0410). Entry EP0409, exit EP0410.
- **Narration (ASR, unverified):** one of two things.
- **Story function (INFERRED):** Presenter comments on how policy works (inferred).
- **Continuity:** Same LAW cluster as S0298.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0300 — f12579-12588 (524.167-524.542 s, 10 frames, 0.42 s) — shot SH119 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0410.jpg; entry EP0410, exit EP0411; second review: OK
- **Objects/placement (OBSERVED):** Grey-hoodie figure with sunglasses and a tuft of blond hair at left (x .09-.3, y .13-.8) holding a green banknote at right hand (x .27-.31, y .35-.42).
- **Background:** Flat near-white canvas.
- **Illustration:** Tan bald head, black shades, grey hoodie with darker outline, thin legs; banknote green with a dollar mark.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.960 #888c85:0.016 #070604:0.012 #d2bbab:0.010 #42433d:0.003
- **Hierarchy:** Single figure; green note is the only saturated accent.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0410); a second figure arrives (EP0411). Entry EP0410, exit EP0411.
- **Narration (ASR, unverified):** It either adds
- **Story function (INFERRED):** Introduces first character in a 'who benefits' scene (inferred; ASR 'It either adds').
- **Continuity:** Figure reused in S0301-S0303.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0301 — f12589-12596 (524.583-524.875 s, 8 frames, 0.33 s) — shot SH119 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0411.jpg; entry EP0411, exit EP0412; second review: OK
- **Objects/placement (OBSERVED):** Hoodie figure left (x .05-.28) and a grey-haired figure in a purple tie at right (x .34-.47, y .12-.83) holding a banknote up.
- **Background:** Flat near-white canvas.
- **Illustration:** Grey hair swirl, smiling, purple tie, thin black body.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.939 #070505:0.020 #878a85:0.020 #c9b9ad:0.017 #41423d:0.005
- **Hierarchy:** Two figures balanced; notes mark the exchange.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry (EP0411); another arrives (EP0412). Entry EP0411, exit EP0412.
- **Narration (ASR, unverified):** either adds buyers,
- **Story function (INFERRED):** Second buyer type added (inferred; 'adds buyers').
- **Continuity:** Continues S0300; precedes S0302.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0302 — f12597-12612 (524.917-525.542 s, 16 frames, 0.67 s) — shot SH119 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0412.jpg; entry EP0412, exit EP0413; second review: OK
- **Objects/placement (OBSERVED):** Hoodie figure left (x .05-.28); grey-haired purple-tie figure upper right (x .34-.47); third bald figure with green tie and closed happy eyes bottom centre (x .31-.46, y .4-.93) holding a note.
- **Background:** Flat near-white canvas.
- **Illustration:** Same style; third figure round tan head, curved smile, green tie.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #070605:0.026 #cebdb0:0.024 #858c82:0.023 #42443e:0.006
- **Hierarchy:** Three-figure triangle; eye travels between the notes.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry (EP0412); armchair added (EP0413). Entry EP0412, exit EP0413.
- **Narration (ASR, unverified):** adds buyers,
- **Story function (INFERRED):** Three buyers 'added' (inferred from ASR 'adds buyers').
- **Continuity:** Continues S0301; precedes S0303.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0303 — f12613-12649 (525.583-527.083 s, 37 frames, 1.54 s) — shot SH119 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0413.jpg; entry EP0413, exit EP0415; second review: OK
- **Objects/placement (OBSERVED):** Three money figures left (x .05-.5); red armchair with a reclining figure right (x .65-.95, y .3-.87); later small speech bubble above chair (EP0414).
- **Background:** Flat near-white canvas.
- **Illustration:** Armchair flat dark red with darker outline; reclining figure small tan head, arms crossed behind.
- **Typography:** Handwritten small bubble text appears late.
- **Readable text:** I ain't moving!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.823 #ad4f4e:0.072 #130b09:0.049 #cebdaf:0.028 #81867c:0.027
- **Hierarchy:** Red chair is the heaviest saturated shape.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry of chair (EP0413); micro bubble (EP0414); hard cut to map close-up (EP0415). Entry EP0413, exit EP0415.
- **Narration (ASR, unverified):** or it keeps owners in place.
- **Story function (INFERRED):** Contrasts buyers with owners staying put (ASR 'keeps owners in place', inferred).
- **Continuity:** Figures from S0300-S0302 reused.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0115 (ADDITIVE_ENTRY, f12622) A small handwritten speech bubble reading 'I ain't moving!' appears above the armchair figure at upper right.

## S0304 — f12650-12685 (527.125-528.583 s, 36 frames, 1.50 s) — shot SH120 (inferred) — F9 full-bleed drawn scene
- **Evidence:** frames/ep_stable/e0415.jpg; entry EP0415, exit EP0416; second review: OK
- **Objects/placement (OBSERVED):** Close-up green map character filling left two-thirds (x 0-.71, y .1-.9): huge eyes (x .17-.35, y .36-.55), wide smile, legs at bottom, cropped by frame.
- **Background:** Flat near-white canvas.
- **Illustration:** Green flat fill, thick black outline, big white eyes with black pupils, black curved smile.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.582 #48a34f:0.358 #030a03:0.047 #2d4b30:0.009 #a9a7a8:0.004
- **Hierarchy:** Giant face/eyes dominate.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0415); paper added (EP0416). Entry EP0415, exit EP0416.
- **Narration (ASR, unverified):** The government rarely actually implements
- **Story function (INFERRED):** Returns to the country character for the government-policy beat (inferred).
- **Continuity:** Same character as S0296, scaled up.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0305 — f12686-12762 (528.625-531.792 s, 77 frames, 3.21 s) — shot SH120 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0416.jpg; entry EP0416, exit EP0422; second review: MINOR
- **Objects/placement (OBSERVED):** Same close-up map (x 0-.71, y .1-.95); beige paper labelled NEW POLICY with a small WE'LL DO THIS NOW line held at right of face (x .5-.67, y .43-.8); loose cluster of about ten tiny houses and grey tower blocks at right (x .73-.94, y .19-.8), added progressively over the state.
- **Background:** Flat near-white canvas.
- **Illustration:** Paper cream with red handwriting heading and scribbled lines; tiny pastel icons.
- **Typography:** Red hand-lettered heading about 5%, small black subtext.
- **Readable text:** NEW POLICY; WE'LL DO THIS NOW (small)
- **Unreadable/uncertain text:** scribbled lines below
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.556 #47a24f:0.329 #060e06:0.060 #eee8d6:0.046 #9f716f:0.009
- **Hierarchy:** Face first, paper second, icon cluster last.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive paper (EP0416); five micro icon additions (EP0417-0421); replaced via presenter/article slide (EP0422). Entry EP0416, exit EP0422.
- **Narration (ASR, unverified):** implements policy to add to the supply of homes on the market.
- **Story function (INFERRED):** Government 'adds to supply' of homes (inferred from ASR).
- **Continuity:** Icons echo S0297.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0116 (ADDITIVE_ENTRY, f12709) Two tiny doodles, a small house and a tall grey building, appear at top right as the first pair of a growing stack.; EVI0117 (ADDITIVE_ENTRY, f12713) Another tiny house/building cluster is added just below the first pair at upper right, enlarging the stack.; EVI0118 (ADDITIVE_ENTRY, f12719) A further tiny house and building group is added lower in the right-edge stack (about y 0.42-0.57).; EVI0119 (ADDITIVE_ENTRY, f12724) Another small house/building group appears further down the right-edge stack (about y 0.53-0.68).; EVI0120 (ADDITIVE_ENTRY, f12734) Final tiny house/building group added at the bottom of the right-edge stack (about y 0.65-0.80); stack now five groups tall.

## S0306 — f12775-12910 (532.333-537.958 s, 136 frames, 5.67 s) — shot SH121 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0422.jpg; entry EP0422, exit EP0423; second review: OK
- **Objects/placement (OBSERVED):** Presenter with pointer left (x .05-.35, y .1-.95); trade-association article screenshot right (x .39-.94, y .05-.92): small logo top-left, search/menu icons top-right, grey banner 'Washington Report', blue bold headline, small body text.
- **Background:** Cut-in white web page with pale grey header band over off-white canvas.
- **Illustration:** Presenter peach head, spiky hair, smile; article in clean sans web typography, blue headline.
- **Typography:** Web sans; banner title about 5%, headline about 5% bold blue, body about 1.5%.
- **Readable text:** Washington Report; President Trump Directs MBS Purchases to Lower Mortgage Rates; 'On Thursday, January 8, President Trump directed the Fannie Mae and Freddie Mac...'
- **Unreadable/uncertain text:** remaining body text, byline, date
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfb:0.892 #e3d2c3:0.051 #909ea6:0.025 #3c6a84:0.020 #0e0a09:0.012
- **Hierarchy:** Blue headline, then presenter pointing, then body.
- **Camera/motion:** STATIC 2D; article slides in during EP0422; **entry/exit:** Slides in at EP0422; hard replaced by document (EP0423). Entry EP0422, exit EP0423.
- **Narration (ASR, unverified):** January 8th, the president directed Fannie Mae and Freddie Mac to buy $200 billion of mortgage bonds.
- **Story function (INFERRED):** Source evidence for the Jan 8 directive (ASR).
- **Continuity:** Article layout reused conceptually in later screenshot+presenter states (S0336).
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0307 — f12911-12932 (538.000-538.875 s, 22 frames, 0.92 s) — shot SH122 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0423.jpg; entry EP0423, exit EP0424; second review: OK
- **Objects/placement (OBSERVED):** Single beige MORTGAGE document, slightly stacked, upper right of centre (x .64-.89, y .17-.7); everything else empty.
- **Background:** Flat near-white canvas.
- **Illustration:** Two stacked cream papers, red marker heading, black wiggly text lines, scribbled signatures at bottom.
- **Typography:** Hand-lettered red capitals about 7% height.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.889 #e8e2c9:0.073 #070504:0.025 #824542:0.008 #b49c92:0.005
- **Hierarchy:** Document alone; empty left draws attention to it.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0423); map slides in left (EP0424). Entry EP0423, exit EP0424.
- **Narration (ASR, unverified):** Mortgage rates are priced
- **Story function (INFERRED):** Names the instrument bought (ASR 'Mortgage rates are priced').
- **Continuity:** Same document in S0308, S0324 etc.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0308 — f12947-12964 (539.500-540.208 s, 18 frames, 0.75 s) — shot SH122 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0424.jpg; entry EP0424, exit EP0425; second review: OK
- **Objects/placement (OBSERVED):** Map character with eyes lower-left to centre (x .02-.58, y .1-.95); orange circle with white percent sign on its east side (x .43-.5, y .55-.7); MORTGAGE document right (x .64-.89).
- **Background:** Flat near-white canvas.
- **Illustration:** Green map, orange badge flat with white percent mark; same document.
- **Typography:** Hand-lettered red heading on paper.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.639 #48a150:0.210 #e6e0c7:0.080 #090f07:0.056 #bc7159:0.015
- **Hierarchy:** Map first, orange badge accent, doc.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Map slides in (EP0424); cut to logo (EP0425). Entry EP0424, exit EP0425.
- **Narration (ASR, unverified):** those bonds,
- **Story function (INFERRED):** Rates tied to bonds (ASR).
- **Continuity:** Map from S0296, doc from S0307.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0309 — f12965-12975 (540.250-540.667 s, 11 frames, 0.46 s) — shot SH123 (inferred) — F9 full-bleed drawn scene
- **Evidence:** frames/ep_stable/e0425.jpg; entry EP0425, exit EP0426; second review: MINOR
- **Objects/placement (OBSERVED):** Wordmark of a lender with roof glyph above it, teal to green gradient lettering, centre-right (x .27-.76, y .25-.45); rest blank.
- **Background:** Flat near-white canvas.
- **Illustration:** Vector logo graphic (not hand-drawn).
- **Typography:** Rounded geometric sans, about 12% height, teal and lime.
- **Readable text:** Freddie Mac
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.969 #1daed6:0.015 #8dc549:0.010 #97e1f0:0.003 #c6e5a3:0.003
- **Hierarchy:** Only object.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0425); second logo added (EP0426). Entry EP0425, exit EP0426.
- **Narration (ASR, unverified):** so a buyer
- **Story function (INFERRED):** Names the buyer of bonds (ASR).
- **Continuity:** Logo reappears in S0310-S0311.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0310 — f12976-12994 (540.708-541.458 s, 19 frames, 0.79 s) — shot SH123 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0426.jpg; entry EP0426, exit EP0427; second review: OK
- **Objects/placement (OBSERVED):** Teal-green wordmark upper (x .27-.76, y .25-.45); second logo below: circular house emblem plus dark navy serif wordmark (x .24-.76, y .58-.75).
- **Background:** Flat near-white canvas.
- **Illustration:** Vector logos.
- **Typography:** Rounded sans and a serif, both about 10-12% height.
- **Readable text:** Freddie Mac; Fannie Mae
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.950 #1eafd7:0.015 #203844:0.014 #8bbd56:0.013 #abcfcb:0.009
- **Hierarchy:** Top logo first by colour, then lower one.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive (EP0426); logos shift left (EP0427). Entry EP0426, exit EP0427.
- **Narration (ASR, unverified):** buyer that size pushes
- **Story function (INFERRED):** Two mortgage buyers named (ASR).
- **Continuity:** Continues S0309/S0311.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0311 — f13024-13026 (542.708-542.792 s, 3 frames, 0.12 s) — shot SH123 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0427.jpg; entry EP0427, exit EP0428; second review: MINOR
- **Objects/placement (OBSERVED):** Both logos shifted left (x .15-.64); orange percent badge appears at right (x .74-.88, y .6-.8) in a 3-frame flicker.
- **Background:** Flat near-white canvas.
- **Illustration:** Orange circle with white percent, thick outline.
- **Typography:** Rounded teal-green sans wordmark and a dark navy serif wordmark, each about 10% height; white percent sign in the badge about 8% height.
- **Readable text:** Freddie Mac; Fannie Mae
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.929 #212d35:0.020 #99bc6c:0.019 #d5804e:0.017 #27b1d7:0.016
- **Hierarchy:** Badge pop catches the eye.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Motion from EP0427; hard cut to post text (EP0428). 3 frames: animation settling frame. Entry EP0427, exit EP0428.
- **Narration (ASR, unverified):** —
- **Story function (INFERRED):** Rates reference (inferred).
- **Continuity:** Same elements as S0310.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0312 — f13027-13041 (542.833-543.417 s, 15 frames, 0.62 s) — shot SH124 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0428.jpg; entry EP0428, exit EP0429; second review: OK
- **Objects/placement (OBSERVED):** Small tall block of social-post text centred (x .36-.64, y .14-.86) with avatar and name header at top, tiny dark text.
- **Background:** White post screenshot on off-white canvas.
- **Illustration:** Screenshot, black sans on white.
- **Typography:** Social UI sans, about 1.2% height lines, black.
- **Readable text:** none
- **Unreadable/uncertain text:** post body text too small; header name tiny
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #e9e9e9:0.029 #929191:0.018 #c1c0c0:0.017 #5f5e5e:0.016
- **Hierarchy:** Text block as one grey column.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0428); caricature added (EP0429). Entry EP0428, exit EP0429.
- **Narration (ASR, unverified):** The Truth Social
- **Story function (INFERRED):** Shows the announcement post (ASR 'The Truth Social Post').
- **Continuity:** Same post in S0313, S0314, S0330-S0332.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0313 — f13042-13049 (543.458-543.750 s, 8 frames, 0.33 s) — shot SH124 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0429.jpg; entry EP0429, exit EP0430; second review: OK
- **Objects/placement (OBSERVED):** Post text block left-centre (x .36-.64) same as S0312; angry caricature right (x .7-.91, y .35-1.0): orange face, scowling brows, blond swept hair, red tie, grey suit, holds phone at lower left.
- **Background:** White post over off-white canvas.
- **Illustration:** Caricature in flat orange skin, thick outlines, angry brow lines.
- **Typography:** Tiny social sans.
- **Readable text:** none
- **Unreadable/uncertain text:** post body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.885 #b3b3b3:0.031 #74605f:0.029 #0c0605:0.028 #cea066:0.028
- **Hierarchy:** Caricature face and red tie first, then the text.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry (EP0429); zoom into the post (EP0430). Entry EP0429, exit EP0430.
- **Narration (ASR, unverified):** Social Post
- **Story function (INFERRED):** Speaker posting the announcement (inferred).
- **Continuity:** Caricature reused S0314, S0341.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0314 — f13065-13187 (544.417-549.500 s, 123 frames, 5.12 s) — shot SH124 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0430.jpg; entry EP0430, exit EP0432; second review: MINOR
- **Objects/placement (OBSERVED):** Enlarged post text left (x .1-.63, y .06-.83) in big black type; caricature right (x .7-.91, y .4-1.0); orange marker highlight over two middle lines; small handwritten caption at lower right of the text.
- **Background:** White text over off-white canvas.
- **Illustration:** Highlight orange; caricature same.
- **Typography:** Social sans about 3% height, black, with orange marker highlight; small black handwritten caption about 1.5% height below the text.
- **Readable text:** "it is now worth many times that amount - AN ABSOLUTE FORTUNE - and has $200 BILLION DOLLARS IN CASH"; "BUY $200 BILLION DOLLARS IN MORTGAGE BONDS"; "MAKE AMERICA GREAT AGAIN!"; small handwritten caption: why is he SCREAMING
- **Unreadable/uncertain text:** handwritten caption (appears at EP0431)
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.838 #141111:0.049 #b59a78:0.047 #5f4e4e:0.035 #c9c9c9:0.031
- **Hierarchy:** Highlighted lines then caricature.
- **Camera/motion:** ZOOM (EP0430) into the text; then static; **entry/exit:** Zoomed from S0313 (EP0430); highlight (EP0431); cut to chalkboard (EP0432). Entry EP0430, exit EP0432.
- **Narration (ASR, unverified):** announcing it said, buy $200 billion in mortgage bonds, this will drive mortgage rates down,
- **Story function (INFERRED):** Reads the quoted post aloud (ASR).
- **Continuity:** Text from S0312-S0313 zoomed.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0121 (HIGHLIGHT_ADD, f13174) An orange marker highlight appears over the middle lines of the post text (centre) and a small handwritten caption appears at lower right of the text block beside the caricature.

## S0315 — f13188-13209 (549.542-550.417 s, 22 frames, 0.92 s) — shot SH125 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0432.jpg; entry EP0432, exit EP0433; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter left with pointer (x .08-.34, y .1-.95); empty green chalkboard in brown frame right (x .47-.98, y .1-.62).
- **Background:** Flat near-white canvas.
- **Illustration:** Chalkboard flat green with thick brown frame; presenter smiling.
- **Typography:** none yet
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.615 #38843f:0.195 #6f534a:0.084 #060504:0.072 #efd1b7:0.034
- **Hierarchy:** Board is big saturated rectangle; presenter second.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0432); text appears (EP0433). Entry EP0432, exit EP0433.
- **Narration (ASR, unverified):** and for a while, it
- **Story function (INFERRED):** Setup for 'it worked' (ASR).
- **Continuity:** Board continues S0316.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0316 — f13210-13231 (550.458-551.333 s, 22 frames, 0.92 s) — shot SH125 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0433.jpg; entry EP0433, exit EP0434; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter shocked open-mouth left (x .05-.34); chalkboard right (x .38-.95, y .1-.75) with white handwriting.
- **Background:** Flat near-white canvas.
- **Illustration:** Presenter mouth open pink oval; board green.
- **Typography:** White hand-lettered, about 12% height, centred on board.
- **Readable text:** It worked!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.623 #38843f:0.183 #71544b:0.086 #070504:0.073 #ead0b7:0.034
- **Hierarchy:** White text on green first, then presenter's face.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Text appears (EP0433); full replace (EP0434). Entry EP0433, exit EP0434.
- **Narration (ASR, unverified):** it worked.
- **Story function (INFERRED):** Payoff line (ASR 'it worked').
- **Continuity:** Continues S0315.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0317 — f13232-13258 (551.375-552.458 s, 27 frames, 1.12 s) — shot SH126 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0434.jpg; entry EP0434, exit EP0435; second review: OK
- **Objects/placement (OBSERVED):** Press-release page (x .07-.63, y .07-.98): navy top bar, white nav, teal banner with headline, boxed PDF link, body text, 'News Facts' list; cropped bottom.
- **Background:** White page on off-white canvas.
- **Illustration:** Screenshot.
- **Typography:** Web sans; headline about 4% white on teal; body about 1.2%.
- **Readable text:** Mortgage Rates Drop Below 6% for the First Time in 3.5 Years
- **Unreadable/uncertain text:** body paragraphs, News Facts bullets
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.773 #0c7e9e:0.142 #bfd1d3:0.031 #071e41:0.029 #879d9a:0.025
- **Hierarchy:** Teal banner headline first.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0434); label and doc added (EP0435). Entry EP0434, exit EP0435.
- **Narration (ASR, unverified):** By late February, the
- **Story function (INFERRED):** Evidence for the sub-6 percent claim (ASR).
- **Continuity:** Page reused S0318.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0318 — f13259-13370 (552.500-557.125 s, 112 frames, 4.67 s) — shot SH126 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0435.jpg; entry EP0435, exit EP0436; second review: OK
- **Objects/placement (OBSERVED):** Press release left (x .07-.63) with green highlight over 'Mortg' and dateline; handwritten '30-year' label top right (x .72-.9, y .22-.29); MORTGAGE document right (x .72-.9, y .39-.78).
- **Background:** White page and off-white canvas.
- **Illustration:** Green highlight marker.
- **Typography:** Web sans plus handwritten black label.
- **Readable text:** Mortgage Rates Drop Below 6% for the First Time in 3.5 Years; 30-year; MORTGAGE
- **Unreadable/uncertain text:** body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.703 #0c7e9d:0.141 #d7dbce:0.075 #0a1b2c:0.047 #879f8b:0.035
- **Hierarchy:** Banner, then label and doc.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive (EP0435); replaced by frowning presenter (EP0436). Entry EP0435, exit EP0436.
- **Narration (ASR, unverified):** the 30 -year mortgage dipped under 6 % for the first time in three and a half years, but
- **Story function (INFERRED):** Labels the rate type (ASR).
- **Continuity:** Same page as S0317.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0319 — f13371-13398 (557.167-558.292 s, 28 frames, 1.17 s) — shot SH127 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0436.jpg; entry EP0436, exit EP0437; second review: MINOR
- **Objects/placement (OBSERVED):** Frowning presenter alone at centre-left (x .41-.58, y .15-.93) with drooped arms.
- **Background:** Flat near-white canvas.
- **Illustration:** Peach head, spiky hair, downturned mouth, dot eyes, thin body.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.032 #080504:0.011 #928c88:0.002 #4b4641:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0436); chart cut (EP0437). Entry EP0436, exit EP0437.
- **Narration (ASR, unverified):** but it didn't last.
- **Story function (INFERRED):** Disappointment beat (ASR 'but it didn't last').
- **Continuity:** Presenter style same as S0342.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0320 — f13399-13413 (558.333-558.917 s, 15 frames, 0.62 s) — shot SH128 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0437.jpg; entry EP0437, exit EP0439; second review: OK
- **Objects/placement (OBSERVED):** Line-chart screenshot in a light-blue panel (x .07-.96, y .2-.8): blue rising line, y axis 5.8-7.2, x axis 2025-10 to 2026-09, small source note and Fullscreen button at bottom; hover crosshair with tooltip steps right in the last frames.
- **Background:** Light-blue chart panel on off-white canvas.
- **Illustration:** Screenshot, thin blue line, grey grid.
- **Typography:** Chart UI sans, about 1.2% height labels, dark grey; title small bold.
- **Readable text:** 30-Year Fixed Rate Mortgage Average in the United States (title, small)
- **Unreadable/uncertain text:** axis ticks, tooltip values, source note
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.792 #eaf2f8:0.168 #cdd2d6:0.027 #97a7b3:0.009 #586c7b:0.004
- **Hierarchy:** Rising blue line then the crosshair.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0437); hover crosshair (EP0438, EP0439); news cards slide in. Entry EP0437, exit EP0439.
- **Narration (ASR, unverified):** Rates drifted back
- **Story function (INFERRED):** Shows rates rising back (ASR 'Rates drifted back').
- **Continuity:** Chart reused in S0321-S0323.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state motion intervals:** EP0438

## S0321 — f13459-13465 (560.833-561.083 s, 7 frames, 0.29 s) — shot SH128 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0439.jpg; entry EP0439, exit EP0440; second review: OK
- **Objects/placement (OBSERVED):** Chart panel (x .08-.97, y .2-.8) with three dark-mode news cards overlaid: top-left card (x .08-.5, y .17-.36) with thumbnail, right-middle card (x .52-.93, y .3-.5) with seal image, lower-right card (x .52-.93, y .55-.77).
- **Background:** Chart panel plus near-black cards on off-white canvas.
- **Illustration:** Cards dark grey with white and light-blue text and small photo thumbnails.
- **Typography:** Dark-UI sans, headlines about 1.8%, white; body grey about 1%.
- **Readable text:** Fed Raises Rates in First Major Step by Warsh to Contain Inflation; Fed Raises Interest Rates for First Time Since 2023; Fed raises interest rates for first time since 2023, defying Trump as inflation mounts
- **Unreadable/uncertain text:** card body lines and timestamps
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.631 #202228:0.190 #e6eef4:0.131 #585b65:0.024 #9198a4:0.023
- **Hierarchy:** Dark cards pull the eye first, chart behind.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Cards appear at end of EP0439; more added next (EP0440). Entry EP0439, exit EP0440.
- **Narration (ASR, unverified):** week,
- **Story function (INFERRED):** Fed rate-hike headlines (ASR 'the Fed hiked').
- **Continuity:** Card style reused S0325-S0329.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0322 — f13466-13471 (561.125-561.333 s, 6 frames, 0.25 s) — shot SH128 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0440.jpg; entry EP0440, exit EP0441; second review: MINOR
- **Objects/placement (OBSERVED):** Chart panel shifted up-left (x .03-.93, y .1-.8) with four dark news cards: NYT-style top-left, business-news left-middle (x .07-.5, y .39-.58), right-top, right-lower.
- **Background:** Chart plus dark cards.
- **Illustration:** Same as S0321.
- **Typography:** Dark-mode UI sans; headlines about 1.8% height in white, body lines tiny grey.
- **Readable text:** Fed Raises Rates in First Major Step by Warsh to Contain Inflation; Federal Reserve hikes interest rates for first time since 2023 amid stubborn inflation
- **Unreadable/uncertain text:** card bodies
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfd:0.567 #202229:0.255 #e7eff5:0.119 #585b64:0.031 #9298a2:0.028
- **Hierarchy:** Cluster of dark cards.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive card (EP0440); another (EP0441). Entry EP0440, exit EP0441.
- **Narration (ASR, unverified):** week, the
- **Story function (INFERRED):** Adds weight of coverage (inferred).
- **Continuity:** Continues S0321, S0323.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0323 — f13472-13512 (561.375-563.042 s, 41 frames, 1.71 s) — shot SH128 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0441.jpg; entry EP0441, exit EP0442; second review: MINOR
- **Objects/placement (OBSERVED):** Same as S0322 plus fifth card bottom-left (x .07-.5, y .66-.82): 'Fed Delivers First Rate Hike in Years With Unanimous Vote'.
- **Background:** Chart plus dark cards.
- **Illustration:** Same.
- **Typography:** Dark-mode UI sans; headlines about 1.8% height in white, body lines tiny grey.
- **Readable text:** Fed Delivers First Rate Hike in Years With Unanimous Vote
- **Unreadable/uncertain text:** other card text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfc:0.621 #202128:0.303 #464853:0.028 #71737c:0.025 #9da2ad:0.022
- **Hierarchy:** Five-card pile.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive (EP0441); replaced by presenter scene (EP0442). Entry EP0441, exit EP0442.
- **Narration (ASR, unverified):** the Fed hiked the policy rate.
- **Story function (INFERRED):** Complete the media pile (ASR 'the Fed hiked the policy rate').
- **Continuity:** Continues S0322.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0324 — f13513-13519 (563.083-563.333 s, 7 frames, 0.29 s) — shot SH129 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0442.jpg; entry EP0442, exit EP0443; second review: OK
- **Objects/placement (OBSERVED):** Smiling shrugging presenter left (x .12-.29, y .45-.95, cropped bottom); MORTGAGE document right (x .51-.69, y .5-.92).
- **Background:** Flat near-white canvas.
- **Illustration:** Peach head, small smile, arms out in shrug.
- **Typography:** Red hand-lettered title.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.891 #eedbc1:0.072 #080604:0.024 #b39e94:0.006 #71504a:0.006
- **Hierarchy:** Presenter then document.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0442); card appears (EP0443). Entry EP0442, exit EP0443.
- **Narration (ASR, unverified):** Now
- **Story function (INFERRED):** 'Now' pivot to current rates (ASR).
- **Continuity:** Layout continues S0325-S0329.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0325 — f13520-13523 (563.375-563.500 s, 4 frames, 0.17 s) — shot SH129 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0443.jpg; entry EP0443, exit EP0444; second review: OK
- **Objects/placement (OBSERVED):** Presenter lower-left (x .12-.29); mortgage document lower centre (x .51-.69); AP-style card with house photo, top-right-ish (x .37-.94, y .15-.42).
- **Background:** Dark card over off-white canvas.
- **Illustration:** Dark charcoal card with white headline and thumbnail; doodles as before.
- **Typography:** Dark-UI sans headline about 2% white; body grey small.
- **Readable text:** US mortgage rates brush 7%, weighing on buyers, sellers and further straining a bleak housing market
- **Unreadable/uncertain text:** card body line and age stamp
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.739 #1d1e23:0.149 #eddac1:0.074 #615a5e:0.021 #9d999c:0.017
- **Hierarchy:** Dark card top, then presenter and document.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive card (EP0443); swapped (EP0444). Very short state, a flicker in a rapid headline montage. Entry EP0443, exit EP0444.
- **Narration (ASR, unverified):** Now mortgage
- **Story function (INFERRED):** Rapid headline montage reinforcing rates near 7 percent (ASR 'Now mortgage rates are...').
- **Continuity:** Same layout as S0324-S0329; only the card changes.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0326 — f13524-13528 (563.542-563.708 s, 5 frames, 0.21 s) — shot SH129 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0444.jpg; entry EP0444, exit EP0445; second review: OK
- **Objects/placement (OBSERVED):** Presenter lower-left (x .12-.29); mortgage document lower centre (x .51-.69); WSJ-style card (x .37-.97, y .15-.42), thumbnail of house.
- **Background:** Dark card over off-white canvas.
- **Illustration:** Dark charcoal card with white headline and thumbnail; doodles as before.
- **Typography:** Dark-UI sans headline about 2% white; body grey small.
- **Readable text:** The New Rules for Selling Your Home With Mortgage Rates Near 7%
- **Unreadable/uncertain text:** card body line and age stamp
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.739 #1d1e23:0.153 #eddac0:0.074 #685d5e:0.017 #a6a0a0:0.017
- **Hierarchy:** Dark card top, then presenter and document.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Card swap (EP0444); swapped again (EP0445). Very short state, a flicker in a rapid headline montage. Entry EP0444, exit EP0445.
- **Narration (ASR, unverified):** mortgage
- **Story function (INFERRED):** Rapid headline montage reinforcing rates near 7 percent (ASR 'Now mortgage rates are...').
- **Continuity:** Same layout as S0324-S0329; only the card changes.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0327 — f13529-13533 (563.750-563.917 s, 5 frames, 0.21 s) — shot SH129 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0445.jpg; entry EP0445, exit EP0446; second review: OK
- **Objects/placement (OBSERVED):** Presenter lower-left (x .12-.29); mortgage document lower centre (x .51-.69); Consumer-affairs card shifted to the right (x .37-.99, y .17-.38) with yard-sign photo.
- **Background:** Dark card over off-white canvas.
- **Illustration:** Dark charcoal card with white headline and thumbnail; doodles as before.
- **Typography:** Dark-UI sans headline about 2% white; body grey small.
- **Readable text:** Selling a home just got harder as mortgage rates hit 7%
- **Unreadable/uncertain text:** card body line and age stamp
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.759 #1d1d22:0.133 #eddac1:0.074 #a5a09a:0.017 #6a5e5c:0.016
- **Hierarchy:** Dark card top, then presenter and document.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Card swap (EP0445); swapped again (EP0446). Very short state, a flicker in a rapid headline montage. Entry EP0445, exit EP0446.
- **Narration (ASR, unverified):** mortgage rates
- **Story function (INFERRED):** Rapid headline montage reinforcing rates near 7 percent (ASR 'Now mortgage rates are...').
- **Continuity:** Same layout as S0324-S0329; only the card changes.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0328 — f13534-13540 (563.958-564.208 s, 7 frames, 0.29 s) — shot SH129 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0446.jpg; entry EP0446, exit EP0447; second review: OK
- **Objects/placement (OBSERVED):** Presenter lower-left (x .12-.29); mortgage document lower centre (x .51-.69); Local-news card (x .36-.94, y .15-.42).
- **Background:** Dark card over off-white canvas.
- **Illustration:** Dark charcoal card with white headline and thumbnail; doodles as before.
- **Typography:** Dark-UI sans headline about 2% white; body grey small.
- **Readable text:** Struggling U.S. homebuyers, and market, face new hurdles as mortgage rates brush 7%
- **Unreadable/uncertain text:** card body line and age stamp
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.733 #1d1e23:0.158 #eddac1:0.074 #635c5e:0.020 #a09c9f:0.016
- **Hierarchy:** Dark card top, then presenter and document.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Card swap (EP0446); swapped again (EP0447). Very short state, a flicker in a rapid headline montage. Entry EP0446, exit EP0447.
- **Narration (ASR, unverified):** rates are
- **Story function (INFERRED):** Rapid headline montage reinforcing rates near 7 percent (ASR 'Now mortgage rates are...').
- **Continuity:** Same layout as S0324-S0329; only the card changes.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0329 — f13541-13578 (564.250-565.792 s, 38 frames, 1.58 s) — shot SH129 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0447.jpg; entry EP0447, exit EP0449; second review: OK
- **Objects/placement (OBSERVED):** Presenter lower-left; mortgage document lower centre; WSJ-style card top (x .37-.94, y .15-.42); red hand-written 7% appears right of the document (x .67-.75, y .5-.63).
- **Background:** Dark card over off-white.
- **Illustration:** Red marker 7% with hand-lettered look.
- **Typography:** Dark-UI sans plus red handwritten numerals about 12%.
- **Readable text:** The Stagnant Housing Market Is About to Face a 7% Mortgage; 7%
- **Unreadable/uncertain text:** card body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.742 #1d1e22:0.152 #eddbc0:0.073 #635b5a:0.017 #a19da0:0.016
- **Hierarchy:** Red 7% pops last.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Card swap (EP0447); micro 7% (EP0448); cut to post (EP0449). Entry EP0447, exit EP0449.
- **Narration (ASR, unverified):** are sitting around 7%. It
- **Story function (INFERRED):** Number reveal: rates around 7 percent (ASR).
- **Continuity:** Same layout as S0324-S0328.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0122 (ADDITIVE_ENTRY, f13557) A large red handwritten '7%' appears to the right of the mortgage document (centre right).

## S0330 — f13579-13616 (565.833-567.375 s, 38 frames, 1.58 s) — shot SH130 (inferred) — F8 dark-UI capture
- **Evidence:** frames/ep_stable/e0449.jpg; entry EP0449, exit EP0450; second review: MINOR
- **Objects/placement (OBSERVED):** Tall social-post block centred-left (x .16-.45, y .12-.89), tiny black text with header.
- **Background:** White post on off-white.
- **Illustration:** Screenshot.
- **Typography:** Social sans about 1% lines.
- **Readable text:** none
- **Unreadable/uncertain text:** entire post body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.930 #dcdcdc:0.023 #7d7c7d:0.016 #aeadad:0.016 #555454:0.015
- **Hierarchy:** Single block.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0449); house added (EP0450). Entry EP0449, exit EP0450.
- **Narration (ASR, unverified):** It was a temporary solution to
- **Story function (INFERRED):** Recalls earlier post (ASR 'It was a temporary solution').
- **Continuity:** Same as S0312.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0331 — f13617-13648 (567.417-568.708 s, 32 frames, 1.33 s) — shot SH130 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0450.jpg; entry EP0450, exit EP0451; second review: MINOR
- **Objects/placement (OBSERVED):** Post block left (x .16-.45); weathered brown house with red roof and blue window right (x .57-.82, y .26-.83).
- **Background:** White post on off-white.
- **Illustration:** House flat brown wood with outlines, red roof, small blue window.
- **Typography:** Tiny post text.
- **Readable text:** none
- **Unreadable/uncertain text:** post text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.864 #8e8b78:0.052 #60504e:0.028 #0a0605:0.028 #c5c7c7:0.027
- **Hierarchy:** House is big colourful form.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive (EP0450); presenter added (EP0451). Entry EP0450, exit EP0451.
- **Narration (ASR, unverified):** to a structural problem, and
- **Story function (INFERRED):** 'Structural problem' symbol (ASR).
- **Continuity:** House new here.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0332 — f13649-13689 (568.750-570.417 s, 41 frames, 1.71 s) — shot SH130 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0451.jpg; entry EP0451, exit EP0452; second review: MINOR
- **Objects/placement (OBSERVED):** Post block left (x .16-.45); house right (x .57-.82); worried presenter overlapping post at centre-left (x .22-.39, y .3-1.0).
- **Background:** White post.
- **Illustration:** Frowning peach head over text.
- **Typography:** Tiny post text.
- **Readable text:** none
- **Unreadable/uncertain text:** post text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.825 #e5d0be:0.057 #908d79:0.052 #0a0605:0.040 #5f4c49:0.025
- **Hierarchy:** Face over text.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive (EP0451); transition to lectern scene (EP0452). Entry EP0451, exit EP0452.
- **Narration (ASR, unverified):** and it wasn't the first attempt.
- **Story function (INFERRED):** Worry about the 'first attempt' (ASR).
- **Continuity:** Continues S0331.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0333 — f13713-13766 (571.417-573.625 s, 54 frames, 2.25 s) — shot SH131 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0452.jpg; entry EP0452, exit EP0457; second review: OK
- **Objects/placement (OBSERVED):** Social header (x .11-.3, y .02-.06); presidents card (x .11-.55, y .07-.83) with navy header, two columns each with portrait; caricature at lectern right (x .7-.97, y .35-1.0), striped flag, brown lectern bottom.
- **Background:** White card on off-white canvas.
- **Illustration:** Caricature flat orange face, blond hair, red tie, grey suit, one arm out.
- **Typography:** Card sans bold, header about 4% white on navy; subheads about 2.5%; captions about 1.5%.
- **Readable text:** Great American Presidents; 30-Year Mortgage; 50-Year Mortgage; President Roosevelt; President Trump; Donald J. Trump @realDonaldTrump
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.614 #4f433e:0.178 #120e11:0.126 #c39f7c:0.059 #b1272b:0.023
- **Hierarchy:** Card header then portraits, caricature.
- **Camera/motion:** STATIC 2D; card slides in at EP0452; **entry/exit:** Card slides in (EP0452); arm-pose loop (EP0453-0456); small head peeks (EP0457). Entry EP0452, exit EP0457.
- **Narration (ASR, unverified):** Trump posted an image of Franklin Roosevelt,
- **Story function (INFERRED):** Meme post comparing mortgages (ASR).
- **Continuity:** Same card S0334-S0335.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0123 (POSE_SWAP, f13723) Caricature's gesturing arms (right side, lower right of card) swap to the alternate pose; sleeves and hands redrawn.; EVI0124 (POSE_SWAP, f13734) Caricature's arms toggle to the other gesture pose again (arm position at lower right changes).; EVI0125 (POSE_SWAP, f13745) Caricature's arm/hand shifts to the alternate talking pose near lower right; card unchanged.; EVI0126 (POSE_SWAP, f13756) Another arm-pose toggle on the caricature (hands/forearms, right side); rest static.

## S0334 — f13770-13863 (573.792-577.667 s, 94 frames, 3.92 s) — shot SH131 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0457.jpg; entry EP0457, exit EP0467; second review: MINOR
- **Objects/placement (OBSERVED):** Card (x .11-.55, y .1-.65); caricature right; small presenter head peeking far left (x 0-.1, y .38-.6); small paper at lower left appears midway.
- **Background:** White card.
- **Illustration:** Same style.
- **Typography:** Bold sans card header about 4% white on navy; column subheads about 2.5% black; captions about 1.5%; handle text tiny grey.
- **Readable text:** Great American Presidents; 30-Year Mortgage; 50-Year Mortgage; President Roosevelt; President Trump
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfafa:0.609 #4f433e:0.179 #120e11:0.128 #c3a07d:0.060 #b1272c:0.024
- **Hierarchy:** Card, caricature, small peeking head.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Entry EP0457; many arm toggles; exit EP0467. Entry EP0457, exit EP0467.
- **Narration (ASR, unverified):** whose administration introduced the 30 -year mortgage in the United States,
- **Story function (INFERRED):** Narration on the image (ASR).
- **Continuity:** Continues S0333.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0127 (POSE_SWAP, f13778) Caricature's arms toggle gesture pose (lower right); small peeking presenter stays at left.; EVI0128 (POSE_SWAP, f13789) Caricature's arms toggle gesture pose again, about 11 frames after the last toggle.; EVI0129 (POSE_SWAP, f13800) Caricature arm pose toggles; peeking presenter and card static.; EVI0130 (ADDITIVE_ENTRY, f13807) A small paper document with red heading appears at lower left under the peeking presenter; caricature's arms also change pose.; EVI0131 (POSE_SWAP, f13811) Caricature's arms toggle gesture pose; small document and presenter static at left.; EVI0132 (POSE_SWAP, f13822) Caricature's arms toggle gesture pose at right; left-side props unchanged.; EVI0133 (POSE_SWAP, f13833) Another caricature arm-pose toggle on the right; nothing else moves.; EVI0134 (POSE_SWAP, f13844) Caricature arm pose toggles; small presenter and document remain at left.; EVI0135 (POSE_SWAP, f13855) Caricature arm pose toggles again just before the small props exit.

## S0335 — f13867-13928 (577.833-580.375 s, 62 frames, 2.58 s) — shot SH131 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0467.jpg; entry EP0467, exit EP0473; second review: OK
- **Objects/placement (OBSERVED):** Card moved to y .1-.65; caricature right; small left props gone; tiny pink handwriting right of card header (x .57-.62, y .1-.12).
- **Background:** White card.
- **Illustration:** Same.
- **Typography:** Tiny pink handwriting.
- **Readable text:** Great American Presidents; I love me (tiny pink)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.614 #60423c:0.178 #070304:0.076 #26222c:0.074 #c49f7b:0.058
- **Hierarchy:** Card, caricature.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Props exit (EP0467); pink text micro (EP0470); hard cut (EP0473). Entry EP0467, exit EP0473.
- **Narration (ASR, unverified):** next to himself labeled 50 -year mortgage.
- **Story function (INFERRED):** Mockery tone (inferred).
- **Continuity:** Continues S0334.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0136 (POSE_SWAP, f13877) Caricature's arms toggle gesture pose; left side now empty.; EVI0137 (POSE_SWAP, f13888) Caricature's arm pose toggles again at lower right.; EVI0138 (ADDITIVE_ENTRY, f13899) Tiny pink handwritten text ('I love me') appears right of the card header, near the caricature's head; arm pose toggles as well.; EVI0139 (POSE_SWAP, f13910) Caricature's arms toggle gesture pose; tiny pink text stays.; EVI0140 (POSE_SWAP, f13921) Last arm-pose toggle of the talking loop before the cut; tiny pink text stays.

## S0336 — f13929-13991 (580.417-583.000 s, 63 frames, 2.62 s) — shot SH132 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0473.jpg; entry EP0473, exit EP0474; second review: OK
- **Objects/placement (OBSERVED):** News article (x .1-.66, y .06-.95): masthead, bold headline, deck text, wide photo of reporters under umbrellas; presenter with newspaper at right (x .75-1.0, y .5-1.0).
- **Background:** White article on off-white.
- **Illustration:** Photo realistic; presenter peach head holding newspaper marked NEWS.
- **Typography:** Masthead sans-serif spaced; headline about 3% bold.
- **Readable text:** POLITICO; Pulte backs away from 50-year mortgage
- **Unreadable/uncertain text:** deck text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.551 #120e15:0.143 #423740:0.122 #886d75:0.096 #dac9b3:0.088
- **Hierarchy:** Photo then headline.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0473); scrolls (EP0474). Entry EP0473, exit EP0474.
- **Narration (ASR, unverified):** By January, when the head of the Federal Housing Finance
- **Story function (INFERRED):** Evidence a policy was dropped (ASR).
- **Continuity:** Presenter and newspaper reused S0337.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0337 — f14013-14086 (583.917-586.958 s, 74 frames, 3.08 s) — shot SH132 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0474.jpg; entry EP0474, exit EP0475; second review: MINOR
- **Objects/placement (OBSERVED):** Scrolled article (x .1-.66): photo bottom strip, caption, byline, body paragraphs; presenter with newspaper lower right (x .75-1.0, y .5-1.0).
- **Background:** White article.
- **Illustration:** Same.
- **Typography:** News serif/sans body about 1.5%.
- **Readable text:** "I think we have other priorities," Pulte told reporters; Federal Housing Director Bill Pulte on Friday signaled...
- **Unreadable/uncertain text:** caption, byline
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.725 #daccb5:0.088 #130f14:0.088 #463d42:0.062 #857c7a:0.037
- **Hierarchy:** Pull quote.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Scroll done (EP0474); hard replace (EP0475). Entry EP0474, exit EP0475.
- **Narration (ASR, unverified):** asked about it, he said, I think we have other priorities.
- **Story function (INFERRED):** Reads the quote (ASR).
- **Continuity:** Continues S0336.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0338 — f14087-14119 (587.000-588.333 s, 33 frames, 1.38 s) — shot SH133 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0475.jpg; entry EP0475, exit EP0476; second review: OK
- **Objects/placement (OBSERVED):** Trade article (x .2-.8, y .15-.85): dark header, nav, headline at left, B/W photo with magnifier over a house at right (x .5-.8, y .3-.8).
- **Background:** Grey-beige article panel on off-white.
- **Illustration:** B/W photo with pinkish cutout border.
- **Typography:** Bold sans headline about 3.5%.
- **Readable text:** Trump pauses 50-year mortgage plan, eyes 401(k)s for down payments; HOUSINGWIRE
- **Unreadable/uncertain text:** body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.601 #e0dedb:0.230 #1a1c1e:0.107 #55595a:0.033 #9d9d9d:0.029
- **Hierarchy:** Headline then photo.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0475); presenter adds (EP0476). Entry EP0475, exit EP0476.
- **Narration (ASR, unverified):** Then in mid -January,
- **Story function (INFERRED):** Names the next idea (ASR).
- **Continuity:** Same article S0339-S0340.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0339 — f14120-14214 (588.375-592.292 s, 95 frames, 3.96 s) — shot SH133 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0476.jpg; entry EP0476, exit EP0477; second review: MINOR
- **Objects/placement (OBSERVED):** Same article; yellow highlight on 'The White House is reportedly preparing...'; worried presenter with pointer lower-left (x .07-.19, y .55-1.0).
- **Background:** Article panel.
- **Illustration:** Yellow marker; frowning peach head.
- **Typography:** Bold sans headline about 3.5% black; body about 1.2% with a yellow marker highlight over the first line.
- **Readable text:** Trump pauses 50-year mortgage plan, eyes 401(k)s for down payments; The White House is reportedly preparing an...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.576 #e1ddd8:0.245 #191b1d:0.112 #565959:0.036 #a09f9b:0.031
- **Hierarchy:** Headline, highlighted lines, presenter.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive presenter (EP0476); 401K paper (EP0477). Entry EP0476, exit EP0477.
- **Narration (ASR, unverified):** the White House floated the idea of letting first -time buyers pull money from their 401k
- **Story function (INFERRED):** 401k idea (ASR).
- **Continuity:** Continues S0338.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0340 — f14215-14299 (592.333-595.833 s, 85 frames, 3.54 s) — shot SH133 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0477.jpg; entry EP0477, exit EP0481; second review: OK
- **Objects/placement (OBSERVED):** Article (x .2-.8, y .15-.85) highlighted; presenter lower-left; 401K paper lower right (x .77-.88, y .6-.9); then piggy bank, cash stack appear bottom right.
- **Background:** Article panel.
- **Illustration:** Piggy pink; cash green.
- **Typography:** Handwritten 401K.
- **Readable text:** 401K; Trump pauses 50-year mortgage plan...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.558 #e2ded8:0.252 #191a1d:0.111 #595b51:0.040 #acae83:0.039
- **Hierarchy:** Paper then icons.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive 401K paper (EP0477); piggy (EP0478); cash (EP0479-0480); hard cut (EP0481). Entry EP0477, exit EP0481.
- **Narration (ASR, unverified):** 401k and their kids' college fund for a down payment.
- **Story function (INFERRED):** College fund and 401k (ASR).
- **Continuity:** Continues S0339.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0141 (ADDITIVE_ENTRY, f14250) A small pink piggy bank appears at bottom right, left of the 401K paper.; EVI0142 (ADDITIVE_ENTRY, f14277) A green banknote appears at lower centre-right, left of the piggy bank.; EVI0143 (ADDITIVE_ENTRY, f14284) A second green banknote is added overlapping the first, forming a small cash stack at lower centre-right.

## S0341 — f14308-14338 (596.208-597.458 s, 31 frames, 1.29 s) — shot SH134 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0481.jpg; entry EP0481, exit EP0483; second review: OK
- **Objects/placement (OBSERVED):** Article (x .13-.65, y .1-.95): magenta serif headline, isometric illustration of man climbing stairs (x .42-.62, y .12-.65), body text; angry caricature right (x .73-.9, y .45-1.0).
- **Background:** White article.
- **Illustration:** Flat orange face, blond hair, red tie.
- **Typography:** Serif headline about 4% magenta.
- **Readable text:** Trump Backs Off From Reported Plan to Let Homebuyers Tap 401(k)s, 529s
- **Unreadable/uncertain text:** body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.790 #e8e0d0:0.100 #b39e87:0.055 #130e0d:0.028 #8f5851:0.027
- **Hierarchy:** Headline.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0481); cursor micro (EP0482); cut (EP0483). Entry EP0481, exit EP0483.
- **Narration (ASR, unverified):** one lasted about a week.
- **Story function (INFERRED):** 'one lasted about a week' (ASR).
- **Continuity:** Caricature S0313.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0144 (OTHER, f14313) Mouse cursor next to the headline's last word changes from a text I-beam to an arrow pointer (upper left of article). No other change.

## S0342 — f14339-14363 (597.500-598.500 s, 25 frames, 1.04 s) — shot SH135 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0483.jpg; entry EP0483, exit EP0484; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling presenter alone centre (x .41-.58, y .1-.88) arms out.
- **Background:** Flat near-white canvas.
- **Illustration:** Same.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f3d2b7:0.032 #070504:0.011 #8d8782:0.002 #45403d:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0483); doc adds (EP0484). Entry EP0483, exit EP0484.
- **Narration (ASR, unverified):** The problem is,
- **Story function (INFERRED):** 'The problem is,' (ASR).
- **Continuity:** Presenter reused.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0343 — f14364-14397 (598.542-599.917 s, 34 frames, 1.42 s) — shot SH135 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0484.jpg; entry EP0484, exit EP0485; second review: MINOR
- **Objects/placement (OBSERVED):** MORTGAGE doc right of centre (x .57-.79, y .19-.69).
- **Background:** Flat near-white canvas.
- **Illustration:** Same.
- **Typography:** Red hand-lettered capitals MORTGAGE about 7% height on the top paper.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.914 #e8e2c8:0.056 #070503:0.019 #794843:0.006 #b79c91:0.005
- **Hierarchy:** Alone.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Additive entry (EP0484); map slides in (EP0485). Entry EP0484, exit EP0485.
- **Narration (ASR, unverified):** each of these solutions is targeted
- **Story function (INFERRED):** 'each of these solutions' (ASR).
- **Continuity:** S0307 doc.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0344 — f14410-14438 (600.458-601.625 s, 29 frames, 1.21 s) — shot SH135 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0485.jpg; entry EP0485, exit EP0486; second review: MINOR
- **Objects/placement (OBSERVED):** Map character at lower left (x 0-.46, y .37-1.0) looking sideways; doc (x .57-.79).
- **Background:** Flat near-white canvas.
- **Illustration:** Same.
- **Typography:** Red hand-lettered capitals MORTGAGE about 7% height on the top paper.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.756 #48a24f:0.138 #e6dfc7:0.060 #080e06:0.036 #84605a:0.010
- **Hierarchy:** Map then doc.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Slides in (EP0485); cut (EP0486). Entry EP0485, exit EP0486.
- **Narration (ASR, unverified):** at the demand side,
- **Story function (INFERRED):** 'demand side' (ASR).
- **Continuity:** S0296 map.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0345 — f14439-14483 (601.667-603.500 s, 45 frames, 1.88 s) — shot SH136 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0486.jpg; entry EP0486, exit EP0488; second review: MINOR
- **Objects/placement (OBSERVED):** Detective presenter centre-left (x .19-.38, y .13-.97) with flat cap and magnifier (x .41-.5); typed text right (x .6-.9, y .47-.55).
- **Background:** Flat near-white canvas.
- **Illustration:** Peach head, deerstalker-style cap, magnifier circle.
- **Typography:** Hand-lettered black about 5%.
- **Readable text:** Let's look at history!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.909 #f2d2b6:0.054 #060403:0.021 #756d5b:0.010 #393633:0.006
- **Hierarchy:** Presenter, then text.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0486); typed (EP0487); exit (EP0488). Entry EP0486, exit EP0488.
- **Narration (ASR, unverified):** and we've run this experiment before. In
- **Story function (INFERRED):** Pivot to historical precedent (ASR).
- **Continuity:** New costume.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state motion intervals:** EP0487

## S0346 — f14507-14519 (604.500-605.000 s, 13 frames, 0.54 s) — shot SH137 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0488.jpg; entry EP0488, exit EP0489; second review: OK
- **Objects/placement (OBSERVED):** Government fact-sheet web page (x .06-.9, y .1-.95): dark-blue banner with seal and nav at top, grey breadcrumb, left sidebar menu (x .08-.28), serif title (x .3-.7, y .45-.7), body text beneath, share icons at right.
- **Background:** White web page on off-white canvas.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Serif title about 5% of height in black; sidebar sans about 1.5% grey; body serif about 1.3%.
- **Readable text:** FACT SHEET: Making Homeownership More Accessible and Sustainable; Briefing Room; January 07, 2015
- **Unreadable/uncertain text:** sidebar items, body paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.825 #345b88:0.079 #dee0e2:0.037 #b3b8bd:0.032 #878a8f:0.027
- **Hierarchy:** Serif title first, then blue banner.
- **Camera/motion:** ZOOM-IN settling (EP0488) then further ZOOM (EP0489); **entry/exit:** Page scales up from EP0488; exits by further zoom (EP0489). Short 13-frame state. Entry EP0488, exit EP0489.
- **Narration (ASR, unverified):** the Federal
- **Story function (INFERRED):** Names a prior-administration precedent (inferred from ASR 'the Federal' / 'the agency').
- **Continuity:** Same page continues zoomed in S0347 and S0348.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0347 — f14557-14559 (606.583-606.667 s, 3 frames, 0.12 s) — shot SH137 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0489.jpg; entry EP0489, exit EP0490; second review: OK
- **Objects/placement (OBSERVED):** Zoomed page: body paragraphs of serif text fill x .0-.88 and share icons (circle with FACEBOOK and EMAIL labels) at right edge (x .9-1.0, y .02-.1); only 3 frames.
- **Background:** White page.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Serif body about 2% black; share labels grey caps small.
- **Readable text:** none
- **Unreadable/uncertain text:** body paragraphs about mortgage reforms; FACEBOOK; EMAIL
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.858 #e5e5e5:0.047 #c7c7c7:0.036 #a5a5a5:0.032 #828282:0.027
- **Hierarchy:** Text block fills frame; no focal point.
- **Camera/motion:** ZOOM/SCROLL in progress; **entry/exit:** Mid-zoom frames of EP0489; exits into presenter slide-in (EP0490). Animation frame of a zoom/scroll. Entry EP0489, exit EP0490.
- **Narration (ASR, unverified):** the agency
- **Story function (INFERRED):** Transitional zoom-in on the page (inferred).
- **Continuity:** Between S0346 and S0348.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0348 — f14586-14836 (607.792-618.208 s, 251 frames, 10.46 s) — shot SH137 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0490.jpg; entry EP0490, exit EP0492; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed page text (x .0-1, y 0-1); yellow highlight on one sentence at upper right (x .3-.88, y .26-.3) that extends rightward; smiling presenter with pointer at lower left (x .08-.32, y .4-1.0), pointer stick crossing the text.
- **Background:** White text page.
- **Illustration:** Peach head, spiky hair, dot eyes, smile, black stick body; pointer dark brown line; highlight lime-yellow marker.
- **Typography:** Serif body about 1.8% black; highlight text same.
- **Readable text:** The Federal Housing Administration (FHA) will reduce annual mortgage insurance premiums
- **Unreadable/uncertain text:** rest of body text, share labels
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.830 #e3d6ca:0.080 #b1b4a8:0.042 #82837d:0.035 #16110f:0.012
- **Hierarchy:** Yellow highlight first, then presenter, then text.
- **Camera/motion:** STATIC 2D after settling; **entry/exit:** Presenter slides in at EP0490; highlight dragged longer at EP0491; hard cut to archive page (EP0492). Longest state, 10.5 s. Entry EP0490, exit EP0492.
- **Narration (ASR, unverified):** mortgages for buyers who can't put much down, cut the insurance premium those buyers pay. For the typical first -time home buyer, that was about a $900 reduction in their annual mortgage payment.
- **Story function (INFERRED):** Evidence that the agency cut the insurance premium (ASR).
- **Continuity:** Presenter + pointer layout reused S0356, S0362.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: text, highlight and presenter from crops and sheets (highlight extension checked at native resolution); INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0145 (HIGHLIGHT_ADD, f14648) The yellow marker highlight on the sentence in the upper paragraph extends a few characters further right (from 'will r' to 'will re'), as if being dragged.

## S0349 — f14837-14856 (618.250-619.042 s, 20 frames, 0.83 s) — shot SH138 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0492.jpg; entry EP0492, exit EP0493; second review: OK
- **Objects/placement (OBSERVED):** Narrow archive news-release page centred (x .28-.72, y .07-.97) with blue outline: seal and 'Archives' title at top, headline in bold caps, dense small paragraphs, footer logo bottom.
- **Background:** White page on off-white canvas.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Serif headline about 1.5% bold; body about 1%.
- **Readable text:** HUD Archives: News Releases; FHA TO REDUCE ANNUAL INSURANCE PREMIUMS
- **Unreadable/uncertain text:** body paragraphs
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.846 #cdcfd3:0.048 #283d66:0.042 #a0a2a6:0.036 #76777d:0.028
- **Hierarchy:** Dark-blue border and header draw the eye.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace at EP0492; zoom-in follows (EP0493). 20 frames. Entry EP0492, exit EP0493.
- **Narration (ASR, unverified):** It was supposed to bring
- **Story function (INFERRED):** The official source of the premium cut (ASR 'mortgages for buyers who can't put much down').
- **Continuity:** Same page zoomed in S0350.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0350 — f14878-14949 (619.958-622.917 s, 72 frames, 3.00 s) — shot SH138 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0493.jpg; entry EP0493, exit EP0494; second review: OK
- **Objects/placement (OBSERVED):** Zoomed release filling frame (x .0-1.0): seal and 'Archives' banner top, release number and date row, bold italic headline, paragraph with teal highlight on '250,000 new' (x .35-.5, y .87-.89).
- **Background:** White page.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Banner serif italic about 6%; headline bold about 2.5%; body about 2%.
- **Readable text:** HUD Archives: News Releases; FHA TO REDUCE ANNUAL INSURANCE PREMIUMS; Reduction to increase credit affordability and reflects improved economic health of FHA; 250,000 new
- **Unreadable/uncertain text:** dateline and body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.752 #c5c9ce:0.092 #334667:0.073 #80838c:0.044 #271a1c:0.040
- **Hierarchy:** Banner and headline, then teal highlight.
- **Camera/motion:** Zoomed in (EP0493) then static; **entry/exit:** Zoom settles after EP0493; hard replace (EP0494). 72 frames. Entry EP0493, exit EP0494.
- **Narration (ASR, unverified):** 250 ,000 new first -time buyers over three years.
- **Story function (INFERRED):** Shows the projected 250,000 buyers target (ASR '250,000 new first-time buyers').
- **Continuity:** S0349 zoomed.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0351 — f14950-14954 (622.958-623.125 s, 5 frames, 0.21 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0494.jpg; entry EP0494, exit EP0495; second review: OK
- **Objects/placement (OBSERVED):** Dark PDF viewer (x .21-.78, y .07-.97): toolbar strip top, thumbnail sidebar left (x .22-.31), white page with serif title block and authors centred (x .38-.76), small footer text.
- **Background:** Dark grey viewer chrome with white page on off-white canvas.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Serif title about 1.8% black; authors about 1%.
- **Readable text:** The Impact of Federal Housing Policy on Housing Demand and Homeownership: Evidence from a Quasi-Experiment
- **Unreadable/uncertain text:** author list, footer
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.836 #252726:0.103 #3a3b3b:0.028 #babdc0:0.018 #6b7478:0.015
- **Hierarchy:** White title page against dark frame.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Hard replace (EP0494); scroll (EP0495). 5 frames. Entry EP0494, exit EP0495.
- **Narration (ASR, unverified):** Researchers
- **Story function (INFERRED):** Introduces the research paper (ASR 'Researchers').
- **Continuity:** S0352-S0353.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0352 — f14965-14969 (623.583-623.750 s, 5 frames, 0.21 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0495.jpg; entry EP0495, exit EP0496; second review: MINOR
- **Objects/placement (OBSERVED):** PDF viewer (x .21-.78) mid-scroll: cover title block partly off the top, next page title block rising at bottom.
- **Background:** Dark viewer.
- **Illustration:** Serif small.
- **Typography:** Serif title blocks about 1.2% height, black on white pages inside a dark viewer; too small to read.
- **Readable text:** none
- **Unreadable/uncertain text:** title blocks
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.829 #252726:0.107 #3b3c3c:0.028 #bebfc1:0.022 #797a7b:0.015
- **Hierarchy:** Two stacked titles.
- **Camera/motion:** SCROLL in progress; **entry/exit:** Mid-scroll of EP0495/EP0496; 5-frame animation state. Entry EP0495, exit EP0496.
- **Narration (ASR, unverified):** went
- **Story function (INFERRED):** Transition between pages.
- **Continuity:** Between S0351 and S0353.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0353 — f14990-14992 (624.625-624.708 s, 3 frames, 0.12 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0496.jpg; entry EP0496, exit EP0497; second review: MINOR
- **Objects/placement (OBSERVED):** PDF viewer page 2 (x .21-.78): title and authors then 'Abstract' with paragraph below; page-2 thumbnail highlighted in blue.
- **Background:** Dark viewer.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Serif title about 1.4%.
- **Readable text:** The Impact of Federal Housing Policy on Housing Demand and Homeownership: Evidence from a Quasi-Experiment; January 2019; Abstract
- **Unreadable/uncertain text:** abstract paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.805 #292b2a:0.129 #c7c8ca:0.030 #9b9b9c:0.022 #6d6e6f:0.014
- **Hierarchy:** Title then abstract.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Scroll settles (EP0496); zoom (EP0497). 3 frames. Entry EP0496, exit EP0497.
- **Narration (ASR, unverified):** counted.
- **Story function (INFERRED):** Leads to abstract (ASR 'counted').
- **Continuity:** S0351.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0354 — f15022-15034 (625.958-626.458 s, 13 frames, 0.54 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0497.jpg; entry EP0497, exit EP0499; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed abstract page: heading at upper left (x .08-.12, y .1), paragraph (x .08-.67, y .17-.6), acknowledgements below, dark vertical bar at right (x .76-.79), mouse cursor at (.78, .77).
- **Background:** White page.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Sans/Calibri-like text about 1.6% black.
- **Readable text:** Abstract
- **Unreadable/uncertain text:** paragraph, acknowledgements
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.823 #d3d4d5:0.053 #a3a4a5:0.050 #727272:0.044 #282828:0.030
- **Hierarchy:** Heading then paragraph.
- **Camera/motion:** Zoom settled; **entry/exit:** Zoom settles (EP0497); micro cursor (EP0498); icons appear (EP0499). 13 frames. Entry EP0497, exit EP0499.
- **Narration (ASR, unverified):** created about
- **Story function (INFERRED):** Abstract reading beat (ASR 'created about').
- **Continuity:** S0355.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0146 (CODEC_ARTIFACT, f15026) Net change is about 0.0 percent; only the mouse cursor at the right edge is visible and it looks identical between frames. No content change seen.

## S0355 — f15038-15143 (626.625-631.000 s, 106 frames, 4.42 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0499.jpg; entry EP0499, exit EP0500; second review: OK
- **Objects/placement (OBSERVED):** Abstract text (x .08-.67); green marker highlight over a sentence (x .08-.67, y .52-.62); three doodle buildings (pink house x .66-.72, tall grey building x .76-.86, blue duplex x .73-.82) on the dark bar at lower right (y .55-.95).
- **Background:** White page, dark bar.
- **Illustration:** Green highlighter; pastel icon doodles with thin outlines.
- **Typography:** Sans about 1.6% black.
- **Readable text:** We also estimate that the premium cut induced approximately 17,000 households to become first-time homebuyers
- **Unreadable/uncertain text:** rest of paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.787 #cccecd:0.068 #9ca199:0.055 #696b67:0.048 #1f201e:0.042
- **Hierarchy:** Highlight then icons.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Highlight and icons pop in (EP0499); presenter arrives (EP0500). 106 frames. Entry EP0499, exit EP0500.
- **Narration (ASR, unverified):** 17 ,000 new first -time buyers, which was an increase that fell far short
- **Story function (INFERRED):** The 17,000 new buyers figure (ASR '17,000 new first-time buyers').
- **Continuity:** Icons echo S0297.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0356 — f15144-15204 (631.042-633.542 s, 61 frames, 2.54 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0500.jpg; entry EP0500, exit EP0501; second review: MINOR
- **Objects/placement (OBSERVED):** Same as S0355 plus neutral-faced presenter bottom centre (x .39-.55, y .62-1.0) overlapping text, hands low.
- **Background:** White page.
- **Illustration:** Peach round head, dot eyes, flat mouth, spiky hair.
- **Typography:** Sans 1.6%.
- **Readable text:** We also estimate that the premium cut induced approximately 17,000 households...
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.754 #cbc9bf:0.098 #7b7b7b:0.067 #1f271c:0.054 #7de74e:0.027
- **Hierarchy:** Presenter's face over highlight.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Presenter added (EP0500); relocates (EP0501). 61 frames. Entry EP0500, exit EP0501.
- **Narration (ASR, unverified):** short of the Federal Housing Administration's projection.
- **Story function (INFERRED):** 'fell far short of the projection' (ASR).
- **Continuity:** Presenter style S0319.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0357 — f15205-15351 (633.583-639.667 s, 147 frames, 6.12 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0501.jpg; entry EP0501, exit EP0503; second review: OK
- **Objects/placement (OBSERVED):** Presenter relocated top-left (x .01-.16, y .03-.23) with pointer crossing text; magenta highlight on 'The premium cut' (x .08-.35, y .13-.2); green highlight remains; buildings at right.
- **Background:** White page.
- **Illustration:** Magenta marker; lines.
- **Typography:** Sans 1.6%.
- **Readable text:** The premium cut
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.754 #c8c6be:0.099 #7a7979:0.066 #1f261d:0.052 #7ae54a:0.028
- **Hierarchy:** Magenta highlight then green.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** EP0501; micro EP0502; zoom out EP0503. 147 frames. Entry EP0501, exit EP0503.
- **Narration (ASR, unverified):** What it did do was give the typical FHA buyer about 6 % more buying power, and they used it.
- **Story function (INFERRED):** Buying power 6 percent (ASR).
- **Continuity:** S0355-S0356.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0147 (OTHER, f15327) Tiny change near the top-left presenter and pink highlighted line; crop shows the pink highlight and pointer virtually identical across frames, so the change cannot be named.

## S0358 — f15404-15435 (641.875-643.167 s, 32 frames, 1.33 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0503.jpg; entry EP0503, exit EP0506; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed-out cover of abstract: 'Previous version: June 2018' centred top (y .08), Abstract heading, paragraph (x .14-.85, y .28-.84); thin dark bar at the far right edge only (x .96-1.0), no bar on the left.
- **Background:** White page.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Sans 1.4%.
- **Readable text:** Previous version: June 2018; Abstract
- **Unreadable/uncertain text:** paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.813 #d0d0d1:0.054 #5f5e5f:0.050 #98999a:0.042 #282828:0.042
- **Hierarchy:** Heading then paragraph.
- **Camera/motion:** Settled after zoom (EP0503); **entry/exit:** Zoom/scroll settles (EP0503); highlight starts (EP0504). 32 frames. Entry EP0503, exit EP0506.
- **Narration (ASR, unverified):** % more for their homes, not
- **Story function (INFERRED):** Reset to the abstract (ASR '% more for their homes').
- **Continuity:** S0354.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0148 (HIGHLIGHT_ADD, f15408) Yellow highlight and a short red underline are drawn on a line of article text at right (x~0.58-0.92,y~0.50-0.75); EVI0149 (HIGHLIGHT_ADD, f15412) A yellow highlight begins on a short run of words in the right part of one abstract line ('Our analysis...').; EVI0150 (HIGHLIGHT_ADD, f15425) The yellow highlight extends further along the same line toward the right margin.

## S0359 — f15448-15494 (643.708-645.625 s, 47 frames, 1.96 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0506.jpg; entry EP0506, exit EP0508; second review: OK
- **Objects/placement (OBSERVED):** Abstract text; yellow highlight over four lines (x .14-.85, y .5-.67); large red-roofed house with green bushes at lower right (x .62-.78, y .66-.92).
- **Background:** White page.
- **Illustration:** Yellow marker; house flat brown with red roof, detailed windows.
- **Typography:** Sans 1.4%.
- **Readable text:** Our analysis shows FHA borrowers increased the value of the housing they purchased by 2.5 percentage points
- **Unreadable/uncertain text:** rest
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfa:0.764 #6f6856:0.068 #b4b1ad:0.061 #2c281f:0.060 #e2de46:0.047
- **Hierarchy:** Highlight then house.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Highlight (EP0504-0505); house rises (EP0506); swap (EP0508). 47 frames. Entry EP0506, exit EP0508.
- **Narration (ASR, unverified):** more for a bigger home or a better one,
- **Story function (INFERRED):** 'more for a bigger home' (ASR).
- **Continuity:** House echoes S0331.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0151 (HIGHLIGHT_ADD, f15456) Yellow highlight gains another line section across the abstract just above the house; house unchanged.

## S0360 — f15495-15547 (645.667-647.833 s, 53 frames, 2.21 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0508.jpg; entry EP0508, exit EP0512; second review: OK
- **Objects/placement (OBSERVED):** Highlight extended to 'buyers.'; large house replaced by small house (x .65-.71, y .73-.9) and tall grey building (x .73-.82); three money bags with dollar signs appear in a row at x .31-.61, y .7-.89.
- **Background:** White page.
- **Illustration:** Green bags with $ marks.
- **Typography:** Sans 1.4%.
- **Readable text:** Our analysis shows FHA borrowers... buyers.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfa:0.761 #343224:0.070 #74766b:0.061 #c2c3bd:0.055 #e1dd43:0.053
- **Hierarchy:** Bags then icons.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** EP0508-0511; scroll (EP0512). 53 frames. Entry EP0508, exit EP0512.
- **Narration (ASR, unverified):** for the same homes at higher prices.
- **Story function (INFERRED):** 'for the same homes at higher prices' (ASR).
- **Continuity:** Icons S0355; bags new.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0152 (ADDITIVE_ENTRY, f15521) A green money bag with a dollar sign appears left of the small house at lower right.; EVI0153 (ADDITIVE_ENTRY, f15528) A second money bag appears to the right of the first.; EVI0154 (ADDITIVE_ENTRY, f15535) A third money bag appears next to the second, completing a row of three bags.

## S0361 — f15585-15601 (649.417-650.083 s, 17 frames, 0.71 s) — shot SH139 (inferred) — F6 chart/graph
- **Evidence:** frames/ep_stable/e0512.jpg; entry EP0512, exit EP0513; second review: MINOR
- **Objects/placement (OBSERVED):** Chart page (x .14-.84, y .08-.75): title above, legend box at left (x .26-.4, y .2-.27), orange rising line above blue line, y axis 90-125, x axis 2013:Q4-2017:Q4, notes below, body text at bottom.
- **Background:** White page, dark bars at edges.
- **Illustration:** Orange and blue thin lines.
- **Typography:** Sans 1.2% axis; title 1.8%.
- **Readable text:** Figure 9. Constant-quality House Price Index; Treatment tracts; Control tracts; 2014:Q4 = 100
- **Unreadable/uncertain text:** axis ticks, note, body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.835 #dad9d9:0.053 #282828:0.041 #686868:0.040 #a3a1a0:0.032
- **Hierarchy:** Two diverging lines.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Scroll arrives (EP0512); presenter enters (EP0513). 17 frames. Entry EP0512, exit EP0513.
- **Narration (ASR, unverified):** stop with the FHA
- **Story function (INFERRED):** Evidence of price jump (ASR 'stop with the FHA').
- **Continuity:** S0362-S0363.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0362 — f15602-15712 (650.125-654.708 s, 111 frames, 4.62 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0513.jpg; entry EP0513, exit EP0519; second review: OK
- **Objects/placement (OBSERVED):** Chart page; presenter with pointer at lower left (x .06-.22, y .47-.95); thick blue marker stroke drawn along the blue line, growing from left to right.
- **Background:** White page.
- **Illustration:** Blue marker over line.
- **Typography:** Sans 1.2%.
- **Readable text:** Figure 9. Constant-quality House Price Index
- **Unreadable/uncertain text:** notes
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.809 #e1d4c9:0.070 #232222:0.049 #676666:0.041 #a19e9e:0.031
- **Hierarchy:** Blue stroke then presenter.
- **Camera/motion:** STATIC 2D; marker stroke progressively drawn; **entry/exit:** Presenter arrives (EP0513); stroke draws (EP0514-0518). 111 frames. Entry EP0513, exit EP0519.
- **Narration (ASR, unverified):** FHA buyers. They hit everyone buying in those neighborhoods, including first -time buyers who
- **Story function (INFERRED):** Non-FHA buyers' prices rose too (ASR).
- **Continuity:** Presenter reused S0348.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.
- **Intra-state events:** EVI0155 (DRAW_ON_OR_REVEAL, f15627) A thick blue stroke starts on the left end of the lower (blue) chart line, just right of the presenter.; EVI0156 (DRAW_ON_OR_REVEAL, f15629) A thick blue stroke is drawn along the lower series of a line chart; this frame group extends it by a segment (x~0.10-0.82,y~0.10-0.99 diff window; stroke front at x~0.30); EVI0157 (DRAW_ON_OR_REVEAL, f15649) Blue chart-line stroke extends further to the right (stroke front at x~0.50); EVI0158 (DRAW_ON_OR_REVEAL, f15651) The blue stroke extends a bit further along the line, roughly mid-chart.; EVI0159 (DRAW_ON_OR_REVEAL, f15653) Blue chart-line stroke extends further right (stroke front at x~0.55); EVI0160 (DRAW_ON_OR_REVEAL, f15660) Blue chart-line stroke extends further right (stroke front at x~0.63); EVI0161 (DRAW_ON_OR_REVEAL, f15667) Blue chart-line stroke reaches the right end of the series (stroke front at x~0.74)
- **Intra-state motion intervals:** EP0515;EP0517;EP0518

## S0363 — f15713-15752 (654.750-656.375 s, 40 frames, 1.67 s) — shot SH139 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0519.jpg; entry EP0519, exit EP0520; second review: OK
- **Objects/placement (OBSERVED):** Chart page; blue stroke now covers the full blue line; presenter at left; second worried black-haired figure holding a banknote at lower right (x .81-.95, y .55-1.0).
- **Background:** White page.
- **Illustration:** Blue marker; dark hair figure.
- **Typography:** Sans 1.2%.
- **Readable text:** Figure 9. Constant-quality House Price Index
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.777 #d7cbc1:0.082 #1f1e1d:0.077 #747471:0.056 #294adc:0.009
- **Hierarchy:** Blue line, then new figure.
- **Camera/motion:** STATIC 2D; no camera move observed; **entry/exit:** Entry EP0519; hard replace (EP0520). 40 frames. Entry EP0519, exit EP0520.
- **Narration (ASR, unverified):** who never got the discount.
- **Story function (INFERRED):** 'who never got the discount' (ASR).
- **Continuity:** Figure echoes S0301.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0364 — f15774-15854 (657.292-660.625 s, 81 frames, 3.38 s) — shot SH139 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0520.jpg; entry EP0520, exit EP0521; second review: MINOR
- **Objects/placement (OBSERVED):** White document page filling the whole frame: indented paragraph (x .16-.84, y .05-.62), short rule (y .67) and numbered footnotes beneath (y .70-.98); no other objects. The grey area in the sheet is padding, not content.
- **Background:** White page.
- **Illustration:** Screenshot capture, no hand-drawn art.
- **Typography:** Calibri-style 1.6% black.
- **Readable text:** In 2015, there were 1.22 million non-FHA home purchase borrowers; about 500,000 of these borrowers were first-time homebuyers; approximately $6,200 extra per house; about $3.1 billion
- **Unreadable/uncertain text:** footnotes
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.812 #dfdfdf:0.060 #838383:0.044 #b4b4b4:0.043 #545454:0.041
- **Hierarchy:** Paragraph then footnotes.
- **Camera/motion:** Zoom settled; **entry/exit:** Hard-ish transition (EP0520); exit EP0521. 81 frames. Entry EP0520, exit EP0521.
- **Narration (ASR, unverified):** added it up. Roughly 500 ,000 of those buyers paid about $6
- **Story function (INFERRED):** The cost to non-FHA buyers (ASR 'Roughly 500,000 ...').
- **Continuity:** Page is the PDF seen in S0361.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and text from the state sheet and boundary sheets; INFERRED: story function from the unverified ASR wording.

## S0365 — f15855-15863 (660.667-661.000 s, 9 frames, 0.38 s) — shot SH139 (inferred) — F4
- **Evidence:** frames/ep_stable/e0521.jpg; entry EP0521, exit EP0522; second review: MINOR
- **Objects/placement (OBSERVED):** Full-frame study-paper page (x0.04-0.96,y0.03-0.98) with a teal-highlighted three-line passage (y0.50-0.62); one green banknote doodle at lower centre-right (x0.59-0.75,y0.68-0.88), ~15% frame width.
- **Background:** Cut-in white document page of printed text.
- **Illustration:** Page is a flat scan; banknote is hand-drawn, thick black outline, flat green fill, yellow dollar mark.
- **Typography:** Serif printed body text, black, ~1.5% frame height, justified; teal marker highlight.
- **Readable text:** Highlighted passage: We estimate that about 500,000 of these borrowers were first-time homebuyers; each of these 500,000 non-FHA first-time homebuyers paid approximately $6,200 extra per house, a total extra payment of about $3.1 billion.
- **Unreadable/uncertain text:** Remaining body paragraphs and footnotes 35-37 are too small to quote.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.793 #7c907d:0.074 #c4c5c4:0.055 #3c4d49:0.041 #91f2de:0.037
- **Hierarchy:** Teal highlight first, then the green banknote doodle.
- **Camera/motion:** STATIC 2D; **entry/exit:** Begins after a small additive event EP0521 (banknote pops on); ends at EP0522 (second note added).
- **Narration (ASR, unverified):** $6 ,200
- **Story function (INFERRED):** INFERRED: shows the research paper behind the spoken per-house cost; money doodle flags the cost.
- **Continuity:** S0366 is the same page with two notes.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0366 — f15864-15910 (661.042-662.958 s, 47 frames, 1.96 s) — shot SH139 (inferred) — F4
- **Evidence:** frames/ep_stable/e0522.jpg; entry EP0522, exit EP0523; second review: MINOR
- **Objects/placement (OBSERVED):** Same study page full-frame with teal highlight; two overlapping green banknotes at lower centre-right (x0.53-0.79,y0.65-0.88), upper note on top, tilted.
- **Background:** Cut-in white document page.
- **Illustration:** Same page; notes flat green, thick outline, stacked at slight angle.
- **Typography:** Serif black body text ~1.5%; teal highlight.
- **Readable text:** Highlighted passage: We estimate that about 500,000 of these borrowers were first-time homebuyers; each of these 500,000 non-FHA first-time homebuyers paid approximately $6,200 extra per house, a total extra payment of about $3.1 billion.
- **Unreadable/uncertain text:** Remaining body paragraphs and footnotes are too small to quote.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafbfb:0.781 #778f79:0.085 #c1c2c0:0.054 #91f2dd:0.042 #32453f:0.038
- **Hierarchy:** Highlight, then stacked notes.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0522 (second note); exits via EP0523, a 3-frame cut to a blank canvas.
- **Narration (ASR, unverified):** ,200 extra per home.
- **Story function (INFERRED):** INFERRED: emphasises extra money per household as the figure is spoken.
- **Continuity:** Follows S0365; next S0367 text card.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0367 — f15914-15976 (663.125-665.708 s, 63 frames, 2.62 s) — shot SH140 (inferred) — F7
- **Evidence:** frames/ep_stable/e0523.jpg; entry EP0523, exit EP0530; second review: OK
- **Objects/placement (OBSERVED):** Single red handwritten text typed on at left-centre (x0.08-0.38,y0.38-0.55 once complete); starts as one '$' and grows to '$3.1 BILLION'. Nothing else.
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Hand-lettered red marker glyphs, no outline.
- **Typography:** Handwritten marker-style, red, ~9% frame height, left-aligned, typed on letter by letter.
- **Readable text:** $3.1 BILLION
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.996 #de0416:0.002 #b81223:0.001 #cd5b61:0.000 #fcb1b7:0.000
- **Hierarchy:** Only red text on white; eye goes straight to it.
- **Camera/motion:** STATIC 2D; **entry/exit:** Starts with EP0523 cut; typed on by micro/animation events EP0524-EP0529; exits via EP0530.
- **Narration (ASR, unverified):** That's $3 .1 billion in extra costs, $3
- **Story function (INFERRED):** INFERRED: kinetic text of the cost figure.
- **Continuity:** Text reused in S0368 (shrunk, up-right).
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0162 (TEXT_CHANGE, f15917) The digit '3' is added after the red '$' at left-centre.; EVI0163 (TEXT_CHANGE, f15920) Handwritten red text '$3' gains a trailing period; value is typed/handwritten one character at a time (x~0.33-0.36,y~0.43-0.58); EVI0164 (TEXT_CHANGE, f15923) Red text grows from '$3.' to '$3.1' (digit 1 appears at left-centre).; EVI0165 (TEXT_CHANGE, f15930) Letter 'B' added after '$3.1' in the red handwritten text, left-centre.; EVI0166 (TEXT_CHANGE, f15951) Final letter 'N' added completing red handwritten '$3.1 BILLION' at upper-left of centre.
- **Intra-state motion intervals:** EP0527;EP0528

## S0368 — f15997-16079 (666.583-670.000 s, 83 frames, 3.46 s) — shot SH140 (inferred) — F3
- **Evidence:** frames/ep_stable/e0530.jpg; entry EP0530, exit EP0533; second review: MINOR
- **Objects/placement (OBSERVED):** Top right: red handwritten text (x0.55-0.89,y0.11-0.22). Left edge: worried peach head with dot eyes and arrow-like arm (x0.00-0.26,y0.28-0.64). Right-centre: heap of about eight dark green money sacks with yellow dollar signs (x0.50-0.96,y0.38-0.76). A tiny house and green count label appear later in the state, not visible in the tile.
- **Background:** Empty off-white canvas.
- **Illustration:** Flat fills, thick outline: peach head with dot eyes and frown; sacks dark green with yellow dollar sign; tiny house.
- **Typography:** Handwritten red text ~8% height; tiny green label ~1.5%.
- **Readable text:** $3.1 BILLION; label near the small house reads 17,000
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.827 #6f8766:0.076 #0e1109:0.049 #e9cfa1:0.039 #c01729:0.009
- **Hierarchy:** Sack pile is the largest mass; red text above it; face at left.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0530 (slide/shrink); micro entries EP0531-EP0532 add house and label; exits by hard cut EP0533.
- **Narration (ASR, unverified):** billion to create about 17 ,000 new homeowners. That's
- **Story function (INFERRED):** INFERRED: contrasts a giant money pile with a small number of new homeowners.
- **Continuity:** Text from S0367 persists; pile unique to this shot.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0167 (ADDITIVE_ENTRY, f16015) A tiny house doodle with small figure appears at lower centre, between the left figure and the money bags.; EVI0168 (TEXT_CHANGE, f16032) Tiny green label '17,000' appears just above the small house doodle at lower centre.

## S0369 — f16080-16118 (670.042-671.625 s, 39 frames, 1.62 s) — shot SH141 (inferred) — F1
- **Evidence:** frames/ep_stable/e0533.jpg; entry EP0533, exit EP0534; second review: MINOR
- **Objects/placement (OBSERVED):** Single standing presenter with olive-green tie, beige head, concerned face, right of centre (x0.71-0.90,y0.24-1.00), ~75% frame height; rest of canvas empty.
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Thick uneven black outline, flat tan fill, bent arm at chest, worried brow.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.938 #ddc7b3:0.029 #030302:0.025 #68885e:0.006 #404038:0.002
- **Hierarchy:** Presenter alone.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0533; exits at EP0534 as a newspaper slides in.
- **Narration (ASR, unverified):** That's a trade so bad, it can
- **Story function (INFERRED):** INFERRED: reaction beat before the sarcastic comparison.
- **Continuity:** Same presenter in S0370, S0371, S0407-S0409.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0370 — f16137-16183 (672.417-674.333 s, 47 frames, 1.96 s) — shot SH141 (inferred) — F5
- **Evidence:** frames/ep_stable/e0534.jpg; entry EP0534, exit EP0535; second review: MINOR
- **Objects/placement (OBSERVED):** Left: tabloid-newspaper cover (x0.12-0.59,y0.00-0.97) with flags, masthead, two portraits and bold black headline block. Right: green-tie presenter (x0.72-0.89,y0.24-1.00).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Cover is a real screenshot (photo plus white-on-black headline); presenter hand-drawn, flat tan fill.
- **Typography:** Heavy condensed sans, white on black, ~9% height headline; smaller caption.
- **Readable text:** NEW YORK POST masthead; DEAL WITH THE DEVIL; Biden trades Merchant of D..th with Russia to free WNBA player Griner
- **Unreadable/uncertain text:** Photo captions and date line
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.622 #1c181a:0.172 #d6c5bf:0.086 #694f53:0.069 #a18382:0.051
- **Hierarchy:** Black headline block first, then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0534 (cover slides in from left); exits via EP0535 pose change then EP0536 cut.
- **Narration (ASR, unverified):** compared to the time we traded Brittany Griner for
- **Story function (INFERRED):** INFERRED: pop-culture analogy for a lopsided trade.
- **Continuity:** Cover continues in S0371.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0371 — f16184-16218 (674.375-675.792 s, 35 frames, 1.46 s) — shot SH141 (inferred) — F5
- **Evidence:** frames/ep_stable/e0535.jpg; entry EP0535, exit EP0536; second review: MINOR
- **Objects/placement (OBSERVED):** Newspaper cover at left (x0.13-0.59,y0.00-0.96) and green-tie presenter right of it (x0.70-0.86,y0.32-1.00), eyes shut, hand to chin.
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Same style; pose changed to a thinking gesture.
- **Typography:** Same headline typography.
- **Readable text:** NEW YORK POST; DEAL WITH THE DEVIL; Biden trades Merchant of D..th with Russia to free WNBA player Griner
- **Unreadable/uncertain text:** Small deck text under headline
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.625 #1c191a:0.170 #d5c5bf:0.086 #674e52:0.067 #9f7e80:0.052
- **Hierarchy:** Headline, then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by pose swap EP0535; exits by hard cut EP0536.
- **Narration (ASR, unverified):** for the Russian arms dealer.
- **Story function (INFERRED):** INFERRED: wry commentary beat.
- **Continuity:** Continues S0370.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0372 — f16219-16244 (675.833-676.875 s, 26 frames, 1.08 s) — shot SH142 (inferred) — F1
- **Evidence:** frames/ep_stable/e0536.jpg; entry EP0536, exit EP0537; second review: OK
- **Objects/placement (OBSERVED):** Plain stick figure centred (x0.43-0.55,y0.10-0.85): large peach head with spiky dark hair, small smile, thin line body, arms out.
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Thin black line body, flat peach head, dot eyes, simple smile.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f4d2b7:0.031 #090605:0.011 #5a534f:0.002 #a19b96:0.002
- **Hierarchy:** Single figure, centred.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0536; replaced by EP0537.
- **Narration (ASR, unverified):** That's what happens when you hand
- **Story function (INFERRED):** INFERRED: neutral narrator reset.
- **Continuity:** Plain figure also in S0380, S0406.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0373 — f16245-16278 (676.917-678.292 s, 34 frames, 1.42 s) — shot SH143 (inferred) — F2
- **Evidence:** frames/ep_stable/e0537.jpg; entry EP0537, exit EP0538; second review: MINOR
- **Objects/placement (OBSERVED):** Large laughing figure with orange tie and mauve-pink head holding fans of green bills in both hands, left of centre (x0.13-0.51,y0.25-1.00).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Thick outline, flat fills, huge open grin, bills with dollar discs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.905 #080906:0.034 #d8c2bd:0.031 #77996d:0.023 #c39d72:0.007
- **Hierarchy:** Grin then bills.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0537; exits by EP0538 (house added).
- **Narration (ASR, unverified):** hand buyers money without fixing
- **Story function (INFERRED):** INFERRED: buyers handed free money.
- **Continuity:** Continues in S0374.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0374 — f16279-16305 (678.333-679.417 s, 27 frames, 1.12 s) — shot SH143 (inferred) — F2
- **Evidence:** frames/ep_stable/e0538.jpg; entry EP0538, exit EP0539; second review: MINOR
- **Objects/placement (OBSERVED):** Left: laughing cash-holding figure (x0.13-0.51,y0.25-1.00). Right: drab olive house with dark red roof, brown door and one blue window (x0.58-0.86,y0.18-0.68).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Thick outline; house drab olive with sketch lines.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.811 #8f956f:0.070 #070504:0.066 #d5c3be:0.034 #61433c:0.018
- **Hierarchy:** Figure then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0538; exits by EP0539 cut.
- **Narration (ASR, unverified):** fixing the root problem.
- **Story function (INFERRED):** INFERRED: free money meets a house.
- **Continuity:** Continues S0373.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0375 — f16306-16337 (679.458-680.750 s, 32 frames, 1.33 s) — shot SH144 (inferred) — F3
- **Evidence:** frames/ep_stable/e0539.jpg; entry EP0539, exit EP0540; second review: MINOR
- **Objects/placement (OBSERVED):** Blue mansion with navy roofs and two green trees (x0.15-0.54,y0.26-0.67), red 'FOR SALE!' sign on a post at right (x0.54-0.70,y0.58-0.83), tiny grey-haired figure at lower left (x0.23-0.28,y0.67-0.89).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Pastel blue house, navy roofs, tiny figure, red sign with white lettering.
- **Typography:** Hand-lettered white caps on a red sign, ~2% height.
- **Readable text:** FOR SALE!
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.888 #070607:0.048 #39585a:0.027 #acc3d0:0.024 #bf322e:0.013
- **Hierarchy:** House first, sign second; tiny figure gives scale.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0539; exits via EP0540 cut.
- **Narration (ASR, unverified):** When supply doesn't move,
- **Story function (INFERRED):** INFERRED: seller-side of the market.
- **Continuity:** House reused in S0407-S0410.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0376 — f16338-16343 (680.792-681.000 s, 6 frames, 0.25 s) — shot SH145 (inferred) — F2
- **Evidence:** frames/ep_stable/e0540.jpg; entry EP0540, exit EP0541; second review: MINOR
- **Objects/placement (OBSERVED):** One green banknote at left (x0.13-0.29,y0.33-0.51) and a grey-haired purple-tie figure at right (x0.73-0.90,y0.28-1.00).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Thick outline; scribbly grey hair; purple tie.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.921 #080708:0.030 #bdb6ad:0.027 #799e6a:0.018 #8857af:0.004
- **Hierarchy:** Bill and figure at opposite sides.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0540; exits EP0541. Only 6 frames because bills are added word by word.
- **Narration (ASR, unverified):** the money
- **Story function (INFERRED):** INFERRED: starts a stack of bills per spoken word.
- **Continuity:** Same figure through S0379.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0377 — f16344-16348 (681.042-681.208 s, 5 frames, 0.21 s) — shot SH145 (inferred) — F2
- **Evidence:** frames/ep_stable/e0541.jpg; entry EP0541, exit EP0542; second review: MINOR
- **Objects/placement (OBSERVED):** Two green bills at left-centre (x0.13-0.42,y0.33-0.72), grey-haired purple-tie figure at right (x0.73-0.90,y0.28-1.00).
- **Background:** empty off-white canvas (#FCFCFC)
- **Illustration:** Same flat style.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.902 #070707:0.033 #7da96b:0.030 #bdb6ad:0.027 #745f84:0.008
- **Hierarchy:** Bills, then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0541; exits EP0542. 5 frames only (word timing).
- **Narration (ASR, unverified):** money has
- **Story function (INFERRED):** INFERRED: bill count rising with narration.
- **Continuity:** Between S0376 and S0378.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0378 — f16349-16393 (681.250-683.083 s, 45 frames, 1.88 s) — shot SH145 (inferred) — F2
- **Evidence:** frames/ep_stable/e0542.jpg; entry EP0542, exit EP0543; second review: MINOR
- **Objects/placement (OBSERVED):** Three green banknotes in a loose triangle at left (x0.13-0.51,y0.19-0.72); grey-haired purple-tie figure at right (x0.73-0.90,y0.28-1.00).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, flat green bills with dollar discs, scribbly grey hair.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.882 #7da76b:0.048 #040604:0.034 #b8acaf:0.031 #4a4d49:0.006
- **Hierarchy:** Bills left, figure right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0542 (third bill); exits via 16-frame bill flight EP0543.
- **Narration (ASR, unverified):** has exactly one place to go, into
- **Story function (INFERRED):** INFERRED: money piling up before reaching the seller.
- **Continuity:** Continues S0377; resolves in S0379.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0379 — f16410-16428 (683.792-684.542 s, 19 frames, 0.79 s) — shot SH145 (inferred) — F2
- **Evidence:** frames/ep_stable/e0543.jpg; entry EP0543, exit EP0544; second review: MINOR
- **Objects/placement (OBSERVED):** Right: grey-haired purple-tie figure smiling, one arm raised holding a bill (x0.63-0.90,y0.28-1.00); small pile of three bills left of its body (x0.57-0.69,y0.66-0.82).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Same figure; grin, arm extended up.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.922 #050504:0.028 #bcb5ad:0.026 #7f937d:0.020 #40433f:0.005
- **Hierarchy:** Figure and bills at far right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0543 motion (bills fly in); exits by hard cut EP0544.
- **Narration (ASR, unverified):** seller's pockets. That's
- **Story function (INFERRED):** INFERRED: money ends in the seller's hand.
- **Continuity:** Same figure as S0376-S0378.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0380 — f16429-16492 (684.583-687.208 s, 64 frames, 2.67 s) — shot SH146 (inferred) — F1
- **Evidence:** frames/ep_stable/e0544.jpg; entry EP0544, exit EP0546; second review: OK
- **Objects/placement (OBSERVED):** Centred plain stick figure (x0.41-0.58,y0.10-0.95): peach head, spiky dark hair, smile, arms out.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thin black line body, flat peach head, dot eyes.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f4d3b7:0.031 #080505:0.011 #59534f:0.002 #a9a19b:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0544; arm tweak EP0545; exits EP0546.
- **Narration (ASR, unverified):** That's the buyer's part of the story. It's the loud part.
- **Story function (INFERRED):** INFERRED: narrator reset on 'the buyer's part of the story'.
- **Continuity:** Plain figure also S0372, S0406.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0169 (POSE_SWAP, f16466) Plain stick figure's arms shift slightly (left arm lowers) at centre; tiny gesture change only.

## S0381 — f16493-16540 (687.250-689.208 s, 48 frames, 2.00 s) — shot SH147 (inferred) — F2
- **Evidence:** frames/ep_stable/e0546.jpg; entry EP0546, exit EP0547; second review: MINOR
- **Objects/placement (OBSERVED):** Large smiling peach-headed figure in a brown tweed cap holding a magnifying glass on a bent arm (x0.18-0.52,y0.17-1.00).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, peach head, brown cap, glass with pale-blue lens.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.892 #f2d2b6:0.064 #070403:0.025 #756d5a:0.012 #383431:0.007
- **Hierarchy:** Face then magnifier.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0546; exits EP0547.
- **Narration (ASR, unverified):** The other part is quieter because it's built into
- **Story function (INFERRED):** INFERRED: investigator motif for 'the quieter part'.
- **Continuity:** Continues S0382.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0382 — f16541-16568 (689.250-690.375 s, 28 frames, 1.17 s) — shot SH147 (inferred) — F2
- **Evidence:** frames/ep_stable/e0547.jpg; entry EP0547, exit EP0548; second review: MINOR
- **Objects/placement (OBSERVED):** Cap figure with magnifying glass at left (x0.18-0.52,y0.17-1.00); cream paper with red TAX heading and black squiggle lines at right (x0.59-0.81,y0.21-0.69).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Paper cream with thick border, red caps title, black squiggle lines.
- **Typography:** Handwritten red caps ~5% height on paper.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.799 #ebdab7:0.131 #060403:0.044 #7e7361:0.016 #4c3631:0.011
- **Hierarchy:** Red title then face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0547 (paper added); exits EP0548 cut.
- **Narration (ASR, unverified):** into the tax code.
- **Story function (INFERRED):** INFERRED: introduces the tax code.
- **Continuity:** TAX paper reused S0386-S0390, S0393-S0395, S0405.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0383 — f16569-16588 (690.417-691.208 s, 20 frames, 0.83 s) — shot SH148 (inferred) — F4
- **Evidence:** frames/ep_stable/e0548.jpg; entry EP0548, exit EP0549; second review: MINOR
- **Objects/placement (OBSERVED):** Magazine-page screenshot centred (x0.26-0.74,y0.00-0.95): dark header bar, nav strip, photo of pink townhouses with palms, bold headline, small byline.
- **Background:** Cut-in white web page on off-white canvas.
- **Illustration:** Real photo header; flat UI typography.
- **Typography:** Sans-serif headline, dark grey, ~3.5% height.
- **Readable text:** Assessment Limits Create Tax Disparities That Obstruct Homeownership; LINCOLN INSTITUTE OF LAND POLICY header; Land Lines Magazine tab
- **Unreadable/uncertain text:** Other nav tabs, byline and date
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.781 #4e5148:0.114 #afa490:0.041 #4773a9:0.040 #79a1c9:0.024
- **Hierarchy:** Photo then headline.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0548 hard replace; exits via EP0549 scroll.
- **Narration (ASR, unverified):** More than a dozen states
- **Story function (INFERRED):** INFERRED: source article for the cap claim.
- **Continuity:** Same article S0384, S0391-S0399 at other scrolls.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0384 — f16627-16676 (692.833-694.875 s, 50 frames, 2.08 s) — shot SH148 (inferred) — F5
- **Evidence:** frames/ep_stable/e0549.jpg; entry EP0549, exit EP0550; second review: MINOR
- **Objects/placement (OBSERVED):** Article body column fills x0.09-0.67 full height, cropped at top and bottom; tall green hand-drawn dollar sign with black outline at right (x0.77-0.88,y0.18-0.53).
- **Background:** White article page.
- **Illustration:** Dollar sign: thick black outline, green fill.
- **Typography:** Sans body ~2% height, dark grey, yellow marker highlight, green links.
- **Readable text:** About a dozen (highlighted yellow); In a recent 50-state comparison study; the largest discrepancy; Miami example mentions $9,205 in annual property taxes
- **Unreadable/uncertain text:** Remaining paragraph text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfb:0.820 #55695c:0.062 #cdcec8:0.057 #9fa09c:0.053 #051305:0.009
- **Hierarchy:** Dollar sign and yellow highlight first.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered via EP0549 scroll; exits EP0550 hard replace.
- **Narration (ASR, unverified):** home's taxable value can rise each year.
- **Story function (INFERRED):** INFERRED: supports the 'more than a dozen states' claim.
- **Continuity:** Same article as S0383, S0392-S0395.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0170 (HIGHLIGHT_ADD, f16631) Yellow highlight stroke begins on a line of a long article paragraph (x~0.30-0.46,y~0.48-0.52)

## S0385 — f16677-16711 (694.917-696.333 s, 35 frames, 1.46 s) — shot SH149 (inferred) — F1
- **Evidence:** frames/ep_stable/e0550.jpg; entry EP0550, exit EP0551; second review: MINOR
- **Objects/placement (OBSERVED):** One large worried figure with messy dark hair, brown skin, brown bowtie and hand raised to chin at left (x0.10-0.35,y0.17-1.00); right 60% empty.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; dark swept hair, brown skin, brown bowtie, worried brow, hand at chin.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.899 #211c18:0.035 #040202:0.034 #b09480:0.027 #695348:0.005
- **Hierarchy:** Face first.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0550; exits EP0551.
- **Narration (ASR, unverified):** The idea is to keep property tax
- **Story function (INFERRED):** INFERRED: reaction while caps are explained.
- **Continuity:** Same character S0386-S0390, S0397+.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0386 — f16712-16728 (696.375-697.042 s, 17 frames, 0.71 s) — shot SH149 (inferred) — F2
- **Evidence:** frames/ep_stable/e0551.jpg; entry EP0551, exit EP0552; second review: MINOR
- **Objects/placement (OBSERVED):** Bowtie figure at left (x0.10-0.35,y0.17-1.00); one cream TAX paper with red heading and squiggle lines (x0.48-0.63,y0.25-0.56).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; dark swept hair, brown skin, brown bowtie, worried brow, hand at chin. Paper cream with red TAX.
- **Typography:** Red handwritten caps on paper.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.858 #040202:0.041 #28211c:0.040 #aa8e7b:0.031 #e4dfba:0.030
- **Hierarchy:** Figure then paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0551; exits EP0552.
- **Narration (ASR, unverified):** property tax bills from
- **Story function (INFERRED):** INFERRED: first tax bill.
- **Continuity:** S0385-S0390 series.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0387 — f16729-16734 (697.083-697.292 s, 6 frames, 0.25 s) — shot SH149 (inferred) — F2
- **Evidence:** frames/ep_stable/e0552.jpg; entry EP0552, exit EP0553; second review: MINOR
- **Objects/placement (OBSERVED):** Bowtie figure at left (x0.10-0.35,y0.17-1.00); two TAX papers: lower (x0.51-0.63,y0.25-0.56) and higher (x0.69-0.84,y0.14-0.46).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; dark swept hair, brown skin, brown bowtie, worried brow, hand at chin.
- **Typography:** Red caps TAX on papers.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.817 #e4e0ba:0.058 #040302:0.048 #2a221d:0.042 #a98d7a:0.034
- **Hierarchy:** Figure then papers.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0552; ends EP0553. Only 6 frames (0.25 s) since papers are added word by word.
- **Narration (ASR, unverified):** from skyrocketing
- **Story function (INFERRED):** INFERRED: papers piling up.
- **Continuity:** Between S0386 and S0388.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0388 — f16735-16739 (697.333-697.500 s, 5 frames, 0.21 s) — shot SH149 (inferred) — F2
- **Evidence:** frames/ep_stable/e0553.jpg; entry EP0553, exit EP0554; second review: MINOR
- **Objects/placement (OBSERVED):** Bowtie figure at left (x0.10-0.35,y0.17-1.00); three TAX papers: left (x0.48-0.63,y0.25-0.56), upper right (x0.69-0.83,y0.14-0.44), lower right overlapping (x0.76-0.90,y0.33-0.64).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; dark swept hair, brown skin, brown bowtie, worried brow, hand at chin.
- **Typography:** TAX on papers.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.783 #100d0b:0.090 #e5e1ba:0.082 #ad937f:0.032 #694b40:0.013
- **Hierarchy:** Figure; paper stack.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0553; ends EP0554 (5 frames).
- **Narration (ASR, unverified):** skyrocketing
- **Story function (INFERRED):** INFERRED: pile continues.
- **Continuity:** S0387, S0389.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0389 — f16740-16756 (697.542-698.208 s, 17 frames, 0.71 s) — shot SH149 (inferred) — F2
- **Evidence:** frames/ep_stable/e0554.jpg; entry EP0554, exit EP0555; second review: MINOR
- **Objects/placement (OBSERVED):** Bowtie figure at left (x0.10-0.35,y0.17-1.00); four cream TAX papers in an overlapping fan at right (x0.48-0.90,y0.14-0.64).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; dark swept hair, brown skin, brown bowtie, worried brow, hand at chin.
- **Typography:** TAX on papers.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.750 #e5e1ba:0.106 #100d0a:0.096 #ad937f:0.034 #6a4a3f:0.015
- **Hierarchy:** Figure; cluster.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0554; exits EP0555.
- **Narration (ASR, unverified):** skyrocketing on people
- **Story function (INFERRED):** INFERRED: bills on 'people who already own'.
- **Continuity:** S0388, S0390.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0390 — f16757-16794 (698.250-699.792 s, 38 frames, 1.58 s) — shot SH149 (inferred) — F3
- **Evidence:** frames/ep_stable/e0555.jpg; entry EP0555, exit EP0556; second review: MINOR
- **Objects/placement (OBSERVED):** Small grey-beige office building with grid windows and lower annex (x0.15-0.30,y0.47-0.81), tiny bowtie figure with hand at chin (x0.38-0.44,y0.63-0.89); four TAX papers in overlapping cluster at right (x0.51-0.90,y0.14-0.64).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Building grey with dark windows, thick outline; figure scaled down.
- **Typography:** TAX on papers.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.807 #e5e1bc:0.114 #0a0805:0.042 #614d42:0.019 #a8a18f:0.018
- **Hierarchy:** Papers then building.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0555 (figure shrinks, building added); exits EP0556.
- **Narration (ASR, unverified):** people who already own.
- **Story function (INFERRED):** INFERRED: owners in their building.
- **Continuity:** Same paper cluster as S0389.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0391 — f16795-16822 (699.833-700.958 s, 28 frames, 1.17 s) — shot SH150 (inferred) — F4
- **Evidence:** frames/ep_stable/e0556.jpg; entry EP0556, exit EP0557; second review: MINOR
- **Objects/placement (OBSERVED):** Full-frame article screenshot: dark header bar with logo and nav at top (x0.25-0.75,y0.07-0.21), narrow column of paragraphs below (x0.27-0.70,y0.20-0.95).
- **Background:** White article page.
- **Illustration:** UI screenshot.
- **Typography:** Sans ~1.3% height, dark grey.
- **Readable text:** none
- **Unreadable/uncertain text:** Article paragraphs about assessment caps, Proposition 13 and the Miami example; header nav labels mostly too small
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.845 #4a545a:0.068 #dadbda:0.030 #8a8b8a:0.029 #b3b4b3:0.028
- **Hierarchy:** Header bar then text block.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0556; exits EP0557 scroll.
- **Narration (ASR, unverified):** But according to the Lincoln Institute,
- **Story function (INFERRED):** INFERRED: cites the source.
- **Continuity:** Same article S0383.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0392 — f16842-16873 (701.792-703.083 s, 32 frames, 1.33 s) — shot SH150 (inferred) — F4
- **Evidence:** frames/ep_stable/e0557.jpg; entry EP0557, exit EP0558; second review: OK
- **Objects/placement (OBSERVED):** Zoomed article text (x0.19-0.77,y0.05-0.65) in two paragraphs; the word 'which' just highlighted yellow.
- **Background:** White article page.
- **Illustration:** UI screenshot.
- **Typography:** Sans ~2.6% height, dark grey; yellow marker.
- **Readable text:** Florida's assessment limit is similar to one established by the State of California's Proposition 13... have some kind of assessment limit in place, which can create dramatic tax bill discrepancies
- **Unreadable/uncertain text:** Second paragraph body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.877 #e9eae8:0.046 #c4c6c1:0.027 #767674:0.026 #9c9d99:0.023
- **Hierarchy:** Yellow highlight.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0557 scroll; exits EP0558.
- **Narration (ASR, unverified):** caps create dramatic tax
- **Story function (INFERRED):** INFERRED: key sentence.
- **Continuity:** S0393-S0395.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0393 — f16874-16883 (703.125-703.500 s, 10 frames, 0.42 s) — shot SH150 (inferred) — F5
- **Evidence:** frames/ep_stable/e0558.jpg; entry EP0558, exit EP0560; second review: MINOR
- **Objects/placement (OBSERVED):** Same text; highlight extended along 'which can create dramatic tax bill'; one small TAX paper at lower right (x0.79-0.90,y0.56-0.78).
- **Background:** White article page.
- **Illustration:** Cream paper doodle with thick outline.
- **Typography:** Sans ~2.6%; red TAX.
- **Readable text:** which can create dramatic tax bill
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.882 #dadacb:0.050 #7a7972:0.033 #adac9b:0.031 #18130a:0.004
- **Hierarchy:** Highlight then paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0558 (paper); micro EP0559; exits EP0560. 10 frames.
- **Narration (ASR, unverified):** tax bill
- **Story function (INFERRED):** INFERRED: highlight progresses with narration.
- **Continuity:** S0392, S0394.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0171 (HIGHLIGHT_ADD, f16879) Second TAX paper appears at lower right and yellow highlight begins on the next text line, left side.

## S0394 — f16884-16915 (703.542-704.833 s, 32 frames, 1.33 s) — shot SH150 (inferred) — F5
- **Evidence:** frames/ep_stable/e0560.jpg; entry EP0560, exit EP0561; second review: MINOR
- **Objects/placement (OBSERVED):** Highlight covers 'which can create dramatic tax bill discrepanc[ies]' across two lines; three TAX papers at lower right: front-left (x0.61-0.72,y0.71-0.93), middle (x0.76-0.86,y0.67-0.90), rear (x0.82-0.90,y0.56-0.78).
- **Background:** White article page.
- **Illustration:** Same.
- **Typography:** Sans ~2.6%; red TAX.
- **Readable text:** which can create dramatic tax bill discrepancies (highlighted)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.847 #dedcc5:0.072 #7a766c:0.035 #adab98:0.035 #131008:0.011
- **Hierarchy:** Highlight; papers.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0560; exits EP0561.
- **Narration (ASR, unverified):** bill discrepancies between new
- **Story function (INFERRED):** INFERRED: more papers as the claim runs.
- **Continuity:** S0393, S0395.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0395 — f16920-16954 (705.042-706.458 s, 35 frames, 1.46 s) — shot SH150 (inferred) — F5
- **Evidence:** frames/ep_stable/e0561.jpg; entry EP0561, exit EP0562; second review: MINOR
- **Objects/placement (OBSERVED):** Article text (x0.19-0.77,y0.05-0.65), highlight over 'which can create dramatic tax bill discrepancies between new and longtime'; red-headband brown-haired figure lower left (x0.12-0.31,y0.40-1.00); hunched grey-haired elderly figure with bun and cane (x0.34-0.53,y0.57-1.00); two TAX papers lower right (x0.62-0.90,y0.56-0.93).
- **Background:** White article page.
- **Illustration:** Thick outline; elderly figure with grey bun and bent back.
- **Typography:** Sans ~2.6%.
- **Readable text:** which can create dramatic tax bill discrepancies between new and longtime (highlighted)
- **Unreadable/uncertain text:** Paragraph body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.795 #dcdac4:0.080 #827664:0.048 #b8b294:0.041 #0e0b08:0.036
- **Hierarchy:** Characters over text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0561 (elderly figure enters); exits EP0562.
- **Narration (ASR, unverified):** new and long -time owners.
- **Story function (INFERRED):** INFERRED: new versus long-time owners.
- **Continuity:** S0394.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0396 — f16969-16988 (707.083-707.875 s, 20 frames, 0.83 s) — shot SH150 (inferred) — F4
- **Evidence:** frames/ep_stable/e0562.jpg; entry EP0562, exit EP0563; second review: MINOR
- **Objects/placement (OBSERVED):** Narrow article column centred (x0.25-0.75,y0.07-0.95) with dark logo header bar at top (y0.07-0.21), tiny paragraphs below.
- **Background:** White article page on off-white canvas.
- **Illustration:** UI screenshot.
- **Typography:** Sans ~1.2%.
- **Readable text:** none
- **Unreadable/uncertain text:** Article text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.844 #4a545a:0.068 #d8d9d8:0.033 #b0b1b0:0.029 #898b8b:0.026
- **Hierarchy:** Header bar.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0562 scroll; exits EP0563.
- **Narration (ASR, unverified):** if you own a home,
- **Story function (INFERRED):** INFERRED: transition to next speaker beat.
- **Continuity:** Same article.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0397 — f16989-17009 (707.917-708.750 s, 21 frames, 0.88 s) — shot SH150 (inferred) — F5
- **Evidence:** frames/ep_stable/e0563.jpg; entry EP0563, exit EP0564; second review: MINOR
- **Objects/placement (OBSERVED):** Article column (x0.25-0.75,y0.07-0.95); worried black-haired figure holding a green bill at lower right (x0.71-0.88,y0.38-1.00), overlapping the column edge.
- **Background:** White article page.
- **Illustration:** Thick outline, black hair, light skin.
- **Typography:** Sans tiny.
- **Readable text:** none
- **Unreadable/uncertain text:** Article text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.794 #4a555a:0.071 #cbcac2:0.053 #91968f:0.043 #141312:0.039
- **Hierarchy:** Figure at right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0563 additive; exits EP0564.
- **Narration (ASR, unverified):** not so great if you
- **Story function (INFERRED):** INFERRED: homeowner perspective.
- **Continuity:** S0398.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0398 — f17010-17042 (708.792-710.125 s, 33 frames, 1.38 s) — shot SH150 (inferred) — F5
- **Evidence:** frames/ep_stable/e0564.jpg; entry EP0564, exit EP0565; second review: MINOR
- **Objects/placement (OBSERVED):** Article column (x0.25-0.75,y0.00-0.95); small red-roof house with red 'SALE!' sign at lower left (x0.09-0.20,y0.40-0.70); large black-haired figure holding a green bill at right (x0.69-0.89,y0.31-1.00).
- **Background:** White article page.
- **Illustration:** House red roof; red sign with white lettering.
- **Typography:** Sans tiny; sign lettering.
- **Readable text:** SALE!
- **Unreadable/uncertain text:** Article text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.771 #515357:0.078 #ceccc4:0.059 #151210:0.046 #929790:0.046
- **Hierarchy:** Figure then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0564 (house additive); exits EP0565.
- **Narration (ASR, unverified):** you don't own one yet.
- **Story function (INFERRED):** INFERRED: 'don't own one yet'.
- **Continuity:** S0397.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0399 — f17060-17360 (710.875-723.375 s, 301 frames, 12.54 s) — shot SH151 (inferred) — F5
- **Evidence:** frames/ep_stable/e0565.jpg; entry EP0565, exit EP0567; second review: OK
- **Objects/placement (OBSERVED):** Article page left (x0.05-0.63,y0.05-0.95) with dark header bar, bold title, byline and intro paragraph; smiling light-skinned figure with a long pointer stick at right (x0.73-0.93,y0.30-0.95).
- **Background:** White article page.
- **Illustration:** Stick figure thin line body, peach head, smile, long pointer stick.
- **Typography:** Sans title ~4.5% height dark grey; body ~1.7%.
- **Readable text:** Assessment Limits Create Tax Disparities That Obstruct Homeownership; 'Two Miami townhouses... The owners of one unit... $4,092 ... $14,693'
- **Unreadable/uncertain text:** Rest of body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.807 #4b5459:0.095 #e2d2c2:0.057 #929593:0.029 #090504:0.011
- **Hierarchy:** Title then pointer.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0565 transition; micro EP0566 pointer tilt; exits EP0567. 12.5 s long hold.
- **Narration (ASR, unverified):** cleanest example of this discrepancy in Coconut Grove Miami with two townhouses a few doors apart in the same complex. One owner pays around $4 ,000 a year in property tax. The other pays more than $14 ,000. The
- **Story function (INFERRED):** INFERRED: walks through the Miami two-townhouse example.
- **Continuity:** Same article S0383.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0172 (POSE_SWAP, f17083) Pointer figure's raised arm/pointer angle shifts lower at right of article; tiny gesture change.

## S0400 — f17361-17484 (723.417-728.542 s, 124 frames, 5.17 s) — shot SH152 (inferred) — F2
- **Evidence:** frames/ep_stable/e0567.jpg; entry EP0567, exit EP0572; second review: MINOR
- **Objects/placement (OBSERVED):** Two small cream houses with red roofs, blue windows and brown doors at upper left (x0.13-0.30,y0.22-0.53) and upper right (x0.70-0.88,y0.22-0.53); plain smiling peach head with spiky hair at centre (x0.41-0.58,y0.38-1.00).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, house walls cream with blue windows, thin line figure.
- **Typography:** Small green label '2006' above left house and red '2023' above right house (~2.5% height), added mid-state.
- **Readable text:** 2006; 2023
- **Unreadable/uncertain text:** Year labels reportedly added mid-state are not visible in the tile; unverified.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.865 #e7d5bb:0.077 #0b0705:0.041 #807668:0.010 #9d2825:0.008
- **Hierarchy:** Houses then year labels.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard replace EP0567; micro events EP0568-EP0571 add labels; exits EP0572.
- **Narration (ASR, unverified):** The only difference is when they bought. One in 2006, the other in 2023.
- **Story function (INFERRED):** INFERRED: compares purchases in two years.
- **Continuity:** Plain face figure S0380.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0173 (POSE_SWAP, f17402) Tiny hand/arm change on the lower-centre figure (arm position at bottom).; EVI0174 (TEXT_CHANGE, f17412) Green year label '2006' appears above the left house.; EVI0175 (POSE_SWAP, f17439) Figure's arms change (lower arm/leg lines) under the head at lower centre; houses and label unchanged.; EVI0176 (TEXT_CHANGE, f17453) Red year label '2023' appears above the right house.

## S0401 — f17485-17528 (728.583-730.375 s, 44 frames, 1.83 s) — shot SH153 (inferred) — F4
- **Evidence:** frames/ep_stable/e0572.jpg; entry EP0572, exit EP0573; second review: OK
- **Objects/placement (OBSERVED):** Think-tank page screenshot (x0.26-0.74,y0.06-0.95): blue banner with serif title, yellow button, 'Key Findings' bullet list.
- **Background:** Cut-in white page with blue banner.
- **Illustration:** Real UI screenshot.
- **Typography:** Serif white title on navy ~3% height; black bullets ~1%.
- **Readable text:** Property Tax Limitation Regimes: A Primer; Key Findings
- **Unreadable/uncertain text:** bullet text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.741 #26557d:0.184 #c3c4b3:0.029 #0a1926:0.023 #808c93:0.023
- **Hierarchy:** Blue banner then Key Findings.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0572 hard replace; exits EP0573 scroll.
- **Narration (ASR, unverified):** That's because in Florida, like most states with
- **Story function (INFERRED):** INFERRED: second source for the cap mechanism.
- **Continuity:** S0402, S0403.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0402 — f17540-17564 (730.875-731.875 s, 25 frames, 1.04 s) — shot SH153 (inferred) — F4
- **Evidence:** frames/ep_stable/e0573.jpg; entry EP0573, exit EP0574; second review: OK
- **Objects/placement (OBSERVED):** Article body text scrolled (x0.26-0.74,y0.03-0.95): heading 'State Examples of Assessment Limits' with paragraphs.
- **Background:** White article page.
- **Illustration:** UI screenshot.
- **Typography:** Sans ~1% body, bold ~1.4% heading.
- **Readable text:** State Examples of Assessment Limits
- **Unreadable/uncertain text:** body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.884 #e5e6e6:0.036 #bfbfbf:0.034 #989898:0.032 #6f7071:0.013
- **Hierarchy:** Heading.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0573 scroll; exits EP0574.
- **Narration (ASR, unverified):** cap, the assessment resets
- **Story function (INFERRED):** INFERRED: continues source reading.
- **Continuity:** S0401.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0403 — f17579-17605 (732.500-733.583 s, 27 frames, 1.12 s) — shot SH153 (inferred) — F5
- **Evidence:** frames/ep_stable/e0574.jpg; entry EP0574, exit EP0575; second review: MINOR
- **Objects/placement (OBSERVED):** Zoomed article (x0.00-0.95,y0.00-1.00): heading at top, paragraphs; orange highlight over 'More typically, however, assessment limits'; smiling peach head with a long diagonal pointer stick at upper right (x0.77-1.00,y0.07-0.65).
- **Background:** White article page.
- **Illustration:** Orange marker highlight; pointer figure.
- **Typography:** Sans ~2.5% body, ~4.5% heading; dark grey.
- **Readable text:** State Examples of Assessment Limits; More typically, however, assessment limits involve an acquisition value rule, with the assessed value resetting upon the sale of the property.
- **Unreadable/uncertain text:** Rest of paragraphs
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.793 #ddd1c7:0.089 #6a6865:0.052 #a79a8b:0.052 #1c1715:0.014
- **Hierarchy:** Orange highlight.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0574 zoom-scroll; exits EP0575 cut.
- **Narration (ASR, unverified):** when the house sells. So
- **Story function (INFERRED):** INFERRED: the reset-on-sale rule.
- **Continuity:** S0402.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0404 — f17606-17636 (733.625-734.875 s, 31 frames, 1.29 s) — shot SH154 (inferred) — F3
- **Evidence:** frames/ep_stable/e0575.jpg; entry EP0575, exit EP0576; second review: MINOR
- **Objects/placement (OBSERVED):** Red recliner with a small resting person with closed eyes (x0.21-0.47,y0.44-0.90), lower left-centre; rest empty.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, maroon armchair, small figure reclining.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #b55252:0.048 #1b0705:0.016 #8a4444:0.013 #d0baa4:0.004
- **Hierarchy:** Chair alone.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0575; exits EP0576.
- **Narration (ASR, unverified):** So the longer you stay,
- **Story function (INFERRED):** INFERRED: 'the longer you stay' comfort.
- **Continuity:** S0405.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0405 — f17637-17673 (734.917-736.417 s, 37 frames, 1.54 s) — shot SH154 (inferred) — F2
- **Evidence:** frames/ep_stable/e0576.jpg; entry EP0576, exit EP0578; second review: MINOR
- **Objects/placement (OBSERVED):** Red recliner with resting person at left-centre (x0.21-0.47,y0.44-0.90) and cream TAX paper at right (x0.62-0.80,y0.21-0.61); a green '75% off' with strike line is reported late in the state, not visible in the tile.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Paper with red caps; green handwriting.
- **Typography:** Green handwritten '75% off' ~2.5% height.
- **Readable text:** TAX; 75% off
- **Unreadable/uncertain text:** '75% off' annotation not visible in the tile; unverified.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.857 #af5151:0.061 #e3dfb7:0.049 #0f0402:0.026 #543833:0.007
- **Hierarchy:** Paper then label.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0576 (paper); micro EP0577 (label and strike); exits EP0578.
- **Narration (ASR, unverified):** the bigger your discount gets,
- **Story function (INFERRED):** INFERRED: discount grows with tenure.
- **Continuity:** S0404.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0177 (ADDITIVE_ENTRY, f17644) Green handwritten '75% off' appears with a green strike line across the TAX paper at upper right.

## S0406 — f17674-17712 (736.458-738.042 s, 39 frames, 1.62 s) — shot SH154 (inferred) — F1
- **Evidence:** frames/ep_stable/e0578.jpg; entry EP0578, exit EP0579; second review: OK
- **Objects/placement (OBSERVED):** Plain smiling stick figure centred (x0.43-0.57,y0.18-0.88).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thin line body, peach head.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f4d2b7:0.031 #080605:0.011 #58514d:0.002 #a09a95:0.002
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0578; exits EP0579.
- **Narration (ASR, unverified):** which makes people stay longer.
- **Story function (INFERRED):** INFERRED: narrator beat.
- **Continuity:** S0380.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0407 — f17713-17745 (738.083-739.417 s, 33 frames, 1.38 s) — shot SH155 (inferred) — F2
- **Evidence:** frames/ep_stable/e0579.jpg; entry EP0579, exit EP0580; second review: MINOR
- **Objects/placement (OBSERVED):** Left: green-tie figure holding a green bill, smiling (x0.16-0.41,y0.24-0.89); right: small blue mansion with navy roofs between two trees (x0.58-0.88,y0.28-0.60).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; round beige head, olive-green tie.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.902 #040607:0.041 #c9c9c4:0.029 #2b4952:0.014 #6f8c68:0.014
- **Hierarchy:** Figure then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0579; exits EP0580.
- **Narration (ASR, unverified):** And whoever buys next starts
- **Story function (INFERRED):** INFERRED: next buyer scenario.
- **Continuity:** S0375, S0408.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0408 — f17746-17767 (739.458-740.333 s, 22 frames, 0.92 s) — shot SH156 (inferred) — F2
- **Evidence:** frames/ep_stable/e0580.jpg; entry EP0580, exit EP0581; second review: MINOR
- **Objects/placement (OBSERVED):** Larger worried green-tie figure with bald beige head, hand at chest (x0.18-0.39,y0.25-1.00); larger blue mansion with trees at right (x0.49-0.91,y0.21-0.63).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; round beige head, olive-green tie. Worried brow.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.810 #030405:0.084 #ccc8c0:0.067 #214656:0.020 #617d5a:0.019
- **Hierarchy:** Face, then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0580; exits EP0581.
- **Narration (ASR, unverified):** starts over at full price.
- **Story function (INFERRED):** INFERRED: fresh buyer faces price.
- **Continuity:** S0407.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0409 — f17768-17786 (740.375-741.125 s, 19 frames, 0.79 s) — shot SH156 (inferred) — F2
- **Evidence:** frames/ep_stable/e0581.jpg; entry EP0581, exit EP0582; second review: MINOR
- **Objects/placement (OBSERVED):** Worried green-tie figure at left (x0.18-0.38,y0.25-1.00); large cream TAX paper over the partly hidden mansion and trees at right (x0.55-0.77,y0.26-0.74).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick black outline, flat fills; round beige head, olive-green tie.
- **Typography:** Red TAX caps on paper.
- **Readable text:** TAX
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.773 #e0d7b9:0.114 #050504:0.079 #4d624b:0.026 #9b938a:0.007
- **Hierarchy:** Paper then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0581; exits EP0582.
- **Narration (ASR, unverified):** full price.
- **Story function (INFERRED):** INFERRED: full-price tax on new buyer.
- **Continuity:** S0408.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0410 — f17787-17873 (741.167-744.750 s, 87 frames, 3.62 s) — shot SH157 (inferred) — F2
- **Evidence:** frames/ep_stable/e0582.jpg; entry EP0582, exit EP0583; second review: MINOR
- **Objects/placement (OBSERVED):** Small blue mansion with trees at left (x0.09-0.27,y0.30-0.49) and curly-grey-haired figure with hand to head (x0.28-0.43,y0.17-0.75); rest empty.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, curly grey hair, content face.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.949 #040607:0.021 #676a67:0.012 #bbbdbd:0.011 #2b3e47:0.007
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0582; exits EP0583.
- **Narration (ASR, unverified):** So what we have is the typical homeowner has every reason not to sell.
- **Story function (INFERRED):** INFERRED: homeowner who won't sell.
- **Continuity:** S0413.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0411 — f17874-17884 (744.792-745.208 s, 11 frames, 0.46 s) — shot SH157 (inferred) — F2
- **Evidence:** frames/ep_stable/e0583.jpg; entry EP0583, exit EP0584; second review: MINOR
- **Objects/placement (OBSERVED):** Same owner (x0.28-0.43,y0.17-0.75) and small mansion (x0.09-0.27,y0.30-0.49) at left; small topknot figure with hammer at right (x0.69-0.84,y0.17-0.77).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thin pale figure with topknot, hammer.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.924 #050506:0.032 #c9c7be:0.020 #6a6c69:0.015 #2d3b42:0.009
- **Hierarchy:** Owner then builder.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0583 additive; exits EP0584 motion.
- **Narration (ASR, unverified):** The builders
- **Story function (INFERRED):** INFERRED: builder arrives.
- **Continuity:** S0410.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0412 — f17913-17935 (746.417-747.333 s, 23 frames, 0.96 s) — shot SH158 (inferred) — F9
- **Evidence:** frames/ep_stable/e0584.jpg; entry EP0584, exit EP0585; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed green United-States-shaped map with two big googly eyes and a smile; edges show white water.
- **Background:** Full-bleed green map.
- **Illustration:** Flat green, thick black outlines, white eyes.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #47a44f:0.787 #fcfcfc:0.114 #020703:0.086 #335835:0.010 #a7a6a7:0.003
- **Hierarchy:** Face.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0584 cut; exits by hard cut EP0585.
- **Narration (ASR, unverified):** and the government's help ends
- **Story function (INFERRED):** INFERRED: personified country.
- **Continuity:** none
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0413 — f17936-17948 (747.375-747.875 s, 13 frames, 0.54 s) — shot SH159 (inferred) — F2
- **Evidence:** frames/ep_stable/e0585.jpg; entry EP0585, exit EP0586; second review: MINOR
- **Objects/placement (OBSERVED):** Curly-grey-haired owner with hand to head (x0.31-0.48,y0.25-0.82) and small blue mansion with two trees (x0.125-0.33,y0.34-0.55).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Same owner.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.946 #050607:0.023 #676a67:0.013 #babebd:0.012 #2b434c:0.006
- **Hierarchy:** Owner.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0585 hard replace; exits EP0586.
- **Narration (ASR, unverified):** ends up in the
- **Story function (INFERRED):** INFERRED: back to owner.
- **Continuity:** S0410.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0414 — f17949-17977 (747.917-749.083 s, 29 frames, 1.21 s) — shot SH159 (inferred) — F2
- **Evidence:** frames/ep_stable/e0586.jpg; entry EP0586, exit EP0588; second review: MINOR
- **Objects/placement (OBSERVED):** Owner (x0.31-0.48,y0.25-0.82) and small mansion with trees (x0.125-0.33,y0.34-0.55); dark briefcase stuffed with green bills below the mansion (x0.17-0.34,y0.66-0.83).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Briefcase dark with green bills.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.923 #040606:0.033 #3a3f3c:0.016 #6b7169:0.015 #bbbebd:0.012
- **Hierarchy:** Briefcase.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0586; micro EP0587; exits EP0588.
- **Narration (ASR, unverified):** the seller's pocket,
- **Story function (INFERRED):** INFERRED: money to seller.
- **Continuity:** S0413.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0178 (ADDITIVE_ENTRY, f17961) A tiny brown pouch with dangling lines appears at right, mid-height.

## S0415 — f17978-18169 (749.125-757.083 s, 192 frames, 8.00 s) — shot SH160 (inferred) — F6
- **Evidence:** frames/ep_stable/e0588.jpg; entry EP0588, exit EP0594; second review: MINOR
- **Objects/placement (OBSERVED):** Line chart of first-time buyer share (x0.14-0.86,y0.12-0.89) with grey recession band and NAR logo at lower right; frowning dark-haired figure with long diagonal pointer at lower centre-right (x0.41-0.58,y0.51-1.00); red circle at the last point and red arrow at left are reported mid-state, not in the tile.
- **Background:** White chart image with title, axes and source line.
- **Illustration:** Blue data line with dot markers; figure thick-outlined, peach head, frown.
- **Typography:** Sans chart title ~1.7% height, axis labels ~1%; red arrow and circle are doodles.
- **Readable text:** Share of first-time home buyers, 1981-2025; First-time home buyers dropped to the lowest historical share since data collection began in 1981, dropping to just 21%; labels 44%, 30%, 50%, 21%; Great Recession: December 2007 to June 2009
- **Unreadable/uncertain text:** Axis ticks and source credit line
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.932 #e6d5c7:0.036 #a1a3a8:0.015 #59606c:0.009 #0f0b0a:0.007
- **Hierarchy:** Line shape then figure and red marks.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard replace EP0588; micro events EP0589-EP0593 move pointer and add circle and arrow; exits via EP0594. 8 s hold.
- **Narration (ASR, unverified):** which is how first -time buyers fell to just 21 % of home purchases, the lowest share since the Realtors Association started counting in 1980.
- **Story function (INFERRED):** INFERRED: shows first-time buyer share falling to 21%.
- **Continuity:** Related chart styles S0417-S0422.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0179 (POSE_SWAP, f18024) Pointer in figure's hand changes angle and a red line segment appears at lower right of the chart; arm/pointer shift.; EVI0180 (HIGHLIGHT_ADD, f18071) A red circle is drawn around the final data point at the right end of the chart, and pointer shifts.; EVI0181 (ADDITIVE_ENTRY, f18129) A red arrow appears at upper left of the chart pointing at the start of the line.; EVI0182 (ELEMENT_EXIT, f18135) The red arrow at upper left of the chart disappears.; EVI0183 (ADDITIVE_ENTRY, f18140) The red arrow at upper left reappears pointing at the start of the line.

## S0416 — f18223-18236 (759.333-759.875 s, 14 frames, 0.58 s) — shot SH161 (inferred) — F5
- **Evidence:** frames/ep_stable/e0594.jpg; entry EP0594, exit EP0597; second review: MINOR
- **Objects/placement (OBSERVED):** News-release page (x0.23-0.85,y0.05-1.00): logo top-left, blue headline, red highlight bar behind 'Median Age Rises to', bold subhead and dateline text; brown cowboy-hat figure at lower right (x0.66-0.86,y0.30-1.00).
- **Background:** White web page.
- **Illustration:** Hat figure thick outline, brown hat, light skin, small smile.
- **Typography:** Sans blue headline ~3.5% height; red highlight bar behind second line.
- **Readable text:** First-Time Home Buyer Share Falls to Historic Low of 21%, Median Age Rises to 40; Approximately nine in 10 buyers and sellers worked with a real estate agent
- **Unreadable/uncertain text:** Body paragraphs
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfcfc:0.878 #c7c3c2:0.049 #1e1916:0.031 #677d8a:0.031 #d7636e:0.012
- **Hierarchy:** Headline then highlight.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0594 (scale/drift with hat figure entering); micro EP0595-EP0596 highlight bar; exits EP0597. 14 frames.
- **Narration (ASR, unverified):** years old.
- **Story function (INFERRED):** INFERRED: release headline about age 40.
- **Continuity:** S0415 data.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0184 (HIGHLIGHT_ADD, f18227) Tiny change in the red highlight bar behind 'Median Age Rises to 40' (cursor/edge) at left centre.; EVI0185 (HIGHLIGHT_ADD, f18232) Red highlight extends over the final characters '40' of the headline at left.

## S0417 — f18237-18271 (759.917-761.333 s, 35 frames, 1.46 s) — shot SH162 (inferred) — F6
- **Evidence:** frames/ep_stable/e0597.jpg; entry EP0597, exit EP0598; second review: MINOR
- **Objects/placement (OBSERVED):** Full-frame teal line chart with bold title and subtitle at top (x0.19-0.81,y0.03-0.93), axis labels grey.
- **Background:** White chart.
- **Illustration:** Teal data line, light gridlines.
- **Typography:** Sans bold title ~2.4% height black; labels grey ~1%.
- **Readable text:** Typical Household Would Need to Spend 38% of Income to Afford Housing; Share of monthly income the median-earning U.S. household would spend on monthly mortgage payments for the median-priced U.S. home; Source: Redfin analysis, Created with Datawrapper; 19%; 38%; years 2014-2026
- **Unreadable/uncertain text:** Axis ticks, source text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.962 #b4bebf:0.017 #649b9f:0.009 #0c0c0c:0.007 #525252:0.006
- **Hierarchy:** Title then rising line.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0597; exits EP0598.
- **Narration (ASR, unverified):** By Redfin's analysis,
- **Story function (INFERRED):** INFERRED: shows the 38%.
- **Continuity:** S0418-S0422.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0418 — f18272-18318 (761.375-763.292 s, 47 frames, 1.96 s) — shot SH162 (inferred) — F5
- **Evidence:** frames/ep_stable/e0598.jpg; entry EP0598, exit EP0599; second review: MINOR
- **Objects/placement (OBSERVED):** Teal line chart full frame with bold title, plus a small family doodle at lower right: baby with teddy bear (x0.60-0.67,y0.60-0.80) and two adults holding hands (x0.67-0.80,y0.50-0.82).
- **Background:** White chart.
- **Illustration:** Doodle thick outline.
- **Typography:** Same chart type.
- **Readable text:** Typical Household Would Need to Spend 38% of Income to Afford Housing; Share of monthly income the median-earning U.S. household would spend on monthly mortgage payments for the median-priced U.S. home; Source: Redfin analysis, Created with Datawrapper
- **Unreadable/uncertain text:** Axis text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.938 #8a9d9d:0.021 #c9cfcd:0.017 #0f0c0b:0.013 #55514f:0.011
- **Hierarchy:** Chart then family.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0598; exits EP0599.
- **Narration (ASR, unverified):** the typical household would have to spend 38
- **Story function (INFERRED):** INFERRED: the household.
- **Continuity:** S0417.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0419 — f18319-18377 (763.333-765.750 s, 59 frames, 2.46 s) — shot SH162 (inferred) — F5
- **Evidence:** frames/ep_stable/e0599.jpg; entry EP0599, exit EP0600; second review: MINOR
- **Objects/placement (OBSERVED):** Teal housing-cost chart (x0.19-0.81,y0.05-0.92) with large shocked dark-haired face, open mouth, hand and arm at chin at left (x0.09-0.30,y0.36-1.00); family doodle at lower right (x0.60-0.80,y0.50-0.79); red circle around the 38% endpoint (x0.77-0.81,y0.26-0.37).
- **Background:** White chart.
- **Illustration:** Face wide-eyed, open mouth.
- **Typography:** Chart title ~2%.
- **Readable text:** Typical Household Would Need to Spend 38% of Income to Afford Housing
- **Unreadable/uncertain text:** Axis text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.869 #ecd1bb:0.060 #0b0807:0.030 #959d9c:0.027 #56504d:0.014
- **Hierarchy:** Face then circle.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0599; exits EP0600.
- **Narration (ASR, unverified):** 38 % of its income just on the
- **Story function (INFERRED):** INFERRED: shock at 38%.
- **Continuity:** S0420.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0420 — f18378-18422 (765.792-767.625 s, 45 frames, 1.88 s) — shot SH162 (inferred) — F5
- **Evidence:** frames/ep_stable/e0600.jpg; entry EP0600, exit EP0602; second review: MINOR
- **Objects/placement (OBSERVED):** As S0419 plus a cream stack of pages headed MORTGAGE in red caps with scribble lines and a signature, right of the face (x0.375-0.51,y0.38-0.71); red circle at 38% (x0.77-0.81,y0.26-0.37).
- **Background:** White chart.
- **Illustration:** Doc cream with squiggles.
- **Typography:** Red caps.
- **Readable text:** MORTGAGE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.829 #ead6c0:0.087 #0b0807:0.039 #9a9b99:0.028 #5c504d:0.017
- **Hierarchy:** Face, document.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0600; micro EP0601; exits EP0602.
- **Narration (ASR, unverified):** the mortgage for the typical home.
- **Story function (INFERRED):** INFERRED: monthly mortgage cost.
- **Continuity:** S0419.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0186 (ADDITIVE_ENTRY, f18392) A small house doodle appears at upper right beside the red circle around 38%.

## S0421 — f18438-18453 (768.292-768.917 s, 16 frames, 0.67 s) — shot SH162 (inferred) — F6
- **Evidence:** frames/ep_stable/e0602.jpg; entry EP0602, exit EP0603; second review: MINOR
- **Objects/placement (OBSERVED):** Chart enlarged to near full frame (x0.18-0.98,y0.07-0.83) with a purple vertical bar at the line's start (x0.27,y0.44-0.78); '19%' tag at left and '38%' at line end.
- **Background:** White chart.
- **Illustration:** Magenta bar.
- **Typography:** Axis grey ~1.2%.
- **Readable text:** 19%; 38%; 2014-2026
- **Unreadable/uncertain text:** Source credit
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.967 #b6c8cb:0.016 #50a7ad:0.010 #666667:0.005 #c420d3:0.003
- **Hierarchy:** Purple bar.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0602 zoom; exits EP0603.
- **Narration (ASR, unverified):** 2012,
- **Story function (INFERRED):** INFERRED: from 2012 point.
- **Continuity:** S0422.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0422 — f18464-18483 (769.375-770.167 s, 20 frames, 0.83 s) — shot SH162 (inferred) — F6
- **Evidence:** frames/ep_stable/e0603.jpg; entry EP0603, exit EP0604; second review: MINOR
- **Objects/placement (OBSERVED):** Chart (x0.09-0.88,y0.07-0.83) with two purple bars: left at the start (x0.175,y0.44-0.78) and right at the end (x0.85,y0.14-0.78); labels 19% and 38%.
- **Background:** White chart.
- **Illustration:** Magenta bars.
- **Typography:** Axis ~1.2%.
- **Readable text:** 19%; 38%; 2014-2026
- **Unreadable/uncertain text:** Source credit
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.962 #b7c8ce:0.016 #53a3ac:0.009 #c018d1:0.009 #5d5c5d:0.004
- **Hierarchy:** Two bars.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0603 bar motion; exits EP0604 cut.
- **Narration (ASR, unverified):** has doubled.
- **Story function (INFERRED):** INFERRED: doubling.
- **Continuity:** S0421.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0423 — f18484-18567 (770.208-773.667 s, 84 frames, 3.50 s) — shot SH163 (inferred) — F2
- **Evidence:** frames/ep_stable/e0604.jpg; entry EP0604, exit EP0606; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling pointer-holding figure at left (x0.07-0.30,y0.25-0.93) and large blank green chalkboard in a brown frame at right (x0.38-0.94,y0.11-0.72); chalk text reported late in the state is not visible in the tile.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Board green with brown frame; chalk text.
- **Typography:** Handwritten white chalk ~2% height.
- **Readable text:** No more than 30%
- **Unreadable/uncertain text:** Chalk text reported late in the state (first reviewer: 'No more than 30%') is not visible in this tile; unverified.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.615 #38843f:0.195 #6f534a:0.084 #060503:0.072 #efd1b7:0.034
- **Hierarchy:** Board then text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0604; micro EP0605 text; exits EP0606.
- **Narration (ASR, unverified):** The usual rule of thumb is don't spend more than 30%. Past
- **Story function (INFERRED):** INFERRED: 30% rule.
- **Continuity:** Plain pointer figure S0399.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0187 (TEXT_CHANGE, f18522) White handwritten text appears on the chalkboard (mid-board) and pointer lifts.

## S0424 — f18599-18631 (775.000-776.333 s, 33 frames, 1.38 s) — shot SH164 (inferred) — F5
- **Evidence:** frames/ep_stable/e0606.jpg; entry EP0606, exit EP0607; second review: OK
- **Objects/placement (OBSERVED):** Shrunken teal line chart with title at upper left (x0.07-0.52,y0.05-0.85); blue definition card with a snow-globe house picture at right (x0.53-0.94,y0.36-0.85).
- **Background:** White chart page.
- **Illustration:** Card flat sky-blue with white-on-blue text and a glass-globe house image; chart thin teal line.
- **Typography:** Card heading bold sans ~3% height black on blue; chart text ~1%.
- **Readable text:** House Poor; Spending a large proportion of total income on homeownership.
- **Unreadable/uncertain text:** Chart axis labels and source line
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.775 #8db8f7:0.162 #bed1e7:0.024 #6e86a2:0.020 #22314d:0.019
- **Hierarchy:** Blue card (saturated block) first, then the small chart.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0606 (chart page appears and card slides in from right); exits by hard cut EP0607.
- **Narration (ASR, unverified):** considered house poor.
- **Story function (INFERRED):** INFERRED: defines the term 'house poor' after the 30% rule.
- **Continuity:** Chart from S0417-S0422.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0425 — f18632-18666 (776.375-777.792 s, 35 frames, 1.46 s) — shot SH165 (inferred) — F1
- **Evidence:** frames/ep_stable/e0607.jpg; entry EP0607, exit EP0608; second review: OK
- **Objects/placement (OBSERVED):** Single plain skeptical figure centred (x0.40-0.57,y0.18-0.88): peach head with spiky dark hair, flat mouth and tilted brows, one arm raised.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thin line body, flat peach head.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.032 #080504:0.011 #948d88:0.002 #4a423b:0.002
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0607; exits EP0608.
- **Narration (ASR, unverified):** So who's still getting in?
- **Story function (INFERRED):** INFERRED: narrator beat on the question 'who is getting in'.
- **Continuity:** Plain figure family S0372, S0380, S0406.
- **Confidence:** HIGH; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0426 — f18667-18693 (777.833-778.917 s, 27 frames, 1.12 s) — shot SH166 (inferred) — F2
- **Evidence:** frames/ep_stable/e0608.jpg; entry EP0608, exit EP0609; second review: MINOR
- **Objects/placement (OBSERVED):** Large blonde-haired figure with tongue out in stride pose (x0.09-0.54,y0.05-1.00), pink piggy bank held out at its left side (x0.09-0.30,y0.55-0.83).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, golden bob hair, peach face, pink pig.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.833 #d1bb84:0.073 #070404:0.047 #dbb7b0:0.040 #61564f:0.008
- **Hierarchy:** Face then piggy bank.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0608; exits EP0609.
- **Narration (ASR, unverified):** It's not the people who save their
- **Story function (INFERRED):** INFERRED: savers.
- **Continuity:** S0427.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0427 — f18694-18724 (778.958-780.208 s, 31 frames, 1.29 s) — shot SH166 (inferred) — F2
- **Evidence:** frames/ep_stable/e0609.jpg; entry EP0609, exit EP0610; second review: MINOR
- **Objects/placement (OBSERVED):** Blonde figure with tongue out (x0.09-0.61,y0.05-1.00), pink piggy bank at left (x0.09-0.30,y0.55-0.83) and a large green banknote held down at right (x0.46-0.61,y0.54-0.86).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Same figure; bill added with thick outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.812 #d1bd83:0.073 #090705:0.052 #dbb7b0:0.040 #769269:0.023
- **Hierarchy:** Face then bill.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0609 additive; exits EP0610.
- **Narration (ASR, unverified):** save their money for years, cut
- **Story function (INFERRED):** INFERRED: saving money.
- **Continuity:** S0426.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0428 — f18725-18754 (780.250-781.458 s, 30 frames, 1.25 s) — shot SH167 (inferred) — F2
- **Evidence:** frames/ep_stable/e0610.jpg; entry EP0610, exit EP0612; second review: MINOR
- **Objects/placement (OBSERVED):** Smaller orange curly-haired figure seated low at left holding a yellow coin (x0.19-0.33,y0.40-0.88) beside a pink piggy bank (x0.37-0.48,y0.72-0.86).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thin outline, orange hair, small pig.
- **Typography:** Tiny handwritten caption ~1.5% height.
- **Readable text:** rice for dinner again (low-confidence reading)
- **Unreadable/uncertain text:** A tiny handwritten caption reportedly appears mid-state; it is not visible in the tile and the first reading is unverified.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.959 #0b0404:0.015 #d59b7d:0.014 #debabd:0.009 #665855:0.004
- **Hierarchy:** Figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0610; micro EP0611; exits EP0612.
- **Narration (ASR, unverified):** cut back on spending,
- **Story function (INFERRED):** INFERRED: cutting back on spending.
- **Continuity:** S0426.
- **Confidence:** LOW; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0188 (TEXT_CHANGE, f18742) Tiny handwritten caption appears to the right of the small figure's head (brief speech text).

## S0429 — f18755-18778 (781.500-782.458 s, 24 frames, 1.00 s) — shot SH168 (inferred) — F2
- **Evidence:** frames/ep_stable/e0612.jpg; entry EP0612, exit EP0613; second review: MINOR
- **Objects/placement (OBSERVED):** Dark-haired figure seated in a grey office chair at a black desk with a laptop marked CF (x0.49-0.88,y0.25-0.89); rest empty.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, black desk, grey chair, laptop.
- **Typography:** Laptop shows a small CF mark in sans caps.
- **Readable text:** CF (laptop mark)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.877 #090708:0.065 #363636:0.028 #666666:0.017 #b5aea7:0.013
- **Hierarchy:** Figure at desk.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0612; exits EP0613.
- **Narration (ASR, unverified):** or make the other common sacrifices
- **Story function (INFERRED):** INFERRED: working hard.
- **Continuity:** S0430, S0431.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0430 — f18779-18805 (782.500-783.583 s, 27 frames, 1.12 s) — shot SH168 (inferred) — F2
- **Evidence:** frames/ep_stable/e0613.jpg; entry EP0613, exit EP0614; second review: MINOR
- **Objects/placement (OBSERVED):** Dark-haired figure at a black desk with a laptop marked CF (x0.49-0.88,y0.25-0.89), handwritten caption at upper left of its head (x0.54-0.69,y0.21-0.28).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Same.
- **Typography:** Handwritten ~2.3% height dark.
- **Readable text:** I'm tired...; CF (laptop mark)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.875 #0a0708:0.066 #363636:0.028 #666666:0.017 #b4aea8:0.013
- **Hierarchy:** Caption then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0613 additive; exits EP0614.
- **Narration (ASR, unverified):** sacrifices to try
- **Story function (INFERRED):** INFERRED: fatigue from sacrifices.
- **Continuity:** S0429.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0431 — f18806-18837 (783.625-784.917 s, 32 frames, 1.33 s) — shot SH168 (inferred) — F2
- **Evidence:** frames/ep_stable/e0614.jpg; entry EP0614, exit EP0615; second review: MINOR
- **Objects/placement (OBSERVED):** Desk figure with CF laptop at right (x0.49-0.88,y0.25-0.89) and a thought bubble with small trailing circles at left holding a teal house drawing (cloud x0.17-0.46,y0.21-0.60; trailing bubbles to x0.62).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Thick outline, bubble with scalloped edge.
- **Typography:** none
- **Readable text:** CF (laptop mark)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.822 #080707:0.094 #363737:0.033 #b7c5bf:0.030 #676867:0.022
- **Hierarchy:** Bubble then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0614; exits via EP0615 transition.
- **Narration (ASR, unverified):** try and purchase a home.
- **Story function (INFERRED):** INFERRED: dream of buying.
- **Continuity:** S0429.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0432 — f18854-18903 (785.625-787.667 s, 50 frames, 2.08 s) — shot SH169 (inferred) — F4
- **Evidence:** frames/ep_stable/e0615.jpg; entry EP0615, exit EP0616; second review: MINOR
- **Objects/placement (OBSERVED):** Article crop (x0.08-0.92,y0.07-0.67): dateline and breadcrumb at upper left, house photo band at upper right (x0.52-0.91), paragraph at left with only its first word starting to turn green-highlighted, share icons in the middle, author box at right.
- **Background:** White news page.
- **Illustration:** UI screenshot; green marker highlight.
- **Typography:** Serif body ~2% height dark grey.
- **Readable text:** September 6, 2023, 5:07pm by Chris Clow; News > Mortgage; Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift from family members or inheritance in order to afford a down payment on a new home purchase...; Redfin
- **Unreadable/uncertain text:** Author box text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.701 #dfdfdb:0.183 #a6aca8:0.046 #687375:0.043 #253845:0.027
- **Hierarchy:** Highlight.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0615; exits EP0616.
- **Narration (ASR, unverified):** 40 % of first -time home buyers under the age of
- **Story function (INFERRED):** INFERRED: gift reliance claim.
- **Continuity:** S0433, S0434.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0433 — f18904-18942 (787.708-789.292 s, 39 frames, 1.62 s) — shot SH169 (inferred) — F5
- **Evidence:** frames/ep_stable/e0616.jpg; entry EP0616, exit EP0617; second review: MINOR
- **Objects/placement (OBSERVED):** Same article (x0.08-0.92,y0.07-0.67) with the first line green-highlighted; curly-dark-haired smirking figure holding a phone at its left and a green bill at its right (x0.54-0.91,y0.36-1.00).
- **Background:** White news page.
- **Illustration:** Thick outline; curly dark hair.
- **Typography:** Serif ~2%.
- **Readable text:** Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift from family members or inheritance
- **Unreadable/uncertain text:** Rest
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.628 #e0e0dc:0.180 #24272a:0.073 #b9c1a9:0.061 #6b7b75:0.058
- **Hierarchy:** Highlight then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0616; exits EP0617.
- **Narration (ASR, unverified):** of 30 used either a cash gift
- **Story function (INFERRED):** INFERRED: young buyer.
- **Continuity:** S0432.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0434 — f18943-19025 (789.333-792.750 s, 83 frames, 3.46 s) — shot SH169 (inferred) — F5
- **Evidence:** frames/ep_stable/e0617.jpg; entry EP0617, exit EP0619; second review: MINOR
- **Objects/placement (OBSERVED):** Article (x0.08-0.92,y0.06-0.67) with green highlight over first two lines; open-mouthed surprised curly-haired figure holding a phone (left) and a green bill (right) at lower right (x0.60-0.92,y0.35-1.00).
- **Background:** White news page.
- **Illustration:** Thick outline; hand-lettered bubble.
- **Typography:** Serif article ~1.6%; bubble ~1.8% handwritten.
- **Readable text:** Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift from family members or inheritance (highlighted)
- **Unreadable/uncertain text:** Speech bubble reportedly added mid-state is not visible in the tile; unverified. Rest of article text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #f9faf9:0.637 #dbdad5:0.202 #252929:0.075 #72827c:0.063 #b2e77e:0.022
- **Hierarchy:** Highlight, figure, bubble.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0617; micro EP0618; exits EP0619.
- **Narration (ASR, unverified):** cash gift from family members or inheritance for their down payment. The
- **Story function (INFERRED):** INFERRED: example of gift use.
- **Continuity:** S0433.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.
- **Intra-state events:** EVI0189 (ADDITIVE_ENTRY, f18976) A speech bubble with handwritten caption appears at lower centre of the article.

## S0435 — f19026-19058 (792.792-794.125 s, 33 frames, 1.38 s) — shot SH170 (inferred) — F3
- **Evidence:** frames/ep_stable/e0619.jpg; entry EP0619, exit EP0620; second review: MINOR
- **Objects/placement (OBSERVED):** Pale columned government building with triangular pediment lettered FEDERAL RESERVE (x0.34-0.68,y0.26-0.68), tall columns and stepped base; rest empty.
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Cream building, thick outline, tan columns.
- **Typography:** Pediment small caps ~1.5%.
- **Readable text:** FEDERAL RESERVE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.906 #dadcbc:0.035 #060503:0.029 #95957c:0.023 #4c4b3d:0.007
- **Hierarchy:** Building.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard cut EP0619; exits EP0620.
- **Narration (ASR, unverified):** The Federal Reserve even published
- **Story function (INFERRED):** INFERRED: central bank introduction.
- **Continuity:** S0436, S0437.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0436 — f19059-19066 (794.167-794.458 s, 8 frames, 0.33 s) — shot SH170 (inferred) — F3
- **Evidence:** frames/ep_stable/e0620.jpg; entry EP0620, exit EP0621; second review: MINOR
- **Objects/placement (OBSERVED):** Same building with two white cartoon eyes in the doorway (x0.33-0.70,y0.24-0.69).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Eyes white with black pupils.
- **Typography:** Pediment text.
- **Readable text:** FEDERAL RESERVE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.888 #dbdcbd:0.042 #050503:0.037 #95947c:0.025 #47463b:0.007
- **Hierarchy:** Eyes.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0620 additive; exits EP0621. 8 frames.
- **Narration (ASR, unverified):** published a
- **Story function (INFERRED):** INFERRED: character.
- **Continuity:** S0435.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0437 — f19067-19075 (794.500-794.833 s, 9 frames, 0.38 s) — shot SH170 (inferred) — F3
- **Evidence:** frames/ep_stable/e0621.jpg; entry EP0621, exit EP0622; second review: MINOR
- **Objects/placement (OBSERVED):** Cartoon-eyed building with FEDERAL RESERVE pediment (x0.32-0.70,y0.24-0.70) and a cream paper headed STUDY with three squiggle lines, the heading grey-highlighted, at its left (x0.12-0.28,y0.18-0.53).
- **Background:** Empty off-white canvas (#FCFCFC).
- **Illustration:** Paper cream with title and squiggles.
- **Typography:** Handwritten caps.
- **Readable text:** STUDY; FEDERAL RESERVE
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.833 #dedbc4:0.084 #060503:0.047 #94937c:0.027 #4a493e:0.009
- **Hierarchy:** Paper then building.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by EP0621 additive; exits EP0622 (report paper added, outside shard). 9 frames.
- **Narration (ASR, unverified):** a working paper
- **Story function (INFERRED):** INFERRED: working paper.
- **Continuity:** S0436.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: objects, positions and legible text from the stable-frame state sheet and boundary sheets; INFERRED: story function and meaning from unverified ASR.

## S0438 — f19076-19108 (794.875-796.208 s, 33 frames, 1.38 s) — shot SH170 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0622.jpg; entry EP0622, exit EP0623; second review: MINOR
- **Objects/placement (OBSERVED):** Left: beige 'STUDY' sheet with squiggles (x .12-.28, y .1-.5). Centre: columned building with googly eyes and roof plaque 'FEDERAL RESERVE' (x .33-.7, y .25-.7, largest). Right: grey 'REPORT' sheet with scribbles (x .73-.9, y .4-.85).
- **Background:** flat off-white canvas
- **Illustration:** Thick black outlines, flat cream/olive fills, hand-drawn googly-eyed anthropomorphic building; paper props with wavy scribble lines.
- **Typography:** Hand-lettered marker caps on props ('STUDY', 'REPORT') and a sign on the roof; black, ~5% height, bold.
- **Readable text:** STUDY; REPORT; FEDERAL RESERVE (roof plaque)
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.805 #dddbc6:0.092 #060503:0.061 #94937e:0.030 #49483f:0.012
- **Hierarchy:** Eye hits the eyed building first (centre, largest), then the two flanking papers by symmetry.
- **Camera/motion:** STATIC 2D; **entry/exit:** Begins on EP0620-0622 additive pops; ends by hard replace EP0623.
- **Narration (ASR, unverified):** paper on this last year.
- **Story function (INFERRED):** INFERRED: introduces the central-bank research paper as source before opening it.
- **Continuity:** Building and paper props reappear in earlier states of the same shot (before S0438); PDF content follows in S0439.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0439 — f19109-19144 (796.250-797.708 s, 36 frames, 1.50 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0623.jpg; entry EP0623, exit EP0624; second review: OK
- **Objects/placement (OBSERVED):** Left: PDF viewer screenshot with dark toolbar and thumbnails (x .03-.52, y .08-.75). Bottom right: smiling bespectacled stick presenter at brown desk with open laptop bearing a logo (x .5-1, y .45-1).
- **Background:** flat off-white canvas with dark-framed document capture
- **Illustration:** Presenter has round head, tiny glasses, simple smile, line-drawn body; desk flat brown, laptop grey; PDF is a raw screenshot.
- **Typography:** UI toolbar tiny sans; document serif tiny; laptop logo 'CF' hand-lettered.
- **Readable text:** none
- **Unreadable/uncertain text:** Document header text unreadable; title line only faint.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.729 #2a2b2a:0.101 #7c716c:0.086 #e3cebd:0.048 #050202:0.036
- **Hierarchy:** Eye goes to presenter (big, saturated) then document thumbnail at left.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace in EP0623; leaves via zoom motion EP0624.
- **Narration (ASR, unverified):** And I'm not making this up. The title
- **Story function (INFERRED):** INFERRED: presenter reads the paper at his laptop, establishing the document source.
- **Continuity:** Same presenter at desk used in earlier shots; PDF reappears in S0440-S0445.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0440 — f19165-19236 (798.583-801.542 s, 72 frames, 3.00 s) — shot SH171 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0624.jpg; entry EP0624, exit EP0625; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed PDF viewer: dark toolbar across top, thumbnail rail at left (x 0-.18) and white document page (x .2-.97) with serif title block, a blue-highlighted title line at centre-left, author line and cite box.
- **Background:** dark UI chrome around white page
- **Illustration:** Raw screenshot, no illustration.
- **Typography:** Serif document text 1-3% height, black; toolbar sans tiny grey.
- **Readable text:** Illiquid Homeownership and the Bank of Mom and Dad (highlighted title)
- **Unreadable/uncertain text:** Series header, ISSN lines, author, cite box.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.693 #252626:0.200 #3c3c3d:0.061 #bfc3c9:0.031 #878c90:0.015
- **Hierarchy:** Highlighted title line is the focal point; dark rail frames page.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered via zoom EP0624; exits with additive presenter EP0625.
- **Narration (ASR, unverified):** Illiquid Homeownership and the Bank of Mom and Dad.
- **Story function (INFERRED):** INFERRED: shows the paper title the speaker is quoting.
- **Continuity:** Same document continues S0441-S0445.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0441 — f19237-19262 (801.583-802.625 s, 26 frames, 1.08 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0625.jpg; entry EP0625, exit EP0627; second review: OK
- **Objects/placement (OBSERVED):** Document viewer fills most of frame (x .02-.97, y 0-1) with the same title page; frowning presenter with long brown pointer stick pops at lower left (x .06-.4, y .55-1).
- **Background:** dark UI chrome + white page
- **Illustration:** Presenter: round head, down-turned mouth, thin stick limbs, thick brown pointer; flat.
- **Typography:** Serif doc text small; no overlay text.
- **Readable text:** Illiquid Homeownership and the Bank of Mom and Dad
- **Unreadable/uncertain text:** author/cite lines
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.674 #232524:0.186 #3d3d3d:0.064 #e2d0c1:0.052 #969ba2:0.025
- **Hierarchy:** Presenter face (high contrast) then highlighted title.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered additively via EP0625; micro EP0626 inside; ends motion EP0627 (scroll).
- **Narration (ASR, unverified):** That's a real paper published
- **Story function (INFERRED):** INFERRED: presenter points at paper title while saying it is a real paper.
- **Continuity:** Presenter reused S0442-S0444.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0190 (DRAW_ON_OR_REVEAL, f19244) Red underline stroke is drawn under a title line in a PDF paper header (x~0.32-0.80,y~0.45-0.47); EVI0191 (OTHER, f19247) Only a hairline change on the highlighted title line of the PDF page (centre); nothing nameable visible at tile size, presenter unchanged.

## S0442 — f19270-19273 (802.958-803.083 s, 4 frames, 0.17 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0627.jpg; entry EP0627, exit EP0628; second review: OK
- **Objects/placement (OBSERVED):** Same viewer, page scrolled so the cite box and a paragraph sit centre (x .35-.85, y .3-.55); frowning presenter at lower left; black page-gap bar below.
- **Background:** dark chrome + white page
- **Illustration:** As S0441.
- **Typography:** Serif tiny.
- **Readable text:** none
- **Unreadable/uncertain text:** cite box, paragraph text.
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.668 #232424:0.191 #3e3d3d:0.063 #e3d1c2:0.052 #9a9ba1:0.026
- **Hierarchy:** Presenter then cite box.
- **Camera/motion:** SCROLL; **entry/exit:** Frame inside scroll animation (EP0627-0628); 4-frame state.
- **Narration (ASR, unverified):** published by
- **Story function (INFERRED):** INFERRED: scroll animation frame, too short to be a message.
- **Continuity:** Same shot S0441.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: mid-scroll frame; INFERRED: transition role.

## S0443 — f19286-19289 (803.625-803.750 s, 4 frames, 0.17 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0628.jpg; entry EP0628, exit EP0629; second review: OK
- **Objects/placement (OBSERVED):** Viewer shows second page: page top with title 'Illiquid Homeownership...' large serif at upper right-centre and abstract beginning; thumbnail rail highlights page 2; frowning presenter lower left; black bar at top of page.
- **Background:** dark chrome + white page
- **Illustration:** As S0441.
- **Typography:** Serif centred title ~3%, body ~1.5%.
- **Readable text:** Illiquid Homeownership and the Bank of Mom and Dad* ; Eirik Eylands Brandsaas; September 15, 2025; Abstract
- **Unreadable/uncertain text:** abstract body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.650 #242424:0.192 #3e3e3e:0.065 #e4d4c6:0.059 #a3a4a7:0.033
- **Hierarchy:** Title then presenter.
- **Camera/motion:** SCROLL; **entry/exit:** Mid-scroll frame between EP0628 and EP0629; 4 frames.
- **Narration (ASR, unverified):** Federal Reserve.
- **Story function (INFERRED):** INFERRED: page-scroll step reaching abstract.
- **Continuity:** S0442/S0444.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0444 — f19299-19302 (804.167-804.292 s, 4 frames, 0.17 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0629.jpg; entry EP0629, exit EP0630; second review: OK
- **Objects/placement (OBSERVED):** Viewer page scrolled further: dense abstract paragraph and a footnote block fill the page, a section heading '1 Introduction' at bottom; presenter frowning at lower left.
- **Background:** dark chrome + white page
- **Illustration:** As S0441.
- **Typography:** Serif body ~1.5%.
- **Readable text:** 1 Introduction
- **Unreadable/uncertain text:** abstract, keywords, footnote paragraphs
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.624 #292a2a:0.253 #e5d6c9:0.064 #b6b7b8:0.041 #888787:0.019
- **Hierarchy:** Presenter then text.
- **Camera/motion:** SCROLL+ZOOM; **entry/exit:** Mid-scroll before the zoom EP0630; 4 frames.
- **Narration (ASR, unverified):** Reserve.
- **Story function (INFERRED):** INFERRED: transitional frame as page enlarges.
- **Continuity:** S0443 and S0445.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0445 — f19334-19451 (805.625-810.500 s, 118 frames, 4.92 s) — shot SH171 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0630.jpg; entry EP0630, exit EP0631; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed white abstract page: centred 'Abstract' heading (x .45, y .09), justified serif paragraph (x .02-.58, y .12-.9), JEL/keywords at bottom; neutral-faced presenter at right (x .56-.82, y .2-1) with pointer stick; top shows date cut off.
- **Background:** white page
- **Illustration:** Presenter: round head, dot eyes, flat mouth, stick limbs, thin brown pointer.
- **Typography:** Serif body about 2.3% height, black; heading bold.
- **Readable text:** Abstract; Housing is the largest asset in U.S. household portfolios, and first-time homebuyers increasingly rely on parental transfers; JEL: D14, D15, E21, G51, R21; Keywords: Homeownership, Parental transfers, Altruism, Life-cycle models
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.850 #e0d2c6:0.076 #a2a1a1:0.036 #666564:0.027 #0d0a09:0.011
- **Hierarchy:** Abstract text mass fills left; presenter face draws eye at right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by zoom/chrome-out EP0630; exits hard replace EP0631.
- **Narration (ASR, unverified):** that help from parents accounts for about 27 % of young households' homeownership.
- **Story function (INFERRED):** INFERRED: narration cites the 27 percent figure from the abstract.
- **Continuity:** Same abstract page was seen earlier; presenter reused.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0446 — f19452-19494 (810.542-812.292 s, 43 frames, 1.79 s) — shot SH172 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0631.jpg; entry EP0631, exit EP0635; second review: OK
- **Objects/placement (OBSERVED):** Mostly blank canvas; a dark-skinned character's head and sliver of body peeking at upper left (x 0-.2, y .2-.55), worried expression, short black hair.
- **Background:** flat off-white canvas
- **Illustration:** Brown fill head, black outlines, tiny face with raised brows; body only an angled stroke at left edge.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.979 #8f7363:0.008 #070403:0.007 #232120:0.006 #b4b5b4:0.001
- **Hierarchy:** Single character at left edge; large negative space.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0631; text drawn on later via EP0632-0634 (micro events in state).
- **Narration (ASR, unverified):** Roughly one in four young owners is there
- **Story function (INFERRED):** INFERRED: set up for the '1 in 4' stat reveal.
- **Continuity:** Character reused S0447.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: character; the later-added '1 in 4' text appears during this state (EP0632-0634).
- **Intra-state events:** EVI0192 (TEXT_CHANGE, f19461) A single thin vertical stroke (the start of handwritten 'I') appears at top centre of the blank canvas.; EVI0193 (TEXT_CHANGE, f19480) The numeral '4' appears after 'in' at top centre, completing handwritten '1 in 4'.
- **Intra-state motion intervals:** EP0633

## S0447 — f19495-19529 (812.333-813.750 s, 35 frames, 1.46 s) — shot SH172 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0635.jpg; entry EP0635, exit EP0637; second review: MINOR
- **Objects/placement (OBSERVED):** Top: handwritten '1 in 4' (x .31-.5, y .02-.2). Left edge: worried dark-skinned head (x 0-.1, y .1-.4). Hoodie sunglasses figure holding a banknote (x .34-.43, y .4-.95), with tiny caption above him in later frames. Right: large red-roofed house with green bushes (x .5-.83, y .4-.75).
- **Background:** flat off-white canvas
- **Illustration:** Marker lettering black; figure grey flat fill with sunglasses; house multi-colour with bushes; line-and-flat style.
- **Typography:** Hand-printed marker, black, large (~9%), left aligned.
- **Readable text:** 1 in 4
- **Unreadable/uncertain text:** tiny caption above the hoodie figure (looks like 'thanks mama').
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.889 #100b09:0.040 #947c6d:0.037 #c8b8a8:0.019 #595245:0.015
- **Hierarchy:** The stat text draws the eye first, then house (colour mass).
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by hard replace EP0631 and additive EP0635; micro EP0636 caption.
- **Narration (ASR, unverified):** is there because a parent helped.
- **Story function (INFERRED):** INFERRED: one-in-four young owners had parental help; hoodie figure is the helped buyer.
- **Continuity:** Dark character from S0446.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0194 (TEXT_CHANGE, f19513) A tiny handwritten caption ('thanks mama') appears just above the hooded figure at centre-left.

## S0448 — f19530-19603 (813.792-816.833 s, 74 frames, 3.08 s) — shot SH173 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0637.jpg; entry EP0637, exit EP0638; second review: OK
- **Objects/placement (OBSERVED):** Single neutral smiling stick presenter centred (x .38-.55, y .15-.95): round beige head, smile, arms out sideways. Nothing else.
- **Background:** flat off-white canvas
- **Illustration:** Beige head, thick black outlines, dot eyes, simple smile, thin stick limbs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.954 #f4d3b6:0.031 #090605:0.011 #5e5854:0.002 #a8a09b:0.002
- **Hierarchy:** Lone figure centre.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0637; exits by hard replace EP0638.
- **Narration (ASR, unverified):** So what decides who gets in isn't who needs it most.
- **Story function (INFERRED):** INFERRED: question beat 'what decides who gets in'.
- **Continuity:** Presenter reused S0449 and S0462 (variant).
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0449 — f19604-19644 (816.875-818.542 s, 41 frames, 1.71 s) — shot SH173 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0638.jpg; entry EP0638, exit EP0639; second review: OK
- **Objects/placement (OBSERVED):** Left: presenter moved left (x .12-.28), smiling with pointer stick. Right: green chalkboard with thick brown frame (x .4-.99, y .13-.77) reading 'Pro tip: BE BORN RICH' in white chalk-like hand lettering.
- **Background:** flat off-white canvas
- **Illustration:** Board flat green with wood-brown frame, white hand-lettered text; presenter as before.
- **Typography:** Chalk-style handwritten, white on green, ~5% height, centred.
- **Readable text:** Pro tip: BE BORN RICH
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.619 #398440:0.186 #70544a:0.086 #070503:0.073 #e9d0b7:0.036
- **Hierarchy:** Board text first by size/colour, then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Partial replace EP0638; exits by zoom-in table EP0639.
- **Narration (ASR, unverified):** It's who has rich parents. Parents
- **Story function (INFERRED):** INFERRED: punchline: wealth of parents decides who gets in.
- **Continuity:** Presenter from S0448.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0450 — f19672-19707 (819.708-821.167 s, 36 frames, 1.50 s) — shot SH174 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0639.jpg; entry EP0639, exit EP0640; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed academic table: caption at top 'Table 1: Descriptive Statistics (Means), Households Aged 25-44', two blocks of numeric rows with columns Receiver No/Yes under All/Renter/Owner; all black on white.
- **Background:** white
- **Illustration:** Raw document table, no illustration.
- **Typography:** Serif/LaTeX, ~1.6% height, black.
- **Readable text:** Table 1: Descriptive Statistics (Means), Households Aged 25-44; row labels Transfer, Wealth, Wealth Parent, Income, College, White, Owner, Age, Observations
- **Unreadable/uncertain text:** numeric cells
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.894 #e8e8e8:0.037 #c7c7c7:0.027 #a3a3a3:0.023 #757575:0.019
- **Hierarchy:** Centred table as one mass; the bold caption leads.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by scale-in EP0639; exits additive EP0640.
- **Narration (ASR, unverified):** kids money are two and a half times
- **Story function (INFERRED):** INFERRED: data evidence that wealthier parents give more.
- **Continuity:** Table continues S0451-S0452.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0451 — f19708-19742 (821.208-822.625 s, 35 frames, 1.46 s) — shot SH174 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0640.jpg; entry EP0640, exit EP0641; second review: OK
- **Objects/placement (OBSERVED):** Same table; green highlight on a 'Yes' column header and a green cell in the 'Wealth Parent' row; white-haired woman holding cash at lower right (x .8-.99, y .45-1).
- **Background:** white
- **Illustration:** Woman: grey wavy hair, brown skin, tired eyes, holds green banknote; flat colours.
- **Typography:** Same table text.
- **Readable text:** Table 1: Descriptive Statistics (Means), Households Aged 25-44
- **Unreadable/uncertain text:** numeric cells
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.878 #bdbbb5:0.059 #7e8278:0.036 #090907:0.023 #2eec40:0.004
- **Hierarchy:** Green highlights then woman.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0640; exits by additive EP0641.
- **Narration (ASR, unverified):** times as wealthy as parents who
- **Story function (INFERRED):** INFERRED: highlighted wealth-of-parent figure for givers.
- **Continuity:** S0450.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0452 — f19743-19757 (822.667-823.250 s, 15 frames, 0.62 s) — shot SH174 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0641.jpg; entry EP0641, exit EP0642; second review: OK
- **Objects/placement (OBSERVED):** Table with orange header/cell highlight added beside green ones; elderly bald man with cane and worried look at left (x .05-.2, y .3-1); wealthy woman at right.
- **Background:** white
- **Illustration:** Man beige skin, cane brown, sad brows.
- **Typography:** Same table text.
- **Readable text:** Table 1: Descriptive Statistics (Means), Households Aged 25-44
- **Unreadable/uncertain text:** numeric cells
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.779 #bfb6a6:0.070 #e2e2e1:0.066 #090907:0.042 #74886f:0.042
- **Hierarchy:** Left man, highlights, right woman for contrast.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0641; exits hard replace EP0642.
- **Narration (ASR, unverified):** who don't.
- **Story function (INFERRED):** INFERRED: contrast between parents who give money and those who do not.
- **Continuity:** S0451.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0453 — f19758-19850 (823.292-827.125 s, 93 frames, 3.88 s) — shot SH175 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0642.jpg; entry EP0642, exit EP0643; second review: OK
- **Objects/placement (OBSERVED):** Upper: paragraph of document text full width (x .02-.98, y .02-.77) fully black; presenter at lower right (x .65-.85, y .6-1) neutral face with long pointer stick toward the lower left.
- **Background:** white
- **Illustration:** Presenter with beige head and small mouth, long brown stick.
- **Typography:** Serif body ~1.8%, black.
- **Readable text:** We show that the premium cut had significant distributional effects.
- **Unreadable/uncertain text:** rest of paragraph
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.858 #e8d1be:0.072 #5a5857:0.029 #959494:0.024 #080605:0.017
- **Hierarchy:** Text block then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0642; additive EP0643.
- **Narration (ASR, unverified):** And in a market where the real constraint is supply, we already saw what easier
- **Story function (INFERRED):** INFERRED: quotes paper's finding about premium cut and prices.
- **Continuity:** Presenter pose reused S0454/S0455.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0454 — f19851-19858 (827.167-827.458 s, 8 frames, 0.33 s) — shot SH175 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0643.jpg; entry EP0643, exit EP0644; second review: OK
- **Objects/placement (OBSERVED):** Same paragraph with a green highlight over two lines near the bottom; a cream 'DEBT' document at lower left (x .04-.1, y .75-.95).
- **Background:** white
- **Illustration:** DEBT paper: cream fill, red hand-lettered caps.
- **Typography:** Serif body ~1.8%; 'DEBT' red marker.
- **Readable text:** DEBT; With limited supply, the boost to demand from the cut ended up raising home prices.
- **Unreadable/uncertain text:** other paragraph text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.816 #e2d2c1:0.101 #6f6a6a:0.043 #0c0e09:0.025 #34dd44:0.015
- **Hierarchy:** Green highlight pops then DEBT paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0643; exits additive EP0644; 8 frames.
- **Narration (ASR, unverified):** easier borrowing
- **Story function (INFERRED):** INFERRED: highlights the supply-limited price effect.
- **Continuity:** S0453.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0455 — f19859-19913 (827.500-829.750 s, 55 frames, 2.29 s) — shot SH175 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0644.jpg; entry EP0644, exit EP0645; second review: OK
- **Objects/placement (OBSERVED):** Same as S0454 with a second DEBT document beside the first at lower left.
- **Background:** white
- **Illustration:** As above.
- **Typography:** Same.
- **Readable text:** DEBT; With limited supply, the boost to demand from the cut ended up raising home prices.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.779 #e3d5c6:0.128 #716a6a:0.047 #0c0d09:0.031 #33dd44:0.015
- **Hierarchy:** Same.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0644; exits hard replace EP0645.
- **Narration (ASR, unverified):** easier borrowing does with the FHA cut.
- **Story function (INFERRED):** INFERRED: doubling debt as borrowing grows.
- **Continuity:** S0454.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0456 — f19914-19943 (829.792-831.000 s, 30 frames, 1.25 s) — shot SH176 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0645.jpg; entry EP0645, exit EP0647; second review: OK
- **Objects/placement (OBSERVED):** Top-left: green dollar sign (x .04-.12, y .05-.5). Bright lime zigzag line falling from top-left toward bottom-right (x .07-.18 -> .33). Lower right: brown-roofed house with chimney and bushes (x .62-.85, y .6-.95).
- **Background:** flat off-white canvas
- **Illustration:** Dollar sign dark green flat with outline; zigzag thick lime marker stroke with no outline; house detailed with red roof.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.899 #111008:0.029 #4f8045:0.027 #b38471:0.025 #71fa2b:0.020
- **Hierarchy:** Green stroke leads the eye diagonally to the house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0645; micro EP0646 extends the line; exits via swap EP0647.
- **Narration (ASR, unverified):** It doesn't lower the price.
- **Story function (INFERRED):** INFERRED: easier borrowing does not lower the price - drawn as a line pointing at the house.
- **Continuity:** S0457 follows with the price tag.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0195 (DRAW_ON_OR_REVEAL, f19937) The green zigzag line extends its tip down to the roof of the house at lower right.

## S0457 — f19978-20011 (832.458-833.833 s, 34 frames, 1.42 s) — shot SH176 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0647.jpg; entry EP0647, exit EP0648; second review: MINOR
- **Objects/placement (OBSERVED):** Large yellow price tag with three red dollar signs and string loop (x .17-.52, y .1-.75). Rest blank.
- **Background:** flat off-white canvas
- **Illustration:** Yellow flat tag, black outline, red hand-drawn dollar signs.
- **Typography:** Red hand-drawn '$$$' ~8% height.
- **Readable text:** $$$
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.936 #e2d933:0.040 #090706:0.013 #c53212:0.009 #7f7f62:0.002
- **Hierarchy:** Single tag centre-left.
- **Camera/motion:** STATIC 2D; **entry/exit:** Entered by swap EP0647; additive EP0648 next.
- **Narration (ASR, unverified):** And a higher price means a bigger
- **Story function (INFERRED):** INFERRED: higher price.
- **Continuity:** S0458-S0460 add money.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0458 — f20012-20015 (833.875-834.000 s, 4 frames, 0.17 s) — shot SH176 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0648.jpg; entry EP0648, exit EP0649; second review: MINOR
- **Objects/placement (OBSERVED):** Yellow price tag (x .17-.53, y .1-.75) and one green banknote at right (x .59-.85, y .45-.7).
- **Background:** flat off-white canvas
- **Illustration:** Green banknote with darker circle seal and yellow dollar, black outline.
- **Typography:** $$$ tag.
- **Readable text:** $$$
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.879 #77a46c:0.046 #e1d934:0.043 #080906:0.024 #c33313:0.009
- **Hierarchy:** Tag then bill.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0648; exits additive EP0649; 4 frames.
- **Narration (ASR, unverified):** bigger down
- **Story function (INFERRED):** INFERRED: tag plus one bill build-up animation frame.
- **Continuity:** S0457.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0459 — f20016-20021 (834.042-834.250 s, 6 frames, 0.25 s) — shot SH176 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0649.jpg; entry EP0649, exit EP0650; second review: MINOR
- **Objects/placement (OBSERVED):** Yellow price tag at left (x .17-.52, y .15-.85) and two stacked banknotes at right (x .55-.85, y .45-.9).
- **Background:** flat off-white canvas
- **Illustration:** As before.
- **Typography:** $$$
- **Readable text:** $$$
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.853 #77a46d:0.063 #e0d935:0.044 #080a06:0.030 #c33313:0.009
- **Hierarchy:** Tag then bills.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0649; exits EP0650; 6 frames.
- **Narration (ASR, unverified):** down payment
- **Story function (INFERRED):** INFERRED: second bill stacks.
- **Continuity:** S0458/S0460.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0460 — f20022-20033 (834.292-834.750 s, 12 frames, 0.50 s) — shot SH176 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0650.jpg; entry EP0650, exit EP0651; second review: MINOR
- **Objects/placement (OBSERVED):** Yellow price tag (x .17-.52, y .1-.8) and three overlapping banknotes to its right (x .55-.9, y .35-.85).
- **Background:** flat off-white canvas
- **Illustration:** As before.
- **Typography:** $$$
- **Readable text:** $$$
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.824 #77a56d:0.086 #e0d935:0.045 #070b06:0.036 #c33313:0.009
- **Hierarchy:** Money stack grows.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0650; exits hard replace EP0651; 12 frames.
- **Narration (ASR, unverified):** payment because
- **Story function (INFERRED):** INFERRED: price rises, bills pile up.
- **Continuity:** S0459.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0461 — f20034-20095 (834.792-837.333 s, 62 frames, 2.58 s) — shot SH177 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0651.jpg; entry EP0651, exit EP0654; second review: MINOR
- **Objects/placement (OBSERVED):** Smiling spiky-haired stick presenter centre (x .39-.61, y .08-1); two stacked banknotes upper left (x .09-.32, y .02-.3). Later a red handwritten '% of price' appears to the right of his head (x .55-.85, y .1-.25).
- **Background:** flat off-white canvas
- **Illustration:** Presenter beige head with black spiky hair, simple smile, thin limbs; arms in small pose change (EP0652).
- **Typography:** Red hand-lettered '% of price' ~4% height (added in-state).
- **Readable text:** % of price
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.868 #f4d3b5:0.058 #7da86e:0.041 #050603:0.029 #4a4f43:0.005
- **Hierarchy:** Presenter face, then red text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0651; micro EP0652 pose; EP0653 text; exits hard replace EP0654.
- **Narration (ASR, unverified):** because the down payment is a percentage of the price.
- **Story function (INFERRED):** INFERRED: down payment is a percentage of price.
- **Continuity:** Presenter model reused S0462.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0196 (POSE_SWAP, f20064) The presenter's arms at lower torso change position slightly (small V-shaped arm lines at bottom centre).; EVI0197 (TEXT_CHANGE, f20071) Red handwritten '% of price' appears right of the presenter's head.

## S0462 — f20096-20129 (837.375-838.750 s, 34 frames, 1.42 s) — shot SH178 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0654.jpg; entry EP0654, exit EP0655; second review: MINOR
- **Objects/placement (OBSERVED):** Skeptical spiky-haired presenter, hand at chin, eyebrow raised, left-centre (x .19-.34, y .05-.9).
- **Background:** flat off-white canvas
- **Illustration:** Beige head, slanted brows, flat mouth; thin limbs.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.962 #f3d2b7:0.025 #080403:0.009 #48413c:0.002 #98918d:0.002
- **Hierarchy:** Single figure left; empty right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0654; additive EP0655.
- **Narration (ASR, unverified):** So a policy meant to get first
- **Story function (INFERRED):** INFERRED: reaction beat 'so a policy meant to get first-time buyers...'
- **Continuity:** Same model S0461/S0463.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0463 — f20130-20154 (838.792-839.792 s, 25 frames, 1.04 s) — shot SH178 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0655.jpg; entry EP0655, exit EP0656; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter left (x .19-.34); family of two adults holding hands with baby and teddy bear at right (x .63-.88, y .25-.72).
- **Background:** flat off-white canvas
- **Illustration:** Adults brown and curly-haired, baby with pacifier; thin stick bodies.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.920 #ebcfb9:0.034 #0b0706:0.024 #aa8f84:0.012 #594f49:0.010
- **Hierarchy:** Presenter then family.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0655; additive EP0656.
- **Narration (ASR, unverified):** first -time buyers through
- **Story function (INFERRED):** INFERRED: first-time buyers/families.
- **Continuity:** S0464.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0464 — f20155-20174 (839.833-840.625 s, 20 frames, 0.83 s) — shot SH178 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0656.jpg; entry EP0656, exit EP0657; second review: MINOR
- **Objects/placement (OBSERVED):** Presenter left (x .19-.34); small cream house with red roof at centre (x .45-.62, y .2-.5); family with baby at right (x .64-.88, y .25-.72).
- **Background:** flat off-white canvas
- **Illustration:** House cream with red roof, two blue windows, orange door.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.885 #e6d2bb:0.050 #0b0706:0.036 #a58f83:0.014 #67463f:0.014
- **Hierarchy:** House bridges presenter and family.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0656; exits hard replace EP0657.
- **Narration (ASR, unverified):** through the door makes the
- **Story function (INFERRED):** INFERRED: getting families through the door.
- **Continuity:** S0463.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0465 — f20175-20193 (840.667-841.417 s, 19 frames, 0.79 s) — shot SH179 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0657.jpg; entry EP0657, exit EP0658; second review: OK
- **Objects/placement (OBSERVED):** Large close-up of a pensive brown-skinned character with black hair, bow tie and hand at chin, at left (x .06-.4, y .1-1). Right empty.
- **Background:** flat off-white canvas
- **Illustration:** Thick outlines, brown fill, brown bow tie, flat face, curved body stroke.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.899 #211c18:0.036 #030202:0.033 #b0937f:0.027 #6a5248:0.005
- **Hierarchy:** Large face on left; empty right.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0657; additive EP0658.
- **Narration (ASR, unverified):** the one part they can't
- **Story function (INFERRED):** INFERRED: reflection on the one part they can't borrow.
- **Continuity:** Character from S0466-S0469.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0466 — f20194-20212 (841.458-842.208 s, 19 frames, 0.79 s) — shot SH179 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0658.jpg; entry EP0658, exit EP0660; second review: MINOR
- **Objects/placement (OBSERVED):** Pensive bow-tie character at left (x .15-.39); red 'Down payment' label upper right (x .56-.83, y .05-.15); one green banknote below (x .59-.79, y .5-.65).
- **Background:** flat off-white canvas
- **Illustration:** Red marker; green bill.
- **Typography:** Red hand-lettered ~4% height.
- **Readable text:** Down payment
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.861 #2b1e1c:0.040 #030302:0.039 #b5937b:0.032 #769c6a:0.028
- **Hierarchy:** Character then red label.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0658; micro EP0659 eyes; motion EP0660.
- **Narration (ASR, unverified):** they can't borrow even
- **Story function (INFERRED):** INFERRED: the part they cannot borrow.
- **Continuity:** S0467-S0469.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0198 (EXPRESSION_CHANGE, f20208) The character's eyes change to wide round eyes with glasses-like rims.

## S0467 — f20217-20219 (842.417-842.500 s, 3 frames, 0.12 s) — shot SH179 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0660.jpg; entry EP0660, exit EP0661; second review: OK
- **Objects/placement (OBSERVED):** Character now with wide round eyes; right: 'Down payment' and two stacked banknotes.
- **Background:** flat off-white canvas
- **Illustration:** Eyes wide with rims.
- **Typography:** Red hand-lettered.
- **Readable text:** Down payment
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.848 #100f0c:0.081 #78a56e:0.039 #b79b7f:0.023 #753f3e:0.010
- **Hierarchy:** Same.
- **Camera/motion:** STATIC 2D; **entry/exit:** Motion exit EP0660; 3-frame state.
- **Narration (ASR, unverified):** even
- **Story function (INFERRED):** INFERRED: frame in the banknote stack animation (second bill).
- **Continuity:** S0466.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0468 — f20220-20225 (842.542-842.750 s, 6 frames, 0.25 s) — shot SH179 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0661.jpg; entry EP0661, exit EP0662; second review: OK
- **Objects/placement (OBSERVED):** Same character; three-layer stack of banknotes at right under the 'Down payment' label.
- **Background:** flat off-white canvas
- **Illustration:** As above.
- **Typography:** Red hand-lettered.
- **Readable text:** Down payment
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.835 #100f0b:0.083 #78a66e:0.048 #b89c7e:0.023 #73403f:0.011
- **Hierarchy:** Same.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0661; exits EP0662; 6 frames.
- **Narration (ASR, unverified):** even bigger,
- **Story function (INFERRED):** INFERRED: growing down payment.
- **Continuity:** S0467.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0469 — f20226-20234 (842.792-843.125 s, 9 frames, 0.38 s) — shot SH179 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0662.jpg; entry EP0662, exit EP0663; second review: OK
- **Objects/placement (OBSERVED):** Same; stack at right slightly larger with an extra bill layer.
- **Background:** flat off-white canvas
- **Illustration:** As above.
- **Typography:** Red hand-lettered.
- **Readable text:** Down payment
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.826 #0f0f0b:0.087 #78a66f:0.053 #b79c7e:0.023 #70423f:0.012
- **Hierarchy:** Same.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0662; exits hard replace EP0663.
- **Narration (ASR, unverified):** bigger, and
- **Story function (INFERRED):** INFERRED: 'even bigger' emphasis.
- **Continuity:** S0468.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0470 — f20235-20279 (843.167-845.000 s, 45 frames, 1.88 s) — shot SH180 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0663.jpg; entry EP0663, exit EP0664; second review: MINOR
- **Objects/placement (OBSERVED):** News article card (x .08-.92, y 0-.67) with houses photo at top right (x .52-.91, y 0-.12), date/byline top left, green highlight on first words of body (x .08-.6, y .28-.4), social icons and author bio at right; white margins below.
- **Background:** grey-white article on white
- **Illustration:** Raw screenshot.
- **Typography:** Serif body ~1.5%, black; green marker highlight.
- **Readable text:** September 6, 2023, 5:07pm by Chris Clow; Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift from family members or inheritance
- **Unreadable/uncertain text:** author bio, remaining text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.698 #dfdfdb:0.185 #a6ada9:0.045 #697376:0.044 #253844:0.028
- **Hierarchy:** Highlighted opening phrase then photo strip.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0663; additive EP0664.
- **Narration (ASR, unverified):** and the buyers most likely to cover it are
- **Story function (INFERRED):** INFERRED: source for the 38 percent claim.
- **Continuity:** Same article S0471-S0472 and earlier shot before S0438.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0471 — f20280-20300 (845.042-845.875 s, 21 frames, 0.88 s) — shot SH180 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0664.jpg; entry EP0664, exit EP0665; second review: MINOR
- **Objects/placement (OBSERVED):** Article card (x .08-.92, y 0-.6) with green highlight on body; grey hoodie sunglasses figure holding cash at bottom (x .45-.69, y .5-1).
- **Background:** grey-white article
- **Illustration:** Figure grey flat, sunglasses, banknote in hand.
- **Typography:** As S0470.
- **Readable text:** Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.635 #dfdfda:0.186 #a9b19c:0.081 #65736f:0.056 #172226:0.042
- **Hierarchy:** Figure bottom, highlight.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0664; additive EP0665.
- **Narration (ASR, unverified):** it are the ones with a parent
- **Story function (INFERRED):** INFERRED: represents the gift-receiving buyer.
- **Continuity:** S0472.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0472 — f20301-20338 (845.917-847.458 s, 38 frames, 1.58 s) — shot SH180 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0665.jpg; entry EP0665, exit EP0666; second review: MINOR
- **Objects/placement (OBSERVED):** Article card with green highlight; hoodie figure (x .45-.69, y .5-1) and grey-haired old woman with cane at right (x .73-.9, y .6-1).
- **Background:** grey-white article
- **Illustration:** Woman grey hair, cane, worried face.
- **Typography:** As S0470.
- **Readable text:** Approximately 38% of first-time homebuyers under the age of 30 relied on either a cash gift
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fafaf9:0.600 #dfdfda:0.189 #738079:0.083 #b9c99e:0.070 #172021:0.057
- **Hierarchy:** Figures at base.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0665; hard replace EP0666.
- **Narration (ASR, unverified):** a parent who can write the check. And
- **Story function (INFERRED):** INFERRED: grandparent giving.
- **Continuity:** S0471.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0473 — f20339-20384 (847.500-849.375 s, 46 frames, 1.92 s) — shot SH181 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0666.jpg; entry EP0666, exit EP0668; second review: OK
- **Objects/placement (OBSERVED):** Large headband character left (x .18-.29 of tile; spiky brown hair, red headband, content smile, hands on hip), blank background.
- **Background:** flat off-white canvas
- **Illustration:** Thick black outlines, brown/tan face, red headband.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.909 #090505:0.035 #9d8366:0.026 #d7bea3:0.021 #903e38:0.008
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0666; micro EP0667 thumbs-up; additive EP0668.
- **Narration (ASR, unverified):** And for the buyers who get into the market,
- **Story function (INFERRED):** INFERRED: introduces an 'I made it' persona.
- **Continuity:** S0474.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0199 (POSE_SWAP, f20366) The character's right arm changes to a raised thumbs-up at centre.

## S0474 — f20385-20424 (849.417-851.042 s, 40 frames, 1.67 s) — shot SH181 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0668.jpg; entry EP0668, exit EP0670; second review: MINOR
- **Objects/placement (OBSERVED):** Headband character with thumbs-up at left (x .12-.48, y .1-1); speech bubble 'Finally, I've done it!' at right (x .42-.81, y .05-.55), with tiny '(it was torture)' (styled with symbols) under the text in later frames.
- **Background:** flat off-white canvas
- **Illustration:** Bubble white with black outline; hand lettering.
- **Typography:** Hand lettering ~5% height, black.
- **Readable text:** Finally, I've done it!
- **Unreadable/uncertain text:** (it was torture)
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.879 #070505:0.057 #9b8369:0.029 #d4bea7:0.024 #7d423c:0.012
- **Hierarchy:** Bubble text then character.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0668; micro EP0669; exits EP0670.
- **Narration (ASR, unverified):** without the help of rich parents,
- **Story function (INFERRED):** INFERRED: a buyer celebrating despite hardship.
- **Continuity:** S0473.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0200 (TEXT_CHANGE, f20412) A tiny parenthetical caption appears under the bubble's text line.

## S0475 — f20428-20474 (851.208-853.125 s, 47 frames, 1.96 s) — shot SH181 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0670.jpg; entry EP0670, exit EP0673; second review: MINOR
- **Objects/placement (OBSERVED):** Single gold coin at centre-right (x .67-.78, y .45-.55) on blank canvas.
- **Background:** flat off-white canvas
- **Illustration:** Gold coin with black outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.992 #090703:0.004 #ccc96c:0.003 #595938:0.001 #95957f:0.000
- **Hierarchy:** Single coin.
- **Camera/motion:** STATIC 2D; **entry/exit:** Character exit EP0670; coin stack grows by EP0671-0672.
- **Narration (ASR, unverified):** they typically lean on low -down payment,
- **Story function (INFERRED):** INFERRED: money left after the buyer, building to coin stack.
- **Continuity:** S0476.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0201 (ADDITIVE_ENTRY, f20439) The single coin becomes a stack of two coins.; EVI0202 (ADDITIVE_ENTRY, f20450) A third coin is added to the stack.

## S0476 — f20475-20509 (853.167-854.583 s, 35 frames, 1.46 s) — shot SH181 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0673.jpg; entry EP0673, exit EP0674; second review: OK
- **Objects/placement (OBSERVED):** Green country-map character with eyes and smile holding a pink LOAN paper (x .24-.47, y .18-.78); stack of three gold coins at right (x .69-.8, y .33-.5).
- **Background:** flat off-white canvas
- **Illustration:** Green flat map with black outline, googly eyes, small legs.
- **Typography:** LOAN in red handwriting on paper.
- **Readable text:** LOAN
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.878 #4a9d50:0.077 #0d1509:0.024 #e1cbc9:0.012 #baad72:0.009
- **Hierarchy:** Map first by size/colour, then coins.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0673; hard replace EP0674.
- **Narration (ASR, unverified):** government -backed loans,
- **Story function (INFERRED):** INFERRED: government-backed loans.
- **Continuity:** S0499 uses the map again.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0477 — f20510-20533 (854.625-855.583 s, 24 frames, 1.00 s) — shot SH182 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0674.jpg; entry EP0674, exit EP0677; second review: MINOR
- **Objects/placement (OBSERVED):** Left: blue Investopedia-style card with house-in-hand art, 'FHA Loan', pronunciation and definition (x .06-.5, y .02-.55). Centre: cream 'MORTGAGE' papers (x .59-.72, y .1-.55). Right: one green banknote (x .79-.9, y .3-.4).
- **Background:** blue card, white canvas
- **Illustration:** Card flat blue with dark-blue illustration; paper cream with red title.
- **Typography:** Sans heading ~3%, body ~1.5%; red hand lettering on paper.
- **Readable text:** FHA Loan ['ef ach 'a lan']; MORTGAGE
- **Unreadable/uncertain text:** definition body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfb:0.753 #8fb8f6:0.192 #768d8a:0.022 #0c1218:0.017 #394966:0.016
- **Hierarchy:** Blue card dominates, then props.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0674; micro EP0675-0676 bills; additive EP0677.
- **Narration (ASR, unverified):** like an FHA or
- **Story function (INFERRED):** INFERRED: shows what FHA is.
- **Continuity:** S0478.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0203 (ADDITIVE_ENTRY, f20519) A second banknote appears under the first at right.; EVI0204 (ADDITIVE_ENTRY, f20526) A third banknote is added to the stack at right.

## S0478 — f20534-20554 (855.625-856.458 s, 21 frames, 0.88 s) — shot SH182 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0677.jpg; entry EP0677, exit EP0678; second review: MINOR
- **Objects/placement (OBSERVED):** FHA Loan card at left (x .06-.43), MORTGAGE papers centre, stack of three banknotes right; white 'About Home Loans' excerpt box lower right (x .44-.96, y .5-.95).
- **Background:** blue card, white canvas
- **Illustration:** Same.
- **Typography:** Excerpt serif ~1.2%.
- **Readable text:** FHA Loan; MORTGAGE; About Home Loans
- **Unreadable/uncertain text:** excerpt body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.689 #8eb7f6:0.187 #6e807c:0.051 #d6d5cb:0.042 #1b242d:0.031
- **Hierarchy:** Blue card then excerpt.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0677; hard replace EP0678.
- **Narration (ASR, unverified):** or VA. And
- **Story function (INFERRED):** INFERRED: second program (VA) mentioned.
- **Continuity:** S0477.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0479 — f20555-20625 (856.500-859.417 s, 71 frames, 2.96 s) — shot SH183 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0678.jpg; entry EP0678, exit EP0680; second review: OK
- **Objects/placement (OBSERVED):** Left: frowning presenter with pointer stick (x .02-.2, y .1-.95); right: news-site capture (x .27-.99, y .1-.65) with black header bar, bold headline 'Mortgage delinquencies eased in Q2, still higher than 2025' and teal photo of a house with papers; subtext with purple highlight added.
- **Background:** white
- **Illustration:** Presenter beige, frowning, thin brown stick.
- **Typography:** Headline bold sans ~3%; body ~1.2%.
- **Readable text:** HOUSINGWIRE; Mortgage delinquencies eased in Q2, still higher than 2025
- **Unreadable/uncertain text:** body text, MBA foreclosure line
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.626 #e2dcd6:0.206 #307479:0.079 #1c1c1d:0.057 #8e9494:0.033
- **Hierarchy:** Headline then teal photo.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0678; micro EP0679 purple highlight; additive EP0680.
- **Narration (ASR, unverified):** And right now, more than one in ten FHA loans are
- **Story function (INFERRED):** INFERRED: FHA delinquency data source.
- **Continuity:** S0480.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0205 (HIGHLIGHT_ADD, f20565) Purple text highlight begins on 'FHA' within the sentence about delinquencies in a housing-news article capture (x~0.4-0.62,y~0.5-0.62); EVI0206 (HIGHLIGHT_ADD, f20567) A purple highlight band appears across two text lines under the headline of the news screenshot.; EVI0207 (HIGHLIGHT_ADD, f20569) Purple text highlight extends across 'FHA delinquencies stayed elevated at 11.79%'; a small red marker appears at the line end; EVI0208 (HIGHLIGHT_ADD, f20577) Purple highlight extends by one more word at the end of the line (x~0.49-0.59,y~0.53-0.60); EVI0209 (OBJECT_MOTION, f20612) Mouse text-cursor and small selection change appear over the house photo and article text on the right (x~0.69-0.92,y~0.44-0.55)

## S0480 — f20626-20663 (859.458-861.000 s, 38 frames, 1.58 s) — shot SH183 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0680.jpg; entry EP0680, exit EP0681; second review: MINOR
- **Objects/placement (OBSERVED):** Frowning presenter with pointer at left (x .0-.25); HousingWire article capture at upper right with purple highlight on 'FHA delinquencies stayed elevated at 11.79%' (x .39-.95, y .05-.65); worried-eyed banknote below it (x .59-.75, y .72-.9).
- **Background:** white
- **Illustration:** Banknote with googly worried eyes.
- **Typography:** As above.
- **Readable text:** HOUSINGWIRE; Mortgage delinquencies eased in Q2, still higher than 2025
- **Unreadable/uncertain text:** body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.606 #e2dcd6:0.202 #327478:0.082 #191a1b:0.063 #919a99:0.047
- **Hierarchy:** Headline then bill.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0680; hard replace EP0681.
- **Narration (ASR, unverified):** are behind on payments.
- **Story function (INFERRED):** INFERRED: loans in trouble.
- **Continuity:** S0479.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0481 — f20664-20731 (861.042-863.833 s, 68 frames, 2.83 s) — shot SH184 (inferred) — F11 other composite
- **Evidence:** frames/ep_stable/e0681.jpg; entry EP0681, exit EP0682; second review: MINOR
- **Objects/placement (OBSERVED):** Article excerpt block with three paragraphs on delinquency rates (x .16-.82, y .2-.7); small pink house (x .64-.74, y .72-.95) and tall grey apartment building (x .78-.93, y .65-.95) at lower right.
- **Background:** white
- **Illustration:** Buildings flat with black outlines.
- **Typography:** Serif ~1.3%.
- **Readable text:** The 30-day delinquency rate fell 3 bps to 2.21%...
- **Unreadable/uncertain text:** paragraph text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfafa:0.884 #d8d7d4:0.037 #63605c:0.033 #aca29f:0.032 #100e0c:0.014
- **Hierarchy:** Text block then buildings.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0681; additive EP0682.
- **Narration (ASR, unverified):** For conventional loans, the kind the government doesn't back,
- **Story function (INFERRED):** INFERRED: contrast conventional versus government-backed delinquency.
- **Continuity:** S0482.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0482 — f20732-20774 (863.875-865.625 s, 43 frames, 1.79 s) — shot SH184 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0682.jpg; entry EP0682, exit EP0683; second review: OK
- **Objects/placement (OBSERVED):** Same article excerpt with red highlight over 'The conventional delinquency rate fell 3 basis points to 2.72%'; puzzled stick presenter at lower left-centre (x .22-.34, y .5-1) overlapping text; two buildings bottom right.
- **Background:** white
- **Illustration:** Presenter small, raised brow, flat mouth.
- **Typography:** Serif ~1.3%; red highlight.
- **Readable text:** The 30-day delinquency rate fell 3 bps to 2.21%; The conventional delinquency rate fell 3 basis points to 2.72%
- **Unreadable/uncertain text:** other paragraphs
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfafa:0.853 #e4d3c5:0.054 #b79b9b:0.037 #665c59:0.034 #0f0c0a:0.022
- **Hierarchy:** Highlight then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0682; hard replace EP0683.
- **Narration (ASR, unverified):** it's fewer than three in a hundred.
- **Story function (INFERRED):** INFERRED: conventional loans have lower delinquency.
- **Continuity:** S0481.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0483 — f20775-20783 (865.667-866.000 s, 9 frames, 0.38 s) — shot SH185 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0683.jpg; entry EP0683, exit EP0684; second review: OK
- **Objects/placement (OBSERVED):** Press-release capture: header band with abstract graphic, small nav text, headline 'ICE Mortgage Monitor: Mortgage Holder Equity Climbs to Record $18 Trillion as Annual Home Price Growth Reaches 14-Month High' at lower left, small body text below.
- **Background:** white
- **Illustration:** Raw screenshot.
- **Typography:** Sans headline ~2.3% bold, body ~1%.
- **Readable text:** Mortgage Monitor: Mortgage Holder Equity Climbs to Record $18 Trillion as Annual Home Price Growth Reaches 14-Month High
- **Unreadable/uncertain text:** body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.897 #e1e3e6:0.055 #b0b1b3:0.022 #7f7e7f:0.020 #1f1f1f:0.005
- **Hierarchy:** Headline then banner.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0683; scroll motion EP0684.
- **Narration (ASR, unverified):** About 813
- **Story function (INFERRED):** INFERRED: entry frame to the equity report.
- **Continuity:** S0484.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0484 — f20832-20874 (868.042-869.792 s, 43 frames, 1.79 s) — shot SH185 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0684.jpg; entry EP0684, exit EP0685; second review: OK
- **Objects/placement (OBSERVED):** Zoomed bullet-list text full-bleed with bullets 'Equity hits record high; negative equity elevated among recent-vintage borrowers', paragraphs about average tappable equity and a sentence including 'approximately 813,000 borrowers are underwater'.
- **Background:** white
- **Illustration:** Raw screenshot.
- **Typography:** Sans body ~1.4%, black.
- **Readable text:** Equity hits record high; negative equity elevated among recent-vintage borrowers; Real estate owned (REO) properties are selling at historically wide discounts
- **Unreadable/uncertain text:** paragraph numbers
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.869 #e0e0e0:0.040 #888888:0.033 #b8b8b8:0.033 #5e5e5e:0.025
- **Hierarchy:** Text mass.
- **Camera/motion:** SCROLL; **entry/exit:** Scroll-in EP0684; additive EP0685.
- **Narration (ASR, unverified):** now have negative equity in their home,
- **Story function (INFERRED):** INFERRED: moving to the negative-equity paragraph.
- **Continuity:** S0485-S0487.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0485 — f20875-20878 (869.833-869.958 s, 4 frames, 0.17 s) — shot SH185 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0685.jpg; entry EP0685, exit EP0686; second review: MINOR
- **Objects/placement (OBSERVED):** Report text with cyan highlight on 'approximately 813,000 borrowers are underwater'; one cream DEBT document at lower centre (x .43-.56, y .6-.95).
- **Background:** white
- **Illustration:** DEBT paper cream with red caps.
- **Typography:** As S0484.
- **Readable text:** approximately 813,000 borrowers are underwater; DEBT
- **Unreadable/uncertain text:** rest
- **Palette (MEASURED, top-5 k-means of representative frame):** #fbfbfb:0.865 #cecdcc:0.059 #868686:0.048 #434746:0.020 #49e9df:0.008
- **Hierarchy:** Cyan highlight then DEBT paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0685; motion EP0686; 4 frames.
- **Narration (ASR, unverified):** meaning
- **Story function (INFERRED):** INFERRED: first debt sheet in pile.
- **Continuity:** S0484.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0486 — f20891-20902 (870.500-870.958 s, 12 frames, 0.50 s) — shot SH185 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0686.jpg; entry EP0686, exit EP0687; second review: OK
- **Objects/placement (OBSERVED):** Text with cyan highlight; pile of ~6 DEBT papers overlapping at lower centre (x .38-.78, y .38-.95).
- **Background:** white
- **Illustration:** Papers cream with red 'DEBT' caps and squiggles.
- **Typography:** As S0484.
- **Readable text:** approximately 813,000 borrowers are underwater; DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.732 #e6e1db:0.144 #6e6868:0.051 #9db4b2:0.048 #0f0d0a:0.025
- **Hierarchy:** Pile hides text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Motion EP0686; additive EP0687.
- **Narration (ASR, unverified):** more than their
- **Story function (INFERRED):** INFERRED: mounting debt.
- **Continuity:** S0487.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0487 — f20903-20976 (871.000-874.042 s, 74 frames, 3.08 s) — shot SH185 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0687.jpg; entry EP0687, exit EP0688; second review: OK
- **Objects/placement (OBSERVED):** As S0486 plus a dark brown rundown house at right of the pile (x .62-.78, y .62-.9).
- **Background:** white
- **Illustration:** House dark brown with red roof.
- **Typography:** As S0484.
- **Readable text:** approximately 813,000 borrowers are underwater; up 44% year-over-year; DEBT
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.705 #e5e1db:0.144 #736c67:0.066 #9db4b0:0.048 #100c0a:0.036
- **Hierarchy:** Pile then house.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0687; hard replace EP0688.
- **Narration (ASR, unverified):** their house is worth. That's 44 % in a year.
- **Story function (INFERRED):** INFERRED: houses worth less than owed.
- **Continuity:** S0486.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0488 — f20985-20990 (874.417-874.625 s, 6 frames, 0.25 s) — shot SH186 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0688.jpg; entry EP0688, exit EP0689; second review: MINOR
- **Objects/placement (OBSERVED):** News page capture 'Real Estate News' header with subscribe button, headline text at left, hands-and-phone photo (x .33-.54, y .05-.35), body text below; frowning presenter with pointer at right (x .6-.83, y .1-1).
- **Background:** white
- **Illustration:** Presenter beige, frown, brown stick.
- **Typography:** Sans bold headline ~2%, body ~1%.
- **Readable text:** Real Estate News; Mortgage holder equity reached $18 trillion in June, but a growing share of borrowers in Texas and Florida are either underwater, behind on payments, or both
- **Unreadable/uncertain text:** body text
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.825 #e1cec0:0.080 #949091:0.045 #100b0b:0.027 #513b38:0.024
- **Hierarchy:** Headline/photo then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0688; scroll EP0689; 6 frames.
- **Narration (ASR, unverified):** 75 %
- **Story function (INFERRED):** INFERRED: second source for underwater claim.
- **Continuity:** S0489-S0491.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0489 — f21018-21130 (875.792-880.458 s, 113 frames, 4.71 s) — shot SH186 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0689.jpg; entry EP0689, exit EP0691; second review: MINOR
- **Objects/placement (OBSERVED):** Article text 'Who is underwater?' at top (x .12-.87, y .02-.3), yellow highlight on the 75% FHA or VA loan sentence appears in later frames; frowning presenter with pointer lower right (x .69-.87, y .25-1); '2022 - 2025' handwritten lower left in later frames.
- **Background:** white
- **Illustration:** Presenter frown, brown stick.
- **Typography:** Sans body ~1.7%; big marker ~5%.
- **Readable text:** Who is underwater? Most of the homeowners in a negative equity situation purchased their properties in the past few years; The report also found that 75% of those currently underwater used an FHA or VA loan; 2022 - 2025
- **Unreadable/uncertain text:** rest
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.875 #e9d3c0:0.062 #a7a9a9:0.025 #706f6e:0.024 #0f0c0b:0.015
- **Hierarchy:** Yellow highlight then date text.
- **Camera/motion:** STATIC 2D; **entry/exit:** Scroll EP0689; micro EP0690; hard replace EP0691.
- **Narration (ASR, unverified):** an FHA or VA loan, and most bought between 2022 and 2025.
- **Story function (INFERRED):** INFERRED: dates of purchase.
- **Continuity:** S0488.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0210 (TEXT_CHANGE, f21082) Large black text '2022 - 2025' appears at lower left over the article.

## S0490 — f21131-21217 (880.500-884.083 s, 87 frames, 3.62 s) — shot SH187 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0691.jpg; entry EP0691, exit EP0696; second review: OK
- **Objects/placement (OBSERVED):** Single large pink LOAN paper centred (x .48-.58, y .12-.8) with red hand-lettered 'LOAN' and squiggles.
- **Background:** flat off-white canvas
- **Illustration:** Pink flat paper, black outline, red lettering.
- **Typography:** Red hand lettering ~7%.
- **Readable text:** LOAN
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.928 #e6cbca:0.051 #090404:0.012 #c6302e:0.005 #6f6665:0.003
- **Hierarchy:** Single paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0691; micro EP0692-0695 add labels.
- **Narration (ASR, unverified):** These are the people who use the loans with the smallest down payments, bought at
- **Story function (INFERRED):** INFERRED: loan with small down payment.
- **Continuity:** S0491.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0211 (TEXT_CHANGE, f21172) Small handwritten 'Down payment' label appears at lower left of the LOAN paper.; EVI0212 (ADDITIVE_ENTRY, f21185) A tiny gold coin appears under the 'Down payment' label.; EVI0213 (ADDITIVE_ENTRY, f21196) The coin becomes a two-coin stack below the label.; EVI0214 (TEXT_CHANGE, f21209) Handwritten label 'Price' appears at right of the LOAN paper.

## S0491 — f21218-21250 (884.125-885.458 s, 33 frames, 1.38 s) — shot SH187 (inferred) — F3 object/icon cluster
- **Evidence:** frames/ep_stable/e0696.jpg; entry EP0696, exit EP0698; second review: MINOR
- **Objects/placement (OBSERVED):** Pink LOAN paper centre (x .41-.6, y .1-.8). Left: 'Down payment' label (x .11-.32, y .5-.58) with two coins below (x .15-.2, y .6-.65). Right: 'Price' label (x .77-.84) with red-roofed house and yellow tag below (x .7-.91, y .8-.95).
- **Background:** flat off-white canvas
- **Illustration:** Handwritten black labels ~3%; house multi-colour.
- **Typography:** Black hand lettering.
- **Readable text:** LOAN; Down payment; Price
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.892 #e2cac7:0.060 #130c09:0.024 #787363:0.016 #bb3736:0.008
- **Hierarchy:** Loan then labels.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0696; micro EP0697; hard replace EP0698.
- **Narration (ASR, unverified):** at near -record prices,
- **Story function (INFERRED):** INFERRED: balance between down payment and price.
- **Continuity:** S0490.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0215 (ADDITIVE_ENTRY, f21225) A small yellow price tag appears on the house's upper left.

## S0492 — f21251-21301 (885.500-887.583 s, 51 frames, 2.12 s) — shot SH188 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0698.jpg; entry EP0698, exit EP0700; second review: MINOR
- **Objects/placement (OBSERVED):** Worried blonde character centre-right (x .59-.87, y .08-1); tiny caption 'I can never win omg pls stop' at left of head appears in later frames.
- **Background:** flat off-white canvas
- **Illustration:** Wavy blonde hair, sad brows, simple body.
- **Typography:** Tiny handwritten caption at left of head (x .06).
- **Readable text:** none
- **Unreadable/uncertain text:** I can never ... caption
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.892 #d1bc84:0.049 #060403:0.037 #d4baaa:0.018 #676158:0.005
- **Hierarchy:** Face centre.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0698; micro EP0699; hard replace EP0700.
- **Narration (ASR, unverified):** and now they're the ones falling behind.
- **Story function (INFERRED):** INFERRED: the buyer without parental help.
- **Continuity:** S0498-.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0216 (TEXT_CHANGE, f21278) A tiny handwritten caption appears at left of the character's head.

## S0493 — f21302-21341 (887.625-889.250 s, 40 frames, 1.67 s) — shot SH189 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0700.jpg; entry EP0700, exit EP0701; second review: MINOR
- **Objects/placement (OBSERVED):** Elderly man with cane smiling at left (x .17-.38, y .05-1); speech bubble 'Sign this? Yes of cour-' (x .44-.62, y .05-.2); contract with blue quill at right (x .57-.77, y .35-.75).
- **Background:** flat off-white canvas
- **Illustration:** Beige, grey tufts, sweet smile; paper cream with ink marks; blue quill.
- **Typography:** Hand lettering in bubble ~2.5%.
- **Readable text:** Sign this? Yes of cour-
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.838 #ded9cf:0.055 #070606:0.052 #c6bea8:0.043 #5a5552:0.012
- **Hierarchy:** Bubble then man.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0700; additive micro frames EP0701.
- **Narration (ASR, unverified):** These are the borrowers who didn't have a parent
- **Story function (INFERRED):** INFERRED: parent signing for child.
- **Continuity:** S0494.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0494 — f21342-21380 (889.292-890.875 s, 39 frames, 1.62 s) — shot SH189 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0701.jpg; entry EP0701, exit EP0702; second review: OK
- **Objects/placement (OBSERVED):** As S0493 but man's head tilted down with eyes closed, no bubble.
- **Background:** flat off-white canvas
- **Illustration:** Slumped head.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.848 #ded9cf:0.054 #060505:0.045 #c7bea8:0.042 #58524e:0.010
- **Hierarchy:** Man then paper.
- **Camera/motion:** STATIC 2D; **entry/exit:** EP0701 change; hard replace EP0702.
- **Narration (ASR, unverified):** a parent to help write the check.
- **Story function (INFERRED):** INFERRED: elderly parent signs and passes out / bank of mom and dad runs dry.
- **Continuity:** S0493.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0495 — f21381-21583 (890.917-899.333 s, 203 frames, 8.46 s) — shot SH190 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0702.jpg; entry EP0702, exit EP0704; second review: MINOR
- **Objects/placement (OBSERVED):** Table 6 upper left (x .02-.45, y .03-.5); section 5.1 heading and paragraph below (x .3-1, y .6-1) gaining yellow highlight later; presenter head and tilted pointer stick upper right (x .65-.9, y .05-.55).
- **Background:** white
- **Illustration:** Presenter in neutral face; stick pointer diagonal.
- **Typography:** Serif ~1.5%.
- **Readable text:** Table 6: Homeownership Decreases while Wealth Increases Without Altruism; 5.1 The Effect of Parental Transfers on Homeownership
- **Unreadable/uncertain text:** paragraph body
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.851 #e4d3c4:0.075 #a7a7a6:0.036 #6d6b6a:0.023 #0b0807:0.014
- **Hierarchy:** Table then yellow paragraph.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0702; micro EP0703; additive EP0704.
- **Narration (ASR, unverified):** When you take away parental help, the Fed's paper found that young homeownership drops 13 percentage points. For comparison, the 2008 financial crisis, the
- **Story function (INFERRED):** INFERRED: shows the 13 point drop.
- **Continuity:** S0496-S0497.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0217 (POSE_SWAP, f21514) The presenter's pointer arm shifts position at right edge.

## S0496 — f21584-21587 (899.375-899.500 s, 4 frames, 0.17 s) — shot SH190 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0704.jpg; entry EP0704, exit EP0705; second review: OK
- **Objects/placement (OBSERVED):** As S0495 but a handwritten 'The world in 2008:' and a fiery chaos GIF image over the table (x .12-.3, y .06-.5).
- **Background:** white
- **Illustration:** GIF red/yellow with burning scenes.
- **Typography:** Handwritten black.
- **Readable text:** The world in 2008:
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.674 #dfb12e:0.107 #86674d:0.081 #e1ceb7:0.078 #331f17:0.060
- **Hierarchy:** GIF dominates.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0704; GIF motion EP0705; 4 frames.
- **Narration (ASR, unverified):** the one
- **Story function (INFERRED):** INFERRED: 2008 crisis comparison.
- **Continuity:** S0497.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0497 — f21636-21682 (901.542-903.458 s, 47 frames, 1.96 s) — shot SH190 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0705.jpg; entry EP0705, exit EP0707; second review: OK
- **Objects/placement (OBSERVED):** As S0495 without GIF; paragraph orange highlighted second sentence 'By comparison, homeownership only decreased by about 8 percentage points'; presenter smile.
- **Background:** white
- **Illustration:** Presenter smile.
- **Typography:** Serif.
- **Readable text:** By comparison, homeownership only decreased by about 8 percentage points during the financial crisis.
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfb:0.774 #dccbb8:0.087 #eabf2e:0.062 #ad7042:0.060 #1b1511:0.018
- **Hierarchy:** Highlight then presenter.
- **Camera/motion:** STATIC 2D; **entry/exit:** Exit of GIF EP0705; micro EP0706; hard replace EP0707.
- **Narration (ASR, unverified):** world, knocked it down by about eight.
- **Story function (INFERRED):** INFERRED: 8 points for 2008 vs 13.
- **Continuity:** S0495.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
- **Intra-state events:** EVI0218 (EXPRESSION_CHANGE, f21667) Presenter's mouth shifts to a slight smile and pointer arm changes slightly.

## S0498 — f21683-21713 (903.500-904.750 s, 31 frames, 1.29 s) — shot SH191 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0707.jpg; entry EP0707, exit EP0708; second review: MINOR
- **Objects/placement (OBSERVED):** Neutral presenter with tilted brows and hand at chin, centred (x .41-.58, y .1-.9).
- **Background:** flat off-white canvas
- **Illustration:** Beige head, black spiky hair.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.953 #f3d2b7:0.031 #080403:0.011 #97908b:0.002 #49403a:0.002
- **Hierarchy:** Single figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0707; exits hard replace EP0708.
- **Narration (ASR, unverified):** What we've built is a system that
- **Story function (INFERRED):** INFERRED: 'What we've built is a system that...'
- **Continuity:** S0462.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0499 — f21714-21733 (904.792-905.583 s, 20 frames, 0.83 s) — shot SH192 (inferred) — F1 character-only
- **Evidence:** frames/ep_stable/e0708.jpg; entry EP0708, exit EP0709; second review: OK
- **Objects/placement (OBSERVED):** Big green country-map character with eyes (x .19-.55, y .1-.85), half-lidded eyes, smug smile.
- **Background:** flat off-white canvas
- **Illustration:** Green flat map shape, googly eyes, short legs, black outline.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.811 #48a350:0.153 #030e03:0.025 #314d34:0.008 #a8aca8:0.004
- **Hierarchy:** Map dominates.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0708; additive EP0709.
- **Narration (ASR, unverified):** that protects the people
- **Story function (INFERRED):** INFERRED: the system/country.
- **Continuity:** S0476, S0500-S0502.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0500 — f21734-21763 (905.625-906.833 s, 30 frames, 1.25 s) — shot SH192 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0709.jpg; entry EP0709, exit EP0710; second review: MINOR
- **Objects/placement (OBSERVED):** Green map character left (x .12-.62); smiling grey-bob woman with purple scarf at right (x .67-.81, y .2-.85); small blue house with tree at right edge (x .82-1, y .45-.7).
- **Background:** flat off-white canvas
- **Illustration:** Woman grey hair, smile.
- **Typography:** none
- **Readable text:** none
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.755 #48a350:0.151 #060e08:0.050 #4c5c59:0.026 #b8bec4:0.017
- **Hierarchy:** Map then woman.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0709; motion EP0710.
- **Narration (ASR, unverified):** people already inside it,
- **Story function (INFERRED):** INFERRED: homeowner insider.
- **Continuity:** S0499.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0501 — f21783-21798 (907.667-908.292 s, 16 frames, 0.67 s) — shot SH192 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0710.jpg; entry EP0710, exit EP0711; second review: OK
- **Objects/placement (OBSERVED):** Presenter small seated at left (x .02-.2, y .5-.85); map with eyes open and BILL paper held at right (x .8-.9, y .38-.65); grey shape at right edge.
- **Background:** flat off-white canvas
- **Illustration:** Bill cream paper red 'BILL'.
- **Typography:** Red hand lettered 'BILL' ~3%.
- **Readable text:** BILL
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.779 #48a24f:0.138 #e9d7c7:0.037 #0c150a:0.035 #78746c:0.010
- **Hierarchy:** Map then bill.
- **Camera/motion:** STATIC 2D; **entry/exit:** Motion EP0710; additive EP0711.
- **Narration (ASR, unverified):** bill to whoever's
- **Story function (INFERRED):** INFERRED: passing the bill.
- **Continuity:** S0502.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0502 — f21799-21821 (908.333-909.250 s, 23 frames, 0.96 s) — shot SH192 (inferred) — F2 character+prop
- **Evidence:** frames/ep_stable/e0711.jpg; entry EP0711, exit EP0712; second review: OK
- **Objects/placement (OBSERVED):** Presenter at left; BILL paper on ground (x .1-.2, y .75-.9); map eyes narrowed; grey shape at right edge.
- **Background:** flat off-white canvas
- **Illustration:** As above.
- **Typography:** BILL
- **Readable text:** BILL
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.772 #49a251:0.155 #060f05:0.032 #e4d0bf:0.030 #41513f:0.012
- **Hierarchy:** Map then bill.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0711; hard replace via zoom EP0712.
- **Narration (ASR, unverified):** whoever's next in line.
- **Story function (INFERRED):** INFERRED: bill passed to next in line.
- **Continuity:** S0501.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0503 — f21857-21869 (910.750-911.250 s, 13 frames, 0.54 s) — shot SH193 (inferred) — F4 full-bleed screenshot/document
- **Evidence:** frames/ep_stable/e0712.jpg; entry EP0712, exit EP0713; second review: OK
- **Objects/placement (OBSERVED):** Full-bleed PDF title page: series header, small ISSN lines, centred title 'Illiquid Homeownership and the Bank of Mom and Dad', author 'Eirik Eylands Brandsaas', '2025-094', cite box at bottom.
- **Background:** white
- **Illustration:** Raw document.
- **Typography:** Serif ~1%-1.5% centred.
- **Readable text:** Finance and Economics Discussion Series; Illiquid Homeownership and the Bank of Mom and Dad; Eirik Eylands Brandsaas; 2025-094
- **Unreadable/uncertain text:** ISSN lines, cite box
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.974 #e1e2e1:0.010 #b7b7b7:0.008 #888888:0.006 #464646:0.002
- **Hierarchy:** Title first.
- **Camera/motion:** STATIC 2D; **entry/exit:** Zoom EP0712; additive EP0713.
- **Narration (ASR, unverified):** that bill are
- **Story function (INFERRED):** INFERRED: final callback to paper.
- **Continuity:** S0440, S0504-S0505.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0504 — f21870-21892 (911.292-912.208 s, 23 frames, 0.96 s) — shot SH193 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0713.jpg; entry EP0713, exit EP0714; second review: OK
- **Objects/placement (OBSERVED):** Same title page; curly-haired shocked character with phone and green cash at lower right (x .65-.97, y .5-1).
- **Background:** white
- **Illustration:** Curly brown hair, open mouth, phone dark, cash green.
- **Typography:** Serif.
- **Readable text:** Illiquid Homeownership and the Bank of Mom and Dad; 2025-094
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.935 #ccc1be:0.021 #3a312e:0.020 #080807:0.012 #858c81:0.012
- **Hierarchy:** Title then figure.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0713.
- **Narration (ASR, unverified):** are the ones whose rich
- **Story function (INFERRED):** INFERRED: next-generation reaction.
- **Continuity:** S0503.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0505 — f21893-21913 (912.250-913.083 s, 21 frames, 0.88 s) — shot SH193 (inferred) — F5 screenshot+character
- **Evidence:** frames/ep_stable/e0714.jpg; entry EP0714, exit EP0715; second review: OK
- **Objects/placement (OBSERVED):** Same page and shocked figure; top-hatted monocle moustache character at left (x .12-.25, y .15-1).
- **Background:** white
- **Illustration:** Top hat black, monocle gold, moustache.
- **Typography:** Serif.
- **Readable text:** Illiquid Homeownership and the Bank of Mom and Dad
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.889 #0a0908:0.042 #cfc1b4:0.030 #3a322e:0.024 #878c7e:0.014
- **Hierarchy:** Hat character then title.
- **Camera/motion:** STATIC 2D; **entry/exit:** Additive EP0714; motion EP0715.
- **Narration (ASR, unverified):** rich daddy can cover
- **Story function (INFERRED):** INFERRED: rich parent.
- **Continuity:** S0504.
- **Confidence:** HIGH; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.

## S0506 — f21946-22096 (914.458-920.708 s, 151 frames, 6.29 s) — shot SH194 (inferred) — F10 title/end card
- **Evidence:** frames/ep_stable/e0715.jpg; entry EP0715, exit end of video; second review: MINOR
- **Objects/placement (OBSERVED):** End card: empty circle (x .07-.23, y .06-.4), 'Subscribe for more' with bold 'Casual Finance' (x .25-.6, y .05-.18), 'the insider club' and three handle lines at right (x .65-.9, y .12-.3), large empty rectangle (x .15-.55, y .42-.88).
- **Background:** flat off-white canvas
- **Illustration:** Hand-drawn thin black outlines, handwritten lettering.
- **Typography:** Handwritten ~4-5% height; bold brand line.
- **Readable text:** Subscribe for more; the insider club; @AdamShake-pm4kw; @user-sy4gy3tdl4; @ChrisPVille
- **Unreadable/uncertain text:** none flagged
- **Palette (MEASURED, top-5 k-means of representative frame):** #fcfcfc:0.957 #080808:0.020 #bebebe:0.009 #454545:0.008 #828282:0.006
- **Hierarchy:** Subscribe text then empty boxes.
- **Camera/motion:** STATIC 2D; **entry/exit:** Hard replace EP0715; end of video.
- **Narration (ASR, unverified):** —
- **Story function (INFERRED):** INFERRED: CTA subscribe end card.
- **Continuity:** None before.
- **Confidence:** MEDIUM; **evidence split:** OBSERVED: layout, objects, text as described; INFERRED: story function from unverified ASR.
