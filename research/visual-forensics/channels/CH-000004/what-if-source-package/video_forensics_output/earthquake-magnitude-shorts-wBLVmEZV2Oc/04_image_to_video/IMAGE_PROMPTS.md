# IMAGE PROMPTS — earthquake-magnitude-shorts-wBLVmEZV2Oc

Master style, reused in every prompt below: black-line hand-drawn/marker-sketch illustration style, thin uniform stroke weight, flat light-grey fills only (no gradients, no 3D shading, no textures), pure white background, no camera perspective (flat 2D graphic), vertical 1080x1920 canvas with generous negative space around the subject so text can be added on top later.

Per the UNIQUE IMAGE RULE, only 8 source images are needed for the entire 66s video — everything else is a reused image, a text/shape overlay in final assembly, or a crossfade between two of these images.

## IMG01
USED BY SHOTS / STATES: F01.0-F01.2
SOURCE STATE: opening
REUSE RELATIONSHIP: none (single use)
TEXT BAKED: NO (title text added in final assembly, per TEXT RULE)
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch illustration of an old mechanical seismograph: a wooden stand holding a paper-drum recorder on the left connected to a long pen arm on the right, with a thin wavy ink line already drawn on the paper. Flat light-grey shading on the drum and stand only, no gradients, no 3D rendering. Pure white background, centered composition, wide empty margin above and below for text overlay. Vertical 1080x1920 frame, flat 2D orthographic view, no camera perspective, no additional objects."

## IMG02
USED BY SHOTS / STATES: F01.3-F01.4
SOURCE STATE: newspaper/phone/LIVE-box composite
REUSE RELATIONSHIP: none (single use)
TEXT BAKED: NO — headline, SMS text, and LIVE-box dialogue are added in final assembly as CLEAN PLATE + TEXT OVERLAY (exact wording control)
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch, flat 2D, three separate elements arranged vertically on a pure white 1080x1920 canvas: top third, a folded newspaper with a blank masthead banner and a blank headline block above a small corn-field line-art illustration; bottom-left third, a smartphone outline with a blank chat-bubble area and a small simple dog icon beside it; bottom-right third, a black rounded-rectangle frame containing two simple stick figures (circle heads, line bodies) facing each other with blank speech-bubble areas above them. No text anywhere in the image. Flat light-grey fills only, no gradients, generous white margins between the three elements."
CLEAN PLATE: blank headline area on newspaper, blank SMS bubble on phone, blank speech bubbles in LIVE box
TEXT OVERLAY: "3.5 EARTHQUAKE STRIKES FEAR IN OHIO CORN FIELD" (newspaper headline, small caps) · "SMALL DOG WAS FRIGHTENED BY 4.8 EARTHQUAKE" / "WE MUST STOP THIS AT THE SOURCE!" (phone, two lines) · "IT'S AT LEAST AN 8 ON THE RICHTER SCALE!" / "UHM, ACTUALLY..." (LIVE box, two speech bubbles) — position: each in its own blank area noted above; color: black; timing: all appear together at 5.00s

## IMG03
USED BY SHOTS / STATES: F01.5-F01.9
SOURCE STATE: bare/growing ruler
REUSE RELATIONSHIP: none (single use — the ruler is also reused as a persistent CLEAN PLATE element composited under every later image, see I2V_REBUILD.md)
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of a tall vertical ruler/number-line: a single vertical line with evenly spaced horizontal tick marks running its full height, numbered '0' near the bottom rising to '30' near the top in increments of 5, small hand-lettered digits beside each labeled tick. Centered on a pure white 1080x1920 canvas, thin uniform black linework, no color, no shading, no other objects, wide empty margins on both sides for later text/graphic overlays."

## IMG04
USED BY SHOTS / STATES: F01.10-F01.12
SOURCE STATE: Magnitude 9 globe
REUSE RELATIONSHIP: base for IMG05 (Magnitude 15) via added damage overlay
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of a simple grey globe of Earth viewed from space, showing Asia and the western Pacific, flat light-grey landmass fill with black coastline linework, a small circular rotation-arrow icon at the top-left of the globe implying slow spin. Two small red concentric ripple/epicenter marks placed over Japan and over Indonesia. Pure white background, centered, vertical 1080x1920 canvas, generous margin around the globe for a title above and a small caption box below, flat 2D, no shading gradients."

## IMG05
USED BY SHOTS / STATES: F01.15-F01.17
SOURCE STATE: Magnitude 11→15 globe (damage escalation)
REUSE RELATIONSHIP: same base globe as IMG04 (North America facing instead of Asia), reused across two damage stages via crossfade in final assembly
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of a simple grey globe of Earth viewed from space, showing North America, flat light-grey landmass fill with black coastline linework, small rotation-arrow icon top-left. A single jagged black crack line splits across the continent, and the globe's outer circular edge is broken into a dense jagged spiky silhouette all the way around, like a cracked eggshell. Pure white background, centered, vertical 1080x1920 canvas, flat 2D, no gradients, generous margin for a title above."

## IMG06
USED BY SHOTS / STATES: F01.13-F01.14
SOURCE STATE: Magnitude 10 fault blocks
REUSE RELATIONSHIP: none (single use)
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of two overlapping isometric rock slabs with jagged torn top edges, resembling a fractured tectonic fault block, flat light-grey fill on the slab tops, black linework, offset diagonally from each other suggesting a shift/fault. Pure white background, centered, vertical 1080x1920 canvas, flat 2D illustration style, no shading gradients, empty margin below for a measurement-arrow caption."

## IMG07
USED BY SHOTS / STATES: F01.20, F01.22 (two density stages via reuse + overlay, see below)
SOURCE STATE: Magnitude 18/>18 debris explosion
REUSE RELATIONSHIP: base image; a second overlay pass (IMG07B, additive fragments only) is composited on top for F01.22's escalation rather than regenerating a full new image
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of a planet broken apart into a dozen irregular jagged chunks scattered outward from a central point, thin radiating streak lines trailing behind each chunk to suggest explosive motion, flat light-grey fill on the chunks, black linework, no other objects. Pure white background, centered, vertical 1080x1920 canvas, flat 2D, no gradients, generous margin above for title/subtitle text."

## IMG07B (overlay, not a full new image)
USED BY: F01.22 only, composited over IMG07
DESCRIPTION: 6-8 additional small jagged fragments and longer radiating streak lines, same style as IMG07, generated on a transparent background so it can be laid over IMG07 to sell the finale's "more fragments than before" escalation without a full regeneration.

## IMG08
USED BY SHOTS / STATES: F01.21 (and reused frame-only for F01.3-4 and F01.12's LIVE boxes — see REUSE)
SOURCE STATE: LIVE broadcast box template
REUSE RELATIONSHIP: this is the G01 template — generate the empty frame ONCE, then reuse it for all three LIVE-box appearances (F01.3-4, F01.12, F01.21) by compositing a different stick-figure pose/prop (from a small separate pose sheet, not a full new background image) and different caption text inside it each time
TEXT BAKED: NO
STANDALONE IMAGE PROMPT:
"Black-line hand-drawn sketch of a rounded-corner black-bordered rectangle frame (broadcast/news-alert box style) with a small 'LIVE' tag in the bottom-left corner, interior left empty/transparent for a character to be composited in, and empty space above the frame for a caption line. Pure white background outside the frame, vertical 1080x1920 canvas, flat 2D, no gradients, no other content inside the frame."

## POSE SHEET (not a numbered IMG — small supplementary asset for C01)
"Black-line hand-drawn sketch, four small simple stick figures (circle heads, straight-line limbs, dot eyes) on a pure white background, each in its own clear quadrant: (1) two figures facing each other mid-conversation; (2) one figure standing beside a small circular badge icon; (3) one figure with both arms raised overhead and a small scribble/shout mark above its head; (4) one figure wearing a simple headset-and-microphone shape over its head. Flat 2D, thin uniform linework, no color, no shading, generous white space between each figure for individual cropping."
