# WAY 2 — Image-to-Video Shot Rebuild

Per-shot builds referencing `IMAGE_PROMPTS.md` (IMG01–IMG15) and `ANIMATION_PROMPTS.md` (A01–A24). No generation/rendering has actually been performed — this is a build specification.

## S01 — 00:00.000–00:05.417
STATE CHAIN: F01.0 → A01 → F01.1
SOURCE IMAGE: IMG01
IMAGE ACTION: Generate.
I2V PASS: A01
EXPECTED RESULT: F01.1
TEXT / GRAPHICS OVERLAY: 'EARTH' / 'MOON' labels recommended as editor overlays for exact wording (or baked if legibility is confirmed).
AUDIO: AU01 continuous from 00:00.000.
CUT TO: S02.
FIDELITY RISK: the field-line density curve (A01) is a texture/opacity change, not object motion — if the I2V model tries to add unrelated camera or object movement, constrain it with explicit locked-camera and static-anchor language.

## S02 — 00:05.417–00:07.958
STATE CHAIN: F02.0 → A02 → F02.0
SOURCE IMAGE: IMG02
IMAGE ACTION: Generate.
I2V PASS: A02
EXPECTED RESULT: F02.0 (held/settled)
TEXT / GRAPHICS OVERLAY: none.
AUDIO: AU01 continuous.
CUT TO: S03.
FIDELITY RISK: none significant; this is a brief (~2.5s), largely static hold with one small figure gesture.

## S03 — 00:07.958–00:26.208
STATE CHAIN: F03.0 → A03 → F03.1 → A04 → F03.2 → A05 → F03.3 → A06 → F03.4 → A07 → F03.5
SOURCE IMAGE: IMG03 (F03.0–F03.2), then IMG04 (F03.3–F03.5)
IMAGE ACTION: Generate both IMG03 and IMG04.
I2V PASS: A03, A04 chained from IMG03; A05 is the transition pass from IMG03 to IMG04; A06, A07 chained from IMG04.
EXPECTED RESULT: F03.5
TEXT / GRAPHICS OVERLAY: all T03 labels ('ORBIT', '10^20', 'F', '10^20·F') recommended as editor overlays for exact wording control.
AUDIO: AU01 continuous; a measured 0.11s near-silence gap falls around 19.2s (mid this shot), APPROXIMATE sync only.
CUT TO: S04.
FIDELITY RISK: A05 is a full compositional change (top diagram removed, new arrow graphic introduced) — treat it as its own isolated pass rather than trying to force one continuous animation across the whole shot, to avoid geometry drift.

## S04 — 00:26.208–00:38.917
STATE CHAIN: F04.0 → A08 → F04.1 → A09 → F04.2 → A10 → F04.3
SOURCE IMAGE: IMG05 (F04.0–F04.1), then IMG06 (F04.2–F04.3)
IMAGE ACTION: Generate both IMG05 and IMG06.
I2V PASS: A08 from IMG05; A09 is the transition pass from IMG05 to IMG06; A10 chained from IMG06.
EXPECTED RESULT: F04.3
TEXT / GRAPHICS OVERLAY: 'UH OH' / 'PLEASE STOP!' (T02) and '200,000 MOLES OF MOLES' (T01) recommended as editor overlays; equation text (T03) may be baked into IMG05/IMG06 if reproduction is reliable.
AUDIO: AU01 continuous.
CUT TO: S05.
FIDELITY RISK: A09 (~7s cloud growth) is the longest single pass in this shot; isolate it from A10 (particle resolution) if the model struggles to keep the growth-then-resolve behavior consistent in one generation.

## S05 — 00:38.917–00:46.542
STATE CHAIN: F05.0 → A11 → F05.1 → A12 → F05.2
SOURCE IMAGE: IMG07 (F05.0–F05.1), then IMG08 (F05.2)
IMAGE ACTION: Generate both IMG07 and IMG08.
I2V PASS: A11 from IMG07; A12 is the transition/cross-dissolve pass from IMG07's end state to IMG08.
EXPECTED RESULT: F05.2
TEXT / GRAPHICS OVERLAY: 'ELECTRON MOON' / 'PE_electrostatic' / 'E=mc²' (T03) recommended as editor overlays.
AUDIO: AU01 continuous.
CUT TO: S06.
FIDELITY RISK: A11's particle-spread path is an estimate; keep the radial-burst language generic (no specific particle count or exact path) to avoid the model overcommitting to a specific pattern that may not match the source exactly.

## S06 — 00:46.542–01:03.500
STATE CHAIN: F06.0 → A13 → F06.1 → A14 → F06.2 → A15 → F06.3
SOURCE IMAGE: IMG09 (start), IMG10 (end)
IMAGE ACTION: Generate both as a first/last-frame pair.
I2V PASS: A13 and A14 as the transition passes from IMG09 toward IMG10; A15 as a final label-reveal pass on IMG10.
EXPECTED RESULT: F06.3
TEXT / GRAPHICS OVERLAY: 'BLACK HOLE' and all scale labels (T03) recommended as editor overlays.
AUDIO: AU01 continuous; a measured 0.19s near-silence gap falls almost exactly at this shot's out-point (~63.5s).
CUT TO: S07.
FIDELITY RISK: this is the shot's key "payoff" transformation (approximation symbol → converging arrows → funnel → black-hole label); using the explicit IMG09/IMG10 first/last-frame pair with a single guided transition pass (covering A13+A14) reduces drift risk versus three independent generations.

## S07 — 01:03.500–01:05.333
STATE CHAIN: F07.0 (static — no animation)
SOURCE IMAGE: IMG11
IMAGE ACTION: Generate.
I2V PASS: none — ANIMATION REQUIRED: NO. Hold IMG11 for the full ~1.8s shot duration.
EXPECTED RESULT: F07.0
TEXT / GRAPHICS OVERLAY: none.
AUDIO: AU01 continuous.
CUT TO: S08.
FIDELITY RISK: none significant.

## S08 — 01:05.333–01:13.083
STATE CHAIN: F08.0 → A16 → F08.0 → A17 → F08.1 → A18 → F08.2 → A19 → F08.3
SOURCE IMAGE: IMG12 (F08.0–F08.1), then IMG13 (F08.2–F08.3)
IMAGE ACTION: Generate both IMG12 and IMG13.
I2V PASS: A16, A17 chained from IMG12; A18, A19 chained from IMG13 (both are regional reveals over the same static plate — the 'DARK ENERGY' graphic and the C02 figure/speech-bubble are both already present in IMG13, so A18/A19 can alternatively be done as simple opacity-mask reveals in an editor rather than generative passes).
EXPECTED RESULT: F08.3
TEXT / GRAPHICS OVERLAY: 'DARK ENERGY' (T01) and 'MAYBE SOMETHING STRINGY?' (T02) recommended as editor overlays.
AUDIO: AU01 continuous; a measured 0.25s near-silence gap falls within F08.1 (~67.0–67.25s).
CUT TO: S09.
FIDELITY RISK: A16's debris path is an estimate; keep language generic (a scatter of fragments, not a specific count/path).

## S09 — 01:13.083–01:28.083
STATE CHAIN: F09.0 → A20 (+A21, A22, A23, A24 in parallel) → F09.6
SOURCE IMAGE: IMG14 (start), IMG15 (end)
IMAGE ACTION: Generate both as a first/last-frame pair.
I2V PASS: A20 is the single long (~13s) continuous-growth pass from IMG14 to IMG15. A21–A24 (caption text swaps) are NOT recommended as separate generative passes — handle them as editor text overlays cut over a single continuous A20 render, since the underlying image otherwise holds no caption text baked in (see IMAGE_PROMPTS.md IMG14/IMG15).
EXPECTED RESULT: F09.6
TEXT / GRAPHICS OVERLAY: all T01 captions and the T03 circle-interior label cycle (PROBLEMS → BIGGER PROBLEMS → EVEN BIGGER PROBLEMS → PROBLEMS BIGGER THAN YOU CAN POSSIBLY IMAGINE) added as editor overlays timed per `../02_analysis/TIMELINE.csv`.
AUDIO: audio's final 1.407s fade (86.736s–88.143s) matched to the last held frames in final assembly.
CUT TO: end of video.
FIDELITY RISK: A20 is the longest single pass in the video (~13s); most I2V models have much shorter native generation windows, so this pass will likely need to be produced as 2–3 shorter chained sub-clips (each re-using the previous clip's last frame as its own start) and stitched in the editor rather than as one continuous generation call.

---

## Final assembly and export
Assemble all 9 shots in order (S01–S09) at 24fps, 720x1280 (or 1080x1920 matched crop), placing AU01 as a single continuous audio track from 00:00.000 with its natural trailing fade (86.736s–88.143s) preserved. Add all caption/label text (T01, T02, T03) as editor overlays per the wording and timing recorded in `../02_analysis/TIMELINE.csv`, rather than relying on generated in-image text, for exact legibility — text was deliberately left off every generated source image (TEXT BAKED: NO throughout). Total export duration: 88.083s video (2114 frames at 24fps) with the audio track's ~0.06s tail beyond the last video frame preserved. No image, video, or audio has actually been generated or rendered as part of this analysis — this document is a build specification only.
