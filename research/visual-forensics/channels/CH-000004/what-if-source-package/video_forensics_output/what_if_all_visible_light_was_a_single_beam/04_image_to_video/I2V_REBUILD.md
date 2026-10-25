# WAY 2 — Image-to-Video Shot Build

Reference `IMAGE_PROMPTS.md` for IMG## prompts and `ANIMATION_PROMPTS.md` for A## prompts. Text/graphic overlay wording and timing are in `02_analysis/TIMELINE.csv`; not repeated here.

## S01 — 0:00.000–0:06.567
STATE CHAIN: F01.0 → A01 → F01.1 → A02 → F01.2
SOURCE IMAGE: IMG01
IMAGE ACTION: GENERATE
I2V PASS: A01, then A02 (chained — A02 starts from A01's resulting frame, not from IMG01 again)
EXPECTED RESULT: F01.2 (narrow 1m beam, "UNINHABITABLE EARTH" caption)
TEXT / GRAPHICS: overlay "UN-SUN-SPECTING EARTH" / "UNINHABITABLE EARTH" / "1m" per TIMELINE.csv timings
AUDIO SYNC: continuous mixed audio under the whole shot
CUT TO: S02

## S02 — 0:06.600–0:15.900
STATE CHAIN: F02.0 → A03 → F02.1 → A04 → F02.2
SOURCE IMAGE: IMG02
IMAGE ACTION: GENERATE
I2V PASS: A03, then A04 (chained)
EXPECTED RESULT: F02.2 (letters + subatomic symbols)
TEXT / GRAPHICS: molecule-name letters are part of IMG02/the A03 result (generated content, not overlay text)
AUDIO SYNC: continuous mixed audio
CUT TO: S03
FIDELITY RISK: if the I2V model cannot reliably keep the scattered-letter shapes legible through A03's disintegration motion, treat legibility of the individual letters as POSSIBLE rather than guaranteed; the overall silhouette-to-particles read is the priority.

## S03 — 0:15.900–0:22.000
STATE CHAIN: F03.0 → A05 → F03.1 → A06 → F03.2
SOURCE IMAGE: IMG03
IMAGE ACTION: GENERATE
I2V PASS: A05, then A06 (chained)
EXPECTED RESULT: F03.2 (both stat captions + disclaimer visible)
TEXT / GRAPHICS: overlay the two energy captions and the disclaimer paragraph per TIMELINE.csv (simplest to add as overlay text rather than bake into the I2V generation, since exact wording must be precise)
AUDIO SYNC: continuous mixed audio
CUT TO: S04

## S04 — 0:22.000–0:40.500
STATE CHAIN: F04.0 → A07 → F04.1 → A08 → F04.2 → A09 → F04.3
SOURCE IMAGE: IMG04
IMAGE ACTION: GENERATE
I2V PASS: A07, A08, A09 (chained in sequence; A08 covers both the growth and the long static hold — extend/freeze the last frame for the remaining hold duration if the model's native clip length is shorter than 11.0s)
EXPECTED RESULT: F04.3 (fully reddened ground, cracks, dome)
TEXT / GRAPHICS: overlay "MILLIONS OF DEGREES...", "PLASMA", "X-RAYS", "MORE PLASMA" per TIMELINE.csv timings
INDEPENDENT PASSES: if the model struggles to keep the dome-growth (A08) and the ground-wide reddening (A09) coherent in one continuation, split A09 into its own fresh pass seeded from A08's last frame rather than degrading A08's result.
AUDIO SYNC: continuous mixed audio
CUT TO: S05

## S05 — 0:40.500–0:49.800
STATE CHAIN: F05.0 → A10 → F05.1
SOURCE IMAGE: IMG05
IMAGE ACTION: GENERATE
I2V PASS: A10
EXPECTED RESULT: F05.1 ("NOT SAFE!" + icon)
TEXT / GRAPHICS: overlay "RIP" (static) and the "SAFE?"→"NOT SAFE!" swap per TIMELINE.csv
AUDIO SYNC: continuous mixed audio
CUT TO: S06

## S06 — 0:49.800–0:52.600
STATE CHAIN: F06.0 → A11 → F06.1
SOURCE IMAGE: IMG06 (generated wide)
IMAGE ACTION: GENERATE
I2V PASS: A11 (camera-pan style prompt) — if the I2V model does not support a pure camera-pan instruction reliably, fall back to a CapCut-style position/crop keyframe over the static wide image instead of a generated pan.
EXPECTED RESULT: F06.1 (next tombstone centered)
TEXT / GRAPHICS: overlay tombstone text per TIMELINE.csv; the third, partially-framed stone's text is UNCONFIRMED — leave blank or reuse "MOONLIGHT" only if a placeholder is acceptable, otherwise omit
AUDIO SYNC: continuous mixed audio
CUT TO: S07

## S07 — 0:52.600–0:56.100
STATE CHAIN: F07.0 → A12 → F07.1
SOURCE IMAGE: IMG07
IMAGE ACTION: GENERATE
I2V PASS: A12
EXPECTED RESULT: F07.1 (cracks forming on terminator)
TEXT / GRAPHICS: overlay "TWILIGHT" (static)
AUDIO SYNC: continuous mixed audio
CUT TO: S08 (no image regeneration — S08 continues directly from F07.1)

## S08 — 0:56.100–1:23.700
STATE CHAIN: F08.0 → A13 → F08.1
SOURCE IMAGE: IMG07 (reused directly, continuing from S07's resulting frame — IMAGE ACTION: REUSE)
IMAGE ACTION: REUSE
I2V PASS: A13
EXPECTED RESULT: F08.1 (ring fully closed)
INDEPENDENT PASSES: A13's ~20s duration likely exceeds a single I2V generation's native clip length; generate it as 3-4 chained sub-passes (e.g. ~5s each), each starting from the previous sub-pass's last frame, all using the same A13 prompt text so the ring keeps growing in the same direction without resetting or reversing.
TEXT / GRAPHICS: "TWILIGHT" caption persists (carried from S07)
AUDIO SYNC: continuous mixed audio; brief measured silence (75.226s-75.393s) falls late in this motion — no visual action required, just be aware
CUT TO: S09

## S09 — 1:23.700–1:30.000
STATE CHAIN: F09.0 (no motion — ANIMATION REQUIRED: NO)
SOURCE IMAGE: IMG04 (reused verbatim — its own fully-escalated end state)
IMAGE ACTION: REUSE
I2V PASS: none
EXPECTED RESULT: F09.0 held for the shot's duration
AUDIO SYNC: continuous mixed audio
CUT TO: S10

## S10 — 1:30.000–1:31.900
STATE CHAIN: F10.0 (no motion — ANIMATION REQUIRED: NO)
SOURCE IMAGE: IMG09
IMAGE ACTION: GENERATE
I2V PASS: none
EXPECTED RESULT: F10.0 held for the shot's duration
AUDIO SYNC: continuous mixed audio
CUT TO: S11

## S11 — 1:31.900–1:44.500
STATE CHAIN: F11.0 → A14 → F11.1 → A15 → F11.2 → A16 → F11.3
SOURCE IMAGE: IMG10
IMAGE ACTION: GENERATE
I2V PASS: A14, A15, A16 (chained in sequence)
EXPECTED RESULT: F11.3 (shockwave ring closed around earth outline)
AUDIO SYNC: measured silence (95.778s-96.079s) falls right at this shot's opening boundary
CUT TO: S12

## S12 — 1:44.500–1:49.000
STATE CHAIN: F12.0 → A17 → F12.1
SOURCE IMAGE: IMG11
IMAGE ACTION: GENERATE
I2V PASS: A17
EXPECTED RESULT: F12.1 (moon at beam, red flash, moon now reddened/cracked)
AUDIO SYNC: continuous mixed audio
CUT TO: S13 (no image regeneration — S13 continues directly from A17's resulting frame)

## S13 — 1:49.000–1:58.000
STATE CHAIN: F13.0 → A18 → F13.1
SOURCE IMAGE: IMG11 (continued from S12's resulting frame — IMAGE ACTION: REUSE)
IMAGE ACTION: REUSE
I2V PASS: A18
EXPECTED RESULT: F13.1 (comet far from beam, lower-right of frame)
AUDIO SYNC: two brief measured silences (109.181s-109.345s; 114.036s-114.285s) occur during this motion, no visual action required
CUT TO: S14

## S14 — 1:58.000–2:00.000
STATE CHAIN: F14.0 (no motion — ANIMATION REQUIRED: NO)
SOURCE IMAGE: IMG12
IMAGE ACTION: GENERATE
I2V PASS: none
EXPECTED RESULT: F14.0 held for the shot's duration
AUDIO SYNC: continuous mixed audio
CUT TO: S15

## S15 — 2:00.000–2:03.933 (end of video)
STATE CHAIN: F15.0 (no motion — ANIMATION REQUIRED: NO)
SOURCE IMAGE: IMG13
IMAGE ACTION: GENERATE
I2V PASS: none
EXPECTED RESULT: F15.0 held to the end of the video
TEXT / GRAPHICS: overlay "RIP" and the closing two-line caption per TIMELINE.csv
AUDIO SYNC: audio fades/quiets from 122.711s to the end (measured) — fade the audio track out under this held card
CUT TO: none (end of video)

## Final assembly / export
Export target: H.264 MP4, 720x1280, 30fps CFR, 3718 frames (123.933s), matching the source's video parameters. Assemble all 15 shots' clips/stills in order (S01→S15) with hard cuts at every TRANSITION_IN marked HARD_CUT in `TIMELINE.csv`, and direct continuations (no cut point) where marked SMOOTH (S07→S08, S12→S13). Lay the original (or a licensed/re-recorded equivalent) audio track under the full timeline per `05_audio/AUDIO_MAP.md`; no additional music, SFX, or audio events beyond what is documented there should be added. No camera motion, zoom, or parallax should be added to any shot beyond the single observed pan in S06 (A11). No image or video generation has actually been performed as part of producing this document — these are build instructions only.
