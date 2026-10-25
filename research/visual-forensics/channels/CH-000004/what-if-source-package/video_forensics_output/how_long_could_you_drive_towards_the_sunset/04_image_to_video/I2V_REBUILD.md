# WAY 2 — Image-to-Video Shot Rebuild

Per-shot builds referencing `IMAGE_PROMPTS.md` (IMG01-IMG14) and `ANIMATION_PROMPTS.md` (A01-A34). No generation/rendering has actually been performed — this is a build specification.

## S01 — 00:00.000-00:05.833
STATE CHAIN: F01.0 → A01 → F01.1
SOURCE IMAGE: IMG01
IMAGE ACTION: Generate.
I2V PASS: A01
EXPECTED RESULT: F01.1
TEXT / GRAPHICS OVERLAY: none.
AUDIO: AU01 continuous from 00:00.000.
CUT TO: S02.
FIDELITY RISK: the chalk-globe "spin" is a redraw effect in the source, not true rotation — a naive I2V rotation may over-animate; keep amplitude small (a few degrees of apparent shift) per A01.

## S02 — 00:05.833-00:11.792
STATE CHAIN: F02.0 → A02 → F02.1 → A03 → F02.2
SOURCE IMAGE: IMG02
IMAGE ACTION: Generate.
I2V PASS: A02, then A03 (two sequential passes, each continuing from the previous pass's end frame).
EXPECTED RESULT: F02.2
TEXT / GRAPHICS OVERLAY: X/check marks and circles are graphic elements generated within the I2V passes, not editor text.
AUDIO: AU01 continuous.
CUT TO: S03.
FIDELITY RISK: none significant.

## S03 — 00:11.792-00:13.833
STATE CHAIN: F03.0 → A04 → F03.1
SOURCE IMAGE: IMG03
IMAGE ACTION: Generate.
I2V PASS: A04
EXPECTED RESULT: F03.1
TEXT / GRAPHICS OVERLAY: "NOT A SUNSET" caption should be added as an editor overlay at shot-in (not baked); A04 only animates the second caption's reveal.
AUDIO: AU01 continuous.
CUT TO: S04.
FIDELITY RISK: none significant.

## S04 — 00:13.833-00:31.417
STATE CHAIN: F04.0 → A05 → F04.1 → A06 → F04.3 → A07 → F04.4 → A08 → F04.5 → A09 → F04.6
SOURCE IMAGE: IMG04
IMAGE ACTION: Generate.
I2V PASS: A05, A06, A07, A08, A09 — five sequential passes chained from each other's end frame; this is the longest and most eventful shot in the video and benefits from isolating each rejection-beat as its own pass to avoid drift across the ~17.6s span.
EXPECTED RESULT: F04.6
TEXT / GRAPHICS OVERLAY: "BRWWAAK" sound-effect lettering (x2, within A07/A08) should be added as editor text overlays for legibility rather than relying on the generative model to render clean lettering.
AUDIO: measured near-silence gap at 25.062s-25.172s falls at the A08→A09 boundary.
CUT TO: S05.
FIDELITY RISK: A09 (mountain-roll) is the highest-risk pass in this shot — isolate it as its own generation and use locked-camera language explicitly, since multi-object bounce motion is prone to geometry drift.

## S05 — 00:31.417-00:42.917
STATE CHAIN: F05.0 → A10 → F05.1 → A11 → F05.2
SOURCE IMAGE: IMG05
IMAGE ACTION: Generate.
I2V PASS: A10, then A11 (sequential, chained).
EXPECTED RESULT: F05.2
TEXT / GRAPHICS OVERLAY: "SUNSET ZONE" / "1000 km/h" / "OH NO!" labels may be generated in-pass (as in the reference) or added as editor overlays if legibility suffers.
AUDIO: AU01 continuous.
CUT TO: S06.
FIDELITY RISK: none significant.

## S06 — 00:42.917-00:49.875
STATE CHAIN: F06.0 → A12 → F06.1 → A13 → F06.2
SOURCE IMAGE: IMG06
IMAGE ACTION: Generate.
I2V PASS: A12, then A13 (sequential, chained).
EXPECTED RESULT: F06.2
TEXT / GRAPHICS OVERLAY: "SUNSET ZONE" label carried from the source image; no new text this shot.
AUDIO: AU01 continuous.
CUT TO: S07.
FIDELITY RISK: none significant.

## S07 — 00:49.875-00:53.000
STATE CHAIN: F07.0 (static — no animation)
SOURCE IMAGE: IMG07
IMAGE ACTION: Generate.
I2V PASS: none — ANIMATION REQUIRED: NO. Hold IMG07 for the full ~3.1s shot duration.
EXPECTED RESULT: F07.0
TEXT / GRAPHICS OVERLAY: "NORTH POLE, 90°N" caption as editor overlay.
AUDIO: AU01 continuous.
CUT TO: S08.
FIDELITY RISK: none significant.

## S08 — 00:53.000-01:08.417
STATE CHAIN: F08.0 → A14 → F08.1 → A15 → F08.2 → A16 → F08.3 → A17 → F08.4 → A18 → F08.5
SOURCE IMAGE: IMG08
IMAGE ACTION: Generate.
I2V PASS: A14 through A18 — five sequential passes chained from each other's end frame (caption-only reveals; each can alternatively be handled as an editor text overlay over a single still hold of IMG08 rather than five separate generative passes, which is the more economical option since none of these five motions involve any moving graphic element beyond text/arrow reveals).
EXPECTED RESULT: F08.5
TEXT / GRAPHICS OVERLAY: recommend handling ALL of "LONGYEARBYEN, 78°N" (fade out), "~55 min", "WEST", the circular map inset, and "355 mph" as editor overlays on a single still hold of IMG08, reserving I2V generation only for shots with genuine graphic motion.
AUDIO: AU01 continuous.
CUT TO: S09.
FIDELITY RISK: the S07→S08 transition is LIKELY a dissolve, not a hard cut (see `TIMELINE.csv`); cross-fade the two still plates if reproducing this precisely.

## S09 — 01:08.417-01:14.292
STATE CHAIN: F09.0 → A19 → F09.1 → A20 → F09.2
SOURCE IMAGE: IMG09
IMAGE ACTION: Generate.
I2V PASS: A19, then A20 (sequential, chained).
EXPECTED RESULT: F09.2
TEXT / GRAPHICS OVERLAY: none (all elements are generated graphics, not text).
AUDIO: AU01 continuous.
CUT TO: S10.
FIDELITY RISK: none significant.

## S10 — 01:14.292-01:35.583
STATE CHAIN: F10.0 → A21 → F10.1 → A22 → F10.2 → A23 → F10.3 → A24 → F10.4
SOURCE IMAGE: IMG10
IMAGE ACTION: Generate.
I2V PASS: A21, A22, A23 as sequential passes; A24 as an ISOLATED final pass (car advance + legend icon growth) since it is the longest single continuous motion in the video (~8.6s) and combines two independently-tracked moving elements (car position, legend circle count) — generate separately and composite if the model struggles to keep both in sync in one pass.
EXPECTED RESULT: F10.4
TEXT / GRAPHICS OVERLAY: "NW"/"SW" labels as editor overlays if in-pass generation renders them illegibly.
AUDIO: AU01 continuous.
CUT TO: S11.
FIDELITY RISK: A24 is the highest drift-risk pass in the video given its length and two independent moving elements — isolate the car-path animation and the legend-icon-count animation into two separate passes and composite (mask the legend icon's corner region) if a single pass drifts.

## S11 — 01:35.583-01:44.500
STATE CHAIN: F11.0 → A25 → F11.1 → A26 → F11.2
SOURCE IMAGE: IMG11
IMAGE ACTION: Generate.
I2V PASS: A25, then A26 (sequential, chained).
EXPECTED RESULT: F11.2
TEXT / GRAPHICS OVERLAY: "PyEphem" and "ARCTIC CIRCLE" labels as editor overlays if legibility suffers from in-pass generation.
AUDIO: AU01 continuous.
CUT TO: S12.
FIDELITY RISK: none significant.

## S12 — 01:44.500-01:53.458
STATE CHAIN: F12.0 → A27/A28 → F12.1
SOURCE IMAGE: IMG12
IMAGE ACTION: Generate.
I2V PASS: A27 and A28 together in one pass (SIMULTANEOUS_INDEPENDENT — caption reveal and car advance do not need isolation since the car's motion is small and low-risk).
EXPECTED RESULT: F12.1
TEXT / GRAPHICS OVERLAY: "~95 min" caption as editor overlay if preferred over in-pass generation.
AUDIO: AU01 continuous.
CUT TO: S13.
FIDELITY RISK: none significant.

## S13 — 01:53.458-01:55.000
STATE CHAIN: F13.0 → A29 → F13.1
SOURCE IMAGE: IMG13
IMAGE ACTION: Generate.
I2V PASS: A29
EXPECTED RESULT: F13.1
TEXT / GRAPHICS OVERLAY: "~55 min" and "LONGYEARBYEN" as editor overlays if preferred over in-pass generation.
AUDIO: AU01 continuous.
CUT TO: S14.
FIDELITY RISK: none significant.

## S14 — 01:55.000-02:09.875
STATE CHAIN: F14.0 → A30 → F14.1 → A31 → F14.2 → A32 → F14.3 → A33 → F14.4 → A34 → F14.5
SOURCE IMAGE: IMG03 (REUSE — no new image; see `IMAGE_PROMPTS.md` reuse decisions)
IMAGE ACTION: Reuse.
I2V PASS: A30 first (isolated — the swirl loop is a distinct, sustained motion best generated on its own so it can loop cleanly), then A31-A34 as sequential caption-reveal passes composited over the looping swirl background, OR handled as editor text overlays over a held/looping video plate (recommended — five caption reveals over one background do not each need a separate generative pass).
EXPECTED RESULT: F14.5
TEXT / GRAPHICS OVERLAY: all five T04 dialogue lines recommended as editor overlays for exact wording control; only the swirl motion (A30) genuinely requires I2V generation.
AUDIO: audio fade 128.228s-129.981s under F14.5; match an audio fade-out to this window in final assembly.
CUT TO: end of video.
FIDELITY RISK: keep A30's swirl as a small, contained loop — do not let it drift into the tripod camera or the left-hand figure; explicit static-anchor language in the prompt covers this.

## Final assembly and export
Assemble all 14 shots in order (S01-S14) at 24fps, 480x854 (or 1080x1920 matched crop), placing AU01 as a single continuous audio track from 00:00.000 with a fade-out matching the measured 128.228s-129.981s tail. Add all caption/label text (T01-T04, plus the numeric/direction data labels grouped under T03) as editor overlays per the wording and timing recorded in `02_analysis/TIMELINE.csv`, rather than relying on generated in-image text, for exact legibility. Total export duration: 129.875s video (3117 frames at 24fps) with the audio track's ~0.1s tail beyond the last video frame preserved. No image, video, or audio has actually been generated or rendered as part of this analysis — this document is a build specification only.
