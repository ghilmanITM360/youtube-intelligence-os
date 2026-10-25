# WAY 2 — Animation/event prompts

A-IDs are shared with MOTION_EVENTS.csv. Each prompt specifies only change. These are control prompts; exact text, one-frame replacements and short reveals should be executed deterministically during final assembly because generative interpolation would reduce fidelity. No prompt is provided for a static hold.

For every later event, SOURCE IMAGE means the named master **plus the current preceding composite state**. Preserve every already-added label, cloud and object. An instantaneous event needs a still replacement, not a generated movement clip. Its one-frame CLIP DURATION is the transition interval; the following held duration comes from TIMELINE.csv. For a reveal, the final changed frame is the fully visible target; OUT is exclusive.

For the two lighting events, a model supporting sufficiently short controlled clips may be tried with the supplied first/target state reference. If it drifts or cannot match timing, composite the fixed image with the measured opacity treatment in final assembly. This remains WAY 2. Never generate exact text or unnecessary character movement.

## A01


ANIMATION ID: A01

SHOT ID: S01

SOURCE IMAGE: IMG01 + preceding composite

SOURCE STATE: F01.0

TARGET STATE: F01.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:01.292–00:01.333

MOVING ELEMENT: G01 TAP cloud

STATIC ANCHORS: Board; both figures; furniture; laptop; books; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Reveal the first TAP word cloud inside the board. Use an abrupt state change with no in-between travel. Keep board; both figures; furniture; laptop; books; camera. Preserve the supplied linework and scale.

## A02


ANIMATION ID: A02

SHOT ID: S01

SOURCE IMAGE: IMG01 + preceding composite

SOURCE STATE: F01.1

TARGET STATE: F01.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:02.875–00:02.917

MOVING ELEMENT: G01 TAP cloud

STATIC ANCHORS: Board; both figures; furniture; laptop; books; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace the cloud with its denser upper-right variant. Use an abrupt state change with no in-between travel. Keep board; both figures; furniture; laptop; books; camera. Preserve the supplied linework and scale.

## A03


ANIMATION ID: A03

SHOT ID: S02

SOURCE IMAGE: IMG02 + IMG03 probe/contact variant + preceding composite

SOURCE STATE: F02.0

TARGET STATE: F02.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:05.667–00:05.708

MOVING ELEMENT: O03 probe

STATIC ANCHORS: Circuit base; framing; white field.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the stationary striped probe hovering above the raised key. Use an abrupt state change with no in-between travel. Keep circuit base; framing; white field. Preserve the supplied linework and scale.

## A04


ANIMATION ID: A04

SHOT ID: S02

SOURCE IMAGE: IMG02 + IMG03 probe/contact variant + preceding composite

SOURCE STATE: F02.1

TARGET STATE: F02.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:06.500–00:06.542

MOVING ELEMENT: O02/O03 pressed key and probe; TAP leader

STATIC ANCHORS: Circuit base; framing; white field.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace raised key/probe with contact pose, buckled dome, impact ticks and TAP leader simultaneously. Use an abrupt state change with no in-between travel. Keep circuit base; framing; white field. Preserve the supplied linework and scale.

## A05


ANIMATION ID: A05

SHOT ID: S04

SOURCE IMAGE: IMG05 + preceding composite

SOURCE STATE: F04.0

TARGET STATE: F04.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:14.250–00:14.292

MOVING ELEMENT: G03 letter-key group

STATIC ANCHORS: Keyboard; paper edges; Figure 2; unreadable body marks; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the red letter-key TAP, 1.5 mJ and A S D key icons together. Use an abrupt state change with no in-between travel. Keep keyboard; paper edges; figure 2; unreadable body marks; framing. Preserve the supplied linework and scale.

## A06


ANIMATION ID: A06

SHOT ID: S04

SOURCE IMAGE: IMG05 + preceding composite

SOURCE STATE: F04.1

TARGET STATE: F04.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:16.417–00:16.458

MOVING ELEMENT: G03 spacebar group

STATIC ANCHORS: Keyboard; paper edges; Figure 2; unreadable body marks; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Add red spacebar TAP, 2.5 mJ and long key outline together. Use an abrupt state change with no in-between travel. Keep keyboard; paper edges; figure 2; unreadable body marks; framing. Preserve the supplied linework and scale.

## A07


ANIMATION ID: A07

SHOT ID: S05

SOURCE IMAGE: IMG06 + preceding composite

SOURCE STATE: F05.0

TARGET STATE: F05.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:21.125–00:21.167

MOVING ELEMENT: O06/G04 droplet and temperature

STATIC ANCHORS: Title; canvas; all already-revealed comparison graphics.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Reveal droplet and temperature label together. Use an abrupt state change with no in-between travel. Keep title; canvas; all already-revealed comparison graphics. Preserve the supplied linework and scale.

## A08


ANIMATION ID: A08

SHOT ID: S05

SOURCE IMAGE: IMG06 + preceding composite

SOURCE STATE: F05.1

TARGET STATE: F05.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:24.083–00:24.125

MOVING ELEMENT: C05/G04 squirrel and caption

STATIC ANCHORS: Title; canvas; all already-revealed comparison graphics.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Reveal the stationary squirrel with its upward-arrow caption. Use an abrupt state change with no in-between travel. Keep title; canvas; all already-revealed comparison graphics. Preserve the supplied linework and scale.

## A09


ANIMATION ID: A09

SHOT ID: S05

SOURCE IMAGE: IMG06 + preceding composite

SOURCE STATE: F05.2

TARGET STATE: F05.3

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:27.667–00:27.708

MOVING ELEMENT: C05/G05 local squirrel patch

STATIC ANCHORS: Title; droplet; temperature; squirrel caption; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Instantly replace only the squirrel silhouette with the reference ground-stroke variant. Keep the title, droplet, temperature and squirrel caption fixed. Do not animate a hop or add in-between motion. End with the two reference strokes visible beneath the feet.

## A10


ANIMATION ID: A10

SHOT ID: S06

SOURCE IMAGE: IMG07 + preceding composite

SOURCE STATE: F06.0

TARGET STATE: F06.2

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:31.125–00:31.417

MOVING ELEMENT: T01 headline

STATIC ANCHORS: Book; page text; TYPICAL NOVEL label; framing.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked camera. Reveal the supplied headline plate from left to right over seven frames. Keep the book, page text and background absolutely fixed. End with the complete headline visible. Do not redraw lettering.

## A11


ANIMATION ID: A11

SHOT ID: S06

SOURCE IMAGE: IMG07 + preceding composite

SOURCE STATE: F06.2

TARGET STATE: F06.4

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:31.750–00:32.042

MOVING ELEMENT: G06 red arrows

STATIC ANCHORS: Book; page text; TYPICAL NOVEL label; framing.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked frame. Reveal only the supplied red curved arrow strokes from their upper starts toward the page endpoints over seven frames. Preserve the book, headline, text and all framing. End with all six arrows complete.

## A12


ANIMATION ID: A12

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.0

TARGET STATE: F07.1

CLIP DURATION: 10 frame(s), 0.416667 s; global 00:35.833–00:36.250

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 1 from left to right over 10 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A13


ANIMATION ID: A13

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.1

TARGET STATE: F07.3

CLIP DURATION: 3 frame(s), 0.125000 s; global 00:36.250–00:36.375

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 1 from left to right over 3 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A14


ANIMATION ID: A14

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.3

TARGET STATE: F07.5

CLIP DURATION: 3 frame(s), 0.125000 s; global 00:36.375–00:36.500

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 1 from left to right over 3 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A15


ANIMATION ID: A15

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.5

TARGET STATE: F07.7

CLIP DURATION: 3 frame(s), 0.125000 s; global 00:36.542–00:36.667

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 1 from left to right over 3 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A16


ANIMATION ID: A16

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.7

TARGET STATE: F07.9

CLIP DURATION: 6 frame(s), 0.250000 s; global 00:36.667–00:36.917

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 1 from left to right over 6 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A17


ANIMATION ID: A17

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.9

TARGET STATE: F07.11

CLIP DURATION: 5 frame(s), 0.208333 s; global 00:36.917–00:37.125

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 2 from left to right over 5 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A18


ANIMATION ID: A18

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.11

TARGET STATE: F07.13

CLIP DURATION: 3 frame(s), 0.125000 s; global 00:37.167–00:37.292

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 2 from left to right over 3 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A19


ANIMATION ID: A19

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.13

TARGET STATE: F07.15

CLIP DURATION: 9 frame(s), 0.375000 s; global 00:37.292–00:37.667

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 2 from left to right over 9 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A20


ANIMATION ID: A20

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.15

TARGET STATE: F07.17

CLIP DURATION: 3 frame(s), 0.125000 s; global 00:37.667–00:37.792

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 2 from left to right over 3 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A21


ANIMATION ID: A21

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.17

TARGET STATE: F07.19

CLIP DURATION: 11 frame(s), 0.458333 s; global 00:37.792–00:38.250

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 2 from left to right over 11 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A22


ANIMATION ID: A22

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.19

TARGET STATE: F07.21

CLIP DURATION: 5 frame(s), 0.208333 s; global 00:38.250–00:38.458

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 2 from left to right over 5 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A23


ANIMATION ID: A23

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.21

TARGET STATE: F07.23

CLIP DURATION: 11 frame(s), 0.458333 s; global 00:38.458–00:38.917

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 3 from left to right over 11 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A24


ANIMATION ID: A24

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.23

TARGET STATE: F07.25

CLIP DURATION: 12 frame(s), 0.500000 s; global 00:39.208–00:39.708

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 4 from left to right over 12 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A25


ANIMATION ID: A25

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.25

TARGET STATE: F07.27

CLIP DURATION: 15 frame(s), 0.625000 s; global 00:39.708–00:40.333

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 5 from left to right over 15 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A26


ANIMATION ID: A26

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.27

TARGET STATE: F07.29

CLIP DURATION: 8 frame(s), 0.333333 s; global 00:41.208–00:41.542

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 6 from left to right over 8 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A27


ANIMATION ID: A27

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.28

TARGET STATE: F07.30

CLIP DURATION: 4 frame(s), 0.166667 s; global 00:41.500–00:41.667

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 6 from left to right over 4 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A28


ANIMATION ID: A28

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.30

TARGET STATE: F07.32

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:41.667–00:41.958

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 7 from left to right over 7 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A29


ANIMATION ID: A29

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.31

TARGET STATE: F07.33

CLIP DURATION: 5 frame(s), 0.208333 s; global 00:41.917–00:42.125

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 7 from left to right over 5 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A30


ANIMATION ID: A30

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.32

TARGET STATE: F07.34

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:42.083–00:42.375

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 8 from left to right over 7 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A31


ANIMATION ID: A31

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.34

TARGET STATE: F07.36

CLIP DURATION: 5 frame(s), 0.208333 s; global 00:42.375–00:42.583

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 8 from left to right over 5 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A32


ANIMATION ID: A32

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.35

TARGET STATE: F07.37

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:42.542–00:42.833

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 9 from left to right over 7 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A33


ANIMATION ID: A33

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.37

TARGET STATE: F07.39

CLIP DURATION: 4 frame(s), 0.166667 s; global 00:42.833–00:43.000

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 9 from left to right over 4 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A34


ANIMATION ID: A34

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.39

TARGET STATE: F07.41

CLIP DURATION: 7 frame(s), 0.291667 s; global 00:43.000–00:43.292

MOVING ELEMENT: T01 black text

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied black artwork strip for line 10 from left to right over 7 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A35


ANIMATION ID: A35

SHOT ID: S07

SOURCE IMAGE: REUSE IMG06 blank region / E01 + exact T01/G07 overlays + preceding composite

SOURCE STATE: F07.40

TARGET STATE: F07.42

CLIP DURATION: 5 frame(s), 0.208333 s; global 00:43.250–00:43.458

MOVING ELEMENT: G07 red strike

STATIC ANCHORS: Previously exposed letters and red strokes; white field; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked white canvas. Reveal only the supplied red artwork strip for line 10 from left to right over 5 frames. Preserve all existing letters and red strokes without reflow. Keep exact lettering as an editor overlay. End with this strip fully visible.

## A36


ANIMATION ID: A36

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.0

TARGET STATE: F08.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:46.167–00:46.208

MOVING ELEMENT: O09 book

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show one closed book at the fixed tabletop position. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A37


ANIMATION ID: A37

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.1

TARGET STATE: F08.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:47.750–00:47.792

MOVING ELEMENT: G08 first label

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the first energy label and curved arrow. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A38


ANIMATION ID: A38

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.2

TARGET STATE: F08.3

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:49.208–00:49.250

MOVING ELEMENT: O09 book stack

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace the one-book image with two stacked books. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A39


ANIMATION ID: A39

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.3

TARGET STATE: F08.4

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:49.375–00:49.417

MOVING ELEMENT: O09 book stack

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace two books with three stacked books. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A40


ANIMATION ID: A40

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.4

TARGET STATE: F08.5

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:50.125–00:50.167

MOVING ELEMENT: G08 second label/bracket

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the second energy label with curved leader and stack bracket. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A41


ANIMATION ID: A41

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.5

TARGET STATE: F08.6

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:51.708–00:51.750

MOVING ELEMENT: O09 ten-book stack

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace three books with ten books; preserve the bottom-book tabletop anchor. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A42


ANIMATION ID: A42

SHOT ID: S08

SOURCE IMAGE: IMG08 + IMG09 count variants + preceding composite

SOURCE STATE: F08.6

TARGET STATE: F08.7

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:53.917–00:53.958

MOVING ELEMENT: O10/G08 cell and label

STATIC ANCHORS: Figure posture; chair; table; key fixture; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the tiny upright cell-like object and third energy arrow/label simultaneously. Use an abrupt state change with no in-between travel. Keep figure posture; chair; table; key fixture; camera. Preserve the supplied linework and scale.

## A43


ANIMATION ID: A43

SHOT ID: S09

SOURCE IMAGE: IMG10 + IMG11 connection/reading patches + preceding composite

SOURCE STATE: F09.0

TARGET STATE: F09.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 00:58.250–00:58.292

MOVING ELEMENT: O12/G09 cable, outlet, plug, red marks

STATIC ANCHORS: Desk; chair; laptop; upright book; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the cable, outlet panel, plug and red laptop burst together. Use an abrupt state change with no in-between travel. Keep desk; chair; laptop; upright book; camera. Preserve the supplied linework and scale.

## A44


ANIMATION ID: A44

SHOT ID: S09

SOURCE IMAGE: IMG10 + IMG11 connection/reading patches + preceding composite

SOURCE STATE: F09.1

TARGET STATE: F09.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:00.875–01:00.917

MOVING ELEMENT: G09 time label

STATIC ANCHORS: Desk; chair; laptop; upright book; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the red time label above the right-hand upright book. Use an abrupt state change with no in-between travel. Keep desk; chair; laptop; upright book; camera. Preserve the supplied linework and scale.

## A45


ANIMATION ID: A45

SHOT ID: S09

SOURCE IMAGE: IMG10 + IMG11 connection/reading patches + preceding composite

SOURCE STATE: F09.2

TARGET STATE: F09.3

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:02.417–01:02.458

MOVING ELEMENT: C02/O13/G09 reading pose and months label

STATIC ANCHORS: Desk; chair; laptop; upright book; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Replace only the figure with its book-reading pose and reveal the months label. Use an abrupt state change with no in-between travel. Keep desk; chair; laptop; upright book; camera. Preserve the supplied linework and scale.

## A46


ANIMATION ID: A46

SHOT ID: S10

SOURCE IMAGE: IMG12 + IMG13 lower callout + preceding composite

SOURCE STATE: F10.0

TARGET STATE: F10.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:09.042–01:09.083

MOVING ELEMENT: C02/O15/G11 internet callout

STATIC ANCHORS: Calendar; red booklets/arrows; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the lower computer-user illustration and its exact supplied speech lettering together. Use an abrupt state change with no in-between travel. Keep calendar; red booklets/arrows; camera. Preserve the supplied linework and scale.

## A47


ANIMATION ID: A47

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.0

TARGET STATE: F11.2

CLIP DURATION: 5 frame(s), 0.208333 s; global 01:14.667–01:14.875

MOVING ELEMENT: G01 local TAP/CLICK cloud

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked view. Reveal the supplied local TAP/CLICK cloud outward from the head-monitor area over five frames. Keep the gamer, hands, headset, monitor, desk, chair and command sequence completely still. Do not generate or deform the words.

## A48


ANIMATION ID: A48

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.2

TARGET STATE: F11.4

CLIP DURATION: 4 frame(s), 0.166667 s; global 01:17.708–01:17.875

MOVING ELEMENT: G13 headline and G01 cloud

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked view. Uncover the supplied headline and wider horizontal word field over four frames, expanding outward. Keep the existing gamer, input code, furniture and earlier words fixed. End with the complete supplied headline; do not regenerate lettering.

## A49


ANIMATION ID: A49

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.4

TARGET STATE: F11.5

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:20.000–01:20.042

MOVING ELEMENT: G01 upper word cloud

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Reveal the additional upper word cloud above the headline. Use an abrupt state change with no in-between travel. Keep desk; chair; monitor; command sequence; framing. Preserve the supplied linework and scale.

## A50


ANIMATION ID: A50

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.5

TARGET STATE: F11.6

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:21.250–01:21.292

MOVING ELEMENT: G01 lower/side cloud

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Reveal the additional lower and side word fields around the desk. Use an abrupt state change with no in-between travel. Keep desk; chair; monitor; command sequence; framing. Preserve the supplied linework and scale.

## A51


ANIMATION ID: A51

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.6

TARGET STATE: F11.8

CLIP DURATION: 6 frame(s), 0.250000 s; global 01:22.042–01:22.292

MOVING ELEMENT: G14 lighting composite

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Optional isolated light pass; exact opacity composite preferred

ANIMATION PROMPT:
Locked frame. Over six frames darken the existing scene to charcoal while retaining a soft stationary light pool between monitor, face and keyboard. Nothing changes position or shape. Preserve all words. End in the supplied dark reference state.

## A52


ANIMATION ID: A52

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.8

TARGET STATE: F11.9

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:23.292–01:23.333

MOVING ELEMENT: G01 central word-field increment

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Add the observed central TAP and CLICK instances; retain the dark lighting. Use an abrupt state change with no in-between travel. Keep desk; chair; monitor; command sequence; framing. Preserve the supplied linework and scale.

## A53


ANIMATION ID: A53

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.9

TARGET STATE: F11.10

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:23.500–01:23.542

MOVING ELEMENT: G01 surrounding word-field increment

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Add the observed outer TAP and CLICK instances; retain the dark lighting. Use an abrupt state change with no in-between travel. Keep desk; chair; monitor; command sequence; framing. Preserve the supplied linework and scale.

## A54


ANIMATION ID: A54

SHOT ID: S11

SOURCE IMAGE: IMG14 + preceding composite

SOURCE STATE: F11.10

TARGET STATE: F11.12

CLIP DURATION: 6 frame(s), 0.250000 s; global 01:25.458–01:25.708

MOVING ELEMENT: G14 lighting composite

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Optional isolated light pass; exact opacity composite preferred

ANIMATION PROMPT:
Locked frame. Over six frames remove the dark treatment and restore the original off-white scene. The stationary monitor light merges into the bright background. Preserve every line, word, object, position and pose. End at the original white level.

## A55


ANIMATION ID: A55

SHOT ID: S11

SOURCE IMAGE: IMG14 preceding composite + IMG15 pose patch + preceding composite

SOURCE STATE: F11.12

TARGET STATE: F11.13

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:27.250–01:27.292

MOVING ELEMENT: C03 gamer pose

STATIC ANCHORS: Desk; chair; monitor; command sequence; framing.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Instantly replace the typing figure with the head-in-hands pose; do not interpolate a gesture. Use an abrupt state change with no in-between travel. Keep desk; chair; monitor; command sequence; framing. Preserve the supplied linework and scale.

## A56


ANIMATION ID: A56

SHOT ID: S12

SOURCE IMAGE: IMG16 + preceding composite

SOURCE STATE: F12.0

TARGET STATE: F12.1

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:31.500–01:31.542

MOVING ELEMENT: O12/G14 cable and illumination

STATIC ANCHORS: Typist pose; furniture; two books; laptop; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the connecting cable, white head rim and soft laptop light together. Use an abrupt state change with no in-between travel. Keep typist pose; furniture; two books; laptop; camera. Preserve the supplied linework and scale.

## A57


ANIMATION ID: A57

SHOT ID: S12

SOURCE IMAGE: IMG16 + preceding composite

SOURCE STATE: F12.1

TARGET STATE: F12.2

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:33.750–01:33.792

MOVING ELEMENT: O13/G15 book icon and rays

STATIC ANCHORS: Typist pose; furniture; two books; laptop; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the tilted stationary book icon and its short radiating strokes. Use an abrupt state change with no in-between travel. Keep typist pose; furniture; two books; laptop; camera. Preserve the supplied linework and scale.

## A58


ANIMATION ID: A58

SHOT ID: S12

SOURCE IMAGE: IMG16 + preceding composite

SOURCE STATE: F12.2

TARGET STATE: F12.3

CLIP DURATION: 1 frame(s), 0.041667 s; global 01:34.542–01:34.583

MOVING ELEMENT: G01/G15 large cloud and time

STATIC ANCHORS: Typist pose; furniture; two books; laptop; camera.

EXECUTION: Instant composite/hold, no generative pass

ANIMATION PROMPT:
Locked frame. Show the upper TAP cloud and red time caption together. Use an abrupt state change with no in-between travel. Keep typist pose; furniture; two books; laptop; camera. Preserve the supplied linework and scale.

## A59


ANIMATION ID: A59

SHOT ID: S13

SOURCE IMAGE: IMG17 + preceding composite

SOURCE STATE: F13.0

TARGET STATE: F13.2

CLIP DURATION: 7 frame(s), 0.291667 s; global 01:37.167–01:37.458

MOVING ELEMENT: G16 two-line final caption

STATIC ANCHORS: Entire outdoor illustration; runner pose; tree leaves; seated figure; book; camera.

EXECUTION: Exact overlay/mask animation during assembly

ANIMATION PROMPT:
Locked outdoor drawing. Reveal the supplied two-line caption simultaneously from left to right over seven frames. Keep the seated person, laptop, book, runner, grass, tree and every leaf perfectly still. End with the full caption visible.

