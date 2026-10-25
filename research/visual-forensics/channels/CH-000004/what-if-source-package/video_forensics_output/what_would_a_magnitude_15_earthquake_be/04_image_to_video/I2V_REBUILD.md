# Image-to-Video Rebuild — what_would_a_magnitude_15_earthquake_be

Per-shot assembly plan. Reference `IMAGE_PROMPTS.md` for IMG## prompts and `ANIMATION_PROMPTS.md` for A## prompts; not repeated here.

## S01 00:00.000–00:16.917
STATE CHAIN: F01.0 → A01 → F01.1 → A02 → F01.2 → A03 → F01.3
SOURCE IMAGE: IMG01 (end frame for A03: IMG02)
IMAGE ACTION: Generate IMG01 and IMG02.
I2V PASS: A01, A02, A03 (three sequential passes on the same source image; A01/A02 are simple text swaps best done as editor text-overlay rather than true I2V, A03 is the one pass that needs real I2V generation)
EXPECTED RESULT: F01.3
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 15"/"25" headline and the intro caption box are both editor text overlays, not baked.
COMPOSITE: None required.
AUDIO: Narration presumed continuous; no measured silence gap in range.
CUT TO: S02
FIDELITY RISK: Low — the only true motion (A03) is a single well-defined explosion+collapse.

## S02 00:16.917–00:18.917
STATE CHAIN: F02.0 (static hold)
SOURCE IMAGE: IMG03
IMAGE ACTION: Generate IMG03 (or reuse the identical bumper asset from another video in this project).
I2V PASS: None — ANIMATION REQUIRED: NO, hold the static image for 2.0s.
EXPECTED RESULT: F02.0
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: Baked into IMG03.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S03
FIDELITY RISK: None.

## S03 00:18.917–00:24.042
STATE CHAIN: F03.0 → A04 → F03.1
SOURCE IMAGE: IMG04
IMAGE ACTION: Generate IMG04.
I2V PASS: A04
EXPECTED RESULT: F03.1
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "RICHTER SCALE" / "MOMENT MAGNITUDE SCALE" headlines are editor text overlays.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S04
FIDELITY RISK: Low.

## S04 00:24.042–00:27.458
STATE CHAIN: F04.0 (static hold)
SOURCE IMAGE: IMG05
IMAGE ACTION: Generate IMG05 (text baked — headline/alert wording is essential to the gag).
I2V PASS: None — ANIMATION REQUIRED: NO, hold for 3.4s.
EXPECTED RESULT: F04.0
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: Baked into IMG05. If exact typography drifts in generation, add speech-bubble captions as an editor overlay instead.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S05
FIDELITY RISK: Low.

## S05 00:27.458–00:46.250
STATE CHAIN: F05.0 → A05 → F05.1 → A06 → F05.2 → A07 → F05.3 → A08 → F05.4
SOURCE IMAGE: IMG06 (for F05.0-F05.2); IMG07 (for F05.3-F05.4)
IMAGE ACTION: Generate IMG06 and IMG07.
I2V PASS: A05, A06 (on IMG06); A07, A08 (on IMG07)
EXPECTED RESULT: F05.4
ADDITIONAL INDEPENDENT PASSES: None — A05/A06 can run as one continuous pass on IMG06 if the generator handles two sequential changes well; split into two passes if drift occurs.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 9" headline, epicenter date labels, and LIVE TV caption text are editor overlays.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S06
FIDELITY RISK: Medium — the small explanatory note text in IMG06 is illegible at delivery resolution; do not attempt to bake exact wording.

## S06 00:46.250–01:06.667
STATE CHAIN: F06.0 → A09 → F06.1 → A10 → F06.2 → A11 → F06.3
SOURCE IMAGE: IMG08 (F06.0); IMG09→IMG10 first/last-frame pair (F06.1-F06.3)
IMAGE ACTION: Generate IMG08, IMG09, IMG10.
I2V PASS: A09 (IMG08→IMG09, quick swap, editor cut may suffice instead of true I2V); A10 and A11 as one first/last-frame I2V pass (IMG09→IMG10)
EXPECTED RESULT: F06.3
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 10/11/15" headlines and "PHEW!" are editor overlays.
COMPOSITE: None.
AUDIO: Two measured near-silence gaps (61.4s, 65.2s) fall here.
CUT TO: S07
FIDELITY RISK: Medium — the crack+debris-ring transformation (A10-A11) is a major visual change; using the IMG09→IMG10 first/last-frame pair is recommended over a single freeform I2V pass to keep the globe's identity/scale locked.

## S07 01:06.667–01:14.583
STATE CHAIN: F07.0 → A12 → F07.1
SOURCE IMAGE: IMG11
IMAGE ACTION: Generate IMG11 (a near-blank text-card composition).
I2V PASS: A12 (or simply an editor overlay reveal, since the only change is the TV-inset box appearing)
EXPECTED RESULT: F07.1
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: All headline/fact/caption text is an editor overlay, not baked.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S08
FIDELITY RISK: Low.

## S08 01:14.583–01:17.625
STATE CHAIN: F08.0 (static hold)
SOURCE IMAGE: IMG12
IMAGE ACTION: Generate IMG12.
I2V PASS: None — ANIMATION REQUIRED: NO, hold for 3.0s.
EXPECTED RESULT: F08.0
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 18" headline overlay.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S09
FIDELITY RISK: Low.

## S09 01:17.625–01:23.292
STATE CHAIN: F09.0 → A13 → F09.1
SOURCE IMAGE: IMG12→IMG13 first/last-frame pair
IMAGE ACTION: Reuse IMG12 as the start frame; generate IMG13 as the end frame.
I2V PASS: A13
EXPECTED RESULT: F09.1
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE >18" headline overlay.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S10
FIDELITY RISK: Medium — a large, fast fragment-count explosion; the first/last-frame pair keeps the fragment shapes consistent between S08/S09.

## S10 01:23.292–01:32.750
STATE CHAIN: F10.0 → A14 → F10.1 → A15 → F10.2
SOURCE IMAGE: IMG14→IMG15 first/last-frame pair
IMAGE ACTION: Generate IMG14 and IMG15.
I2V PASS: A14, A15 (can run as one longer first/last-frame pass across both if the generator handles the two-stage texture morph; split if drift occurs)
EXPECTED RESULT: F10.2
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 24" and "*SUNQUAKE" are editor overlays.
COMPOSITE: None.
AUDIO: One measured near-silence gap (84.6s) falls here.
CUT TO: S11
FIDELITY RISK: Medium — sun-to-magnetar is a major object-identity change; the mid transformation (banded texture) is LIKELY, not frame-exact, so treat the intermediate look as approximate.

## S11 01:32.750–01:37.083
STATE CHAIN: F11.0 (single state, internal motion A16)
SOURCE IMAGE: IMG15
IMAGE ACTION: Reuse IMG15.
I2V PASS: A16 (PERSISTENT_LOOP — generate a short looping pulse and repeat/extend to fill 4.3s)
EXPECTED RESULT: F11.0 (held/looped)
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "KERTHUMP" and "SGR 1806-20" are editor overlays.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S12
FIDELITY RISK: Low.

## S12 01:37.083–02:05.958
STATE CHAIN: F12.0 → A17 → F12.1 → A18 → F12.2 → A19 → F12.3 → A20 → F12.4 → A21 → F12.5 → A22 → F12.6
SOURCE IMAGE: IMG15 (F12.0, reused); IMG14 (F12.1-F12.2, reused); IMG16 (F12.3-F12.5, reused across three passes); IMG17 (F12.6)
IMAGE ACTION: Reuse IMG15 and IMG14; generate IMG16 and IMG17.
I2V PASS: A17, A18 (on IMG14); A19, A20, A21 (on IMG16); A22 (transition into IMG17)
EXPECTED RESULT: F12.6
ADDITIONAL INDEPENDENT PASSES: A17/A19/A20/A21/A22 are simple swaps or reveals best done as editor overlays/cuts rather than true I2V generation; only A18 (the sun explosion) needs real I2V motion.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 25", "PLEASE DON'T!", "MAGNITUDE 1" are editor overlays.
COMPOSITE: None.
AUDIO: Three measured near-silence gaps (106.9s, 108.6s, 111.1s) fall in the host/thought-bubble section; one gap (125.6s) falls near this shot's end.
CUT TO: S13
FIDELITY RISK: Medium — this is the longest, most content-dense shot (7 states); F12.0's boundary is APPROXIMATE (see `TIMELINE.csv`), so treat the very start of this shot as a continuation of S11 rather than a hard new composition.

## S13 02:05.958–02:12.583
STATE CHAIN: F13.0 → A23 → F13.1
SOURCE IMAGE: IMG17 (start); IMG18 (end)
IMAGE ACTION: Reuse IMG17; generate IMG18.
I2V PASS: A23
EXPECTED RESULT: F13.1
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE 1" / "MAGNITUDE 0" headline overlays.
COMPOSITE: None.
AUDIO: None distinct measured.
CUT TO: S14
FIDELITY RISK: Low.

## S14 02:12.583–02:50.958
STATE CHAIN: F14.0 →A24→ F14.0 →A25→ F14.1 →A26→ F14.2 →A27→ F14.3 →A28→ F14.4 →A29→ F14.5 →A30→ F14.6 →A31→ F14.7 →A32→ F14.8
SOURCE IMAGE: IMG19 through IMG27 (one per state, all single-use)
IMAGE ACTION: Generate IMG19, IMG20, IMG21, IMG22, IMG23, IMG24, IMG25, IMG26, IMG27.
I2V PASS: A24 (leaf fall, on IMG19); A25 (cat fall, IMG19→IMG20); A26 (cat crash, IMG20→IMG21); A30 (feather fall, on IMG25); A31 (sand flow, on IMG26). A27, A28, A29, A32 are simple static swaps — editor cuts, no I2V generation needed.
EXPECTED RESULT: F14.8
ADDITIONAL INDEPENDENT PASSES: Each magnitude step is intentionally isolated into its own image/pass to avoid drift across nine unrelated micro-scenes.
TEXT / GRAPHICS OVERLAY: "MAGNITUDE -1" through "MAGNITUDE -15" headlines (render -15 dimmer/gray); "WHUMP", "CRASH", "PLINK", "CLICK" onomatopoeia; "I DESERVE THAT." speech text — all editor overlays.
COMPOSITE: None.
AUDIO: Near-silence gaps at 144.5s/147.8s (near -4/-5) and 158.2s (near -7/-8).
CUT TO: S15
FIDELITY RISK: Low per individual state; the only risk is pacing — nine hard cuts in ~38s must land on the exact per-state durations in `TIMELINE.csv` to stay in sync with any restored narration.

## S15 02:50.958–02:55.292
STATE CHAIN: F15.0 → A33 → F15.1
SOURCE IMAGE: IMG28 (F15.0 is a plain black card, no generated image needed)
IMAGE ACTION: Generate IMG28.
I2V PASS: A33
EXPECTED RESULT: F15.1
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: None.
COMPOSITE: None.
AUDIO: This shot falls within the extended near-silence region (173.8s onward).
CUT TO: S16
FIDELITY RISK: Low.

## S16 02:55.292–03:05.292
STATE CHAIN: F16.0 (static hold)
SOURCE IMAGE: IMG29
IMAGE ACTION: Generate IMG29 (or reuse the identical credits asset from another video in this project).
I2V PASS: None — ANIMATION REQUIRED: NO, hold for ~10s to end of video.
EXPECTED RESULT: F16.0
ADDITIONAL INDEPENDENT PASSES: None.
TEXT / GRAPHICS OVERLAY: Baked into IMG29.
COMPOSITE: None.
AUDIO: Extended near-silence measured through this entire shot.
CUT TO: End of video.
FIDELITY RISK: None.
