# WAY 1 — CapCut Reconstruction

Media/asset descriptions reference `../02_analysis/ASSET_MANIFEST.csv`; per-frame descriptions reference `../02_analysis/TIMELINE.csv`. Do not repeat those here.

## Project setup
- CANVAS / ASPECT RATIO: 9:16 portrait
- RESOLUTION: 720x1280 (source-matched; 1080x1920 acceptable if upscaling all imported graphics)
- FPS: 24
- TOTAL DURATION: 88.083s (2114 frames) video; extend the final audio track to 88.143s to preserve the trailing fade
- BACKGROUND: none needed as a base layer — every shot supplies its own full-frame background asset (E01/E02/E03/E04/E05)
- MASTER AUDIO: AU01, single continuous track from 00:00.000, no splitting (see `../05_audio/AUDIO_MAP.md`)
- GLOBAL FONT/TEXT SYSTEM: three text roles held throughout — T01 (red, casual/handwriting-style, for asides/jokes), T02 (black, plain sans-serif, for character dialogue), T03 (small black label text, baked into diagram graphics wherever practical, or CapCut native text matching diagram lettering otherwise)
- GLOBAL COLOR RULE: monochrome black/white/grey line art; red (T01/G04) is the only reserved accent color and is never used for T02/T03 text
- GLOBAL EFFECTS: none observed — no camera moves, no filters/LUTs, no persistent overlay effects

## Media to import
Reference `../02_analysis/ASSET_MANIFEST.csv` for full descriptions. Summary: C01, C02 (characters); E01–E05 (backgrounds); G01–G16 (diagram/graphic elements, most single-use); T01–T03 (text systems, native CapCut text layers where wording is exact); AU01 (audio).

---

## S01 — 00:00.000–00:05.417 (frames 0–129)
SOURCE STATES: F01.0 → F01.1
MEDIA: E01, G01, T03, C01
TRACK STACK: V2 — G01 diagram box + T03 labels · V1 — E01 background · (C01 is drawn as part of G01's composed frame, or on its own layer if animating independently) · A1 — AU01
INITIAL COMPOSITION: G01 box centered in the upper third of the frame; C01 below it, facing the box.
BUILD: Import E01 as background. Import/place G01 box graphic with 'EARTH'/'MOON' labels (T03) baked in. Place C01 below.
KEYFRAMES: Use opacity/mask reveal on an overlaid field-line PNG sequence (or a short pre-rendered clip) for A01 rather than manual per-frame keyframing — field-line density increase is a texture change, not a position/scale change.
00:01.000 (frame 24) — field-line overlay opacity 0% → begins fading/building in (A01 start).
00:05.375 (frame 129) — field-line overlay at full density (A01 end).
TOOLS: opacity, overlay, mask
TEXT: 'EARTH' / 'MOON' labels (T03), baked into G01, static position.
TRANSITION: hard cut in at 00:00.000 (video start); hard cut out to S02.
AUDIO SYNC: AU01 continuous from 00:00.000.
END STATE: F01.1.
FIDELITY LIMITATION: exact field-line density curve is APPROXIMATE (derived from 1s-interval sampling, not frame-exact).

## S02 — 00:05.417–00:07.958 (frames 130–190)
SOURCE STATES: F02.0
MEDIA: E03, C01
TRACK STACK: V2 — C01 (recoil pose) · V1 — E03 flash background · A1 — AU01
INITIAL COMPOSITION: E03 fills the frame; C01 small, lower area, in a crouching/recoiling pose.
BUILD: Hard-cut import of E03 as a full-frame graphic/clip. Swap C01's pose asset to the recoiling variant.
KEYFRAMES: If E03 is a static image rather than a short animated clip, no keyframes are needed (APPROXIMATE: source may use a brief pre-rendered burst clip — see A02).
TOOLS: cutout, overlay
TEXT: none.
TRANSITION: hard cut in from S01; hard cut out to S03.
AUDIO SYNC: AU01 continuous.
END STATE: F02.0.
FIDELITY LIMITATION: A02's exact motion (recoil timing/extent) is APPROXIMATE.

## S03 — 00:07.958–00:26.208 (frames 191–628)
SOURCE STATES: F03.0 → F03.1 → F03.2 → F03.3 → F03.4 → F03.5
MEDIA: E01, G02, G03, G04, G05, T03
TRACK STACK: V3 — G04 (red marks, appears mid-shot) · V2 — G02/G03/G05 diagram elements + T03 labels · V1 — E01 background · A1 — AU01
INITIAL COMPOSITION: G02 (macro orbit diagram) upper-middle, G03 (micro proton/electron diagram) directly below it, both same horizontal center.
BUILD: Import E01, then G02+G03. Reveal T03 'ORBIT'/'ORBIT' labels (A03). Overlay G04 red-scribble graphic, animated in with an outline-draw/opacity reveal (A04). Remove G02+G04 (opacity 0 or delete), reveal G05's first arrow+electron (A05). Add second electron + double arrow + '10^20' label (A06). Add second 'F' arrow + '10^20·F' label (A07).
KEYFRAMES:
00:13.000 (frame 312) — T03 'ORBIT' labels opacity 0→100 (A03).
00:17.000 (frame 408) — G04 red-mark overlay opacity 0→100, drawn on (A04).
00:20.000 (frame 480) — G02+G04 opacity 100→0; G05 first electron+arrow opacity 0→100 (A05).
00:21.000 (frame 504) — G05 second electron+arrow+'10^20' opacity 0→100 (A06).
00:25.000 (frame 600) — G05 'F' arrow+'10^20·F' label opacity 0→100 (A07).
TOOLS: opacity, mask, text, overlay
TEXT: 'ORBIT' / 'ORBIT' / '10^20' / 'F' / '10^20·F' (T03), positions per keyframes above.
TRANSITION: hard cut in from S02; hard cut out to S04.
AUDIO SYNC: AU01 continuous; a measured 0.11s near-silence gap falls at ~19.2s (mid F03.1/F03.2), APPROXIMATE sync only.
END STATE: F03.5.
FIDELITY LIMITATION: all internal reveal timings (A03–A07) are APPROXIMATE, derived from 1s sampling.

## S04 — 00:26.208–00:38.917 (frames 629–933)
SOURCE STATES: F04.0 → F04.1 → F04.2 → F04.3
MEDIA: E01, E02, G06, T01, T02, T03, C01
TRACK STACK: V3 — T01/T02 captions · V2 — G06 box/equation + C01 · V1 — E01+E02 background · A1 — AU01
INITIAL COMPOSITION: G06 torn-edge equation box upper area, E02 ground horizon beneath it, C01 lower-center.
BUILD: Import E01+E02, place G06. Reveal T01 '200,000 MOLES OF MOLES' caption with the box. Add T02 'UH OH' caption (A08). Animate the box border to a jagged/cracked mask and grow a cloud graphic above the ground (A09) — use a mask/crop reveal on a pre-rendered growth clip, or scale keyframes on a cloud PNG if animating natively. Swap the cloud asset for the discrete radiating-dots variant of G07 and continue its outward spread (A10). Swap T02 caption to 'PLEASE STOP!' concurrent with A09.
KEYFRAMES:
00:28.000 (frame 672) — T02 'UH OH' opacity 0→100 (A08).
00:29.000 (frame 696) — box border mask → jagged; G07 cloud scale 0%→100% growth ramp begins (A09); T02 → 'PLEASE STOP!'.
00:35.958 (frame 863) — A09 growth ramp ends.
00:36.000 (frame 864) — G07 asset swap to radiating-dots variant; continued outward scale/spread (A10) through 00:38.917 (frame 933).
TOOLS: mask, crop, scale, opacity, text
TEXT: '200,000 MOLES OF MOLES' (T01); 'UH OH' then 'PLEASE STOP!' (T02); equation text (T03, baked into G06).
TRANSITION: hard cut in from S03; hard cut out to S05.
AUDIO SYNC: AU01 continuous.
END STATE: F04.3.
FIDELITY LIMITATION: A09's growth curve and A10's resolve-to-particles moment are APPROXIMATE.

## S05 — 00:38.917–00:46.542 (frames 934–1116)
SOURCE STATES: F05.0 → F05.1 → F05.2
MEDIA: E01, G08, G09, G10, T03
TRACK STACK: V2 — G08/G09/G10 + T03 labels · V1 — E01 background · A1 — AU01
INITIAL COMPOSITION: single icon (G08) centered.
BUILD: Import E01, place G08. Swap G08 for G09 (starburst) with a quick cross-dissolve or hard swap (A11). Swap G09 for G10 (stretched-fabric well graphic) (A12).
KEYFRAMES:
00:41.167 (frame 988) — G08→G09 swap, particles begin at center and scale/spread outward through 00:43.875 (frame 1053) (A11).
00:43.917 (frame 1054) — G09→G10 swap (A12).
TOOLS: opacity, mask, overlay, text
TEXT: 'ELECTRON MOON' / 'PE_electrostatic' / 'E=mc²' (T03).
TRANSITION: hard cut in from S04; hard cut out to S06.
AUDIO SYNC: AU01 continuous.
END STATE: F05.2.
FIDELITY LIMITATION: A11's particle-spread path is APPROXIMATE (radial estimate, not per-particle tracked).

## S06 — 00:46.542–01:03.500 (frames 1117–1523)
SOURCE STATES: F06.0 → F06.1 → F06.2 → F06.3
MEDIA: E01, G11, G08 (miniature), G12, T03
TRACK STACK: V2 — G11/G08/G12 + T03 labels · V1 — E01 background · A1 — AU01
INITIAL COMPOSITION: G11 (universe sphere) upper area; '≈' symbol; miniature G08 lower area.
BUILD: Import E01, place G11 + miniature G08 + '≈' text. Swap '≈' for two converging-arrow graphics (A13). Add G12 funnel graphic beneath the miniature G08 (A14). Reveal 'BLACK HOLE' text (A15).
KEYFRAMES:
00:55.000 (frame 1320) — '≈' opacity 100→0; converging-arrow graphic opacity 0→100 (A13).
00:57.000 (frame 1368) — G12 funnel opacity/scale 0→100, held through 00:59.958 (frame 1439) (A14).
01:00.000 (frame 1440) — 'BLACK HOLE' text opacity 0→100 (A15).
TOOLS: opacity, scale, mask, text
TEXT: '93 BILLION LIGHTYEARS' / 'OBSERVABLE UNIVERSE' / '3,475 km' / 'ELECTRON MOON' / 'BLACK HOLE' (T03).
TRANSITION: hard cut in from S05; hard cut out to S07.
AUDIO SYNC: AU01 continuous; a measured 0.19s near-silence gap falls almost exactly at this shot's out-point (~63.5s).
END STATE: F06.3.
FIDELITY LIMITATION: A13/A14 reveal timings are APPROXIMATE.

## S07 — 01:03.500–01:05.333 (frames 1524–1567)
SOURCE STATES: F07.0 (static — no animation)
MEDIA: E04, G13
TRACK STACK: V1 — E04+G13 combined full-frame illustration · A1 — AU01
INITIAL COMPOSITION: full-frame static illustration.
BUILD: Import G13 (on E04) as a single full-frame image; hold for the shot's duration. ANIMATION REQUIRED: NO.
KEYFRAMES: none.
TOOLS: none beyond a static image clip.
TEXT: none.
TRANSITION: hard cut in from S06; hard cut out to S08.
AUDIO SYNC: AU01 continuous.
END STATE: F07.0.
FIDELITY LIMITATION: none significant (very short, single static hold).

## S08 — 01:05.333–01:13.083 (frames 1568–1753)
SOURCE STATES: F08.0 → F08.1 → F08.2 → F08.3
MEDIA: E05, G14, G15, T01, T02, C02
TRACK STACK: V3 — T01/T02 captions + C02 · V2 — G14/G15 · V1 — E05 background · A1 — AU01
INITIAL COMPOSITION: E05 starfield full-frame; G14 debris burst left-of-center.
BUILD: Import E05, place G14 (debris burst) (A16). Fade G14 out to plain black (A17). Reveal G15 'DARK ENERGY' graphic (A18). Add C02 + speech-bubble caption 'MAYBE SOMETHING STRINGY?' (T02) at lower right (A19).
KEYFRAMES:
00:65.333 (frame 1568) — G14 opacity 100, radial burst held/settling through 00:66.958 (frame 1607) (A16).
00:67.000 (frame 1608) — G14 opacity 100→0 (A17).
00:68.000 (frame 1632) — G15 opacity 0→100 (A18).
00:71.000 (frame 1704) — C02 + T02 speech bubble opacity 0→100 (A19).
TOOLS: opacity, cutout, text
TEXT: 'DARK ENERGY' (T01); 'MAYBE SOMETHING STRINGY?' (T02).
TRANSITION: hard cut in from S07; hard cut out to S09.
AUDIO SYNC: AU01 continuous; a measured 0.25s near-silence gap falls within F08.1 (~67.0–67.25s), APPROXIMATE sync to the plain-black beat.
END STATE: F08.3.
FIDELITY LIMITATION: A16's debris path is APPROXIMATE (radial estimate).

## S09 — 01:13.083–01:28.083 (frames 1754–2113)
SOURCE STATES: F09.0 → F09.1 → F09.2 → F09.3 → F09.4 → F09.5 → F09.6
MEDIA: E05, G16, T01, T03
TRACK STACK: V2 — G16 + T01/T03 · V1 — E05 background · A1 — AU01
INITIAL COMPOSITION: E05 starfield; small G16 circle centered, T01 caption upper-left.
BUILD: Import E05, place G16 at small scale with 'PROBLEMS' label and 'WHAT A BEAUTIFUL DAY' caption. Continuously scale up G16 for the remainder of the shot (A20), swapping its interior label text at three points (PROBLEMS → BIGGER PROBLEMS → EVEN BIGGER PROBLEMS → 'PROBLEMS BIGGER THAN YOU CAN POSSIBLY IMAGINE') timed to roughly match the scale keyframes below. Swap T01 caption text twice more (A21 'JUST MINDING MY OWN BUSINESS...', A22 'HO HUM'), then once more (A23 'LA LA LA'), then fade it out (A24).
KEYFRAMES:
00:73.083 (frame 1754) — G16 scale ≈ small (start of A20).
00:77.000 (frame 1848) — T01 → 'JUST MINDING MY OWN BUSINESS...' (A21).
00:81.000 (frame 1944) — T01 → 'HO HUM' (A22); G16 label → full three-line sentence.
00:84.000 (frame 2016) — T01 → 'LA LA LA' (A23).
00:87.000 (frame 2088) — T01 opacity 100→0 (A24).
01:28.042 (frame 2113) — G16 scale ≈ fills most of frame (end of A20); video ends.
TOOLS: scale, opacity, text
TEXT: T01 caption cycle above; T03 circle-interior label cycle (PROBLEMS / BIGGER PROBLEMS / EVEN BIGGER PROBLEMS / PROBLEMS BIGGER THAN YOU CAN POSSIBLY IMAGINE).
TRANSITION: hard cut in from S08; ends at video out-point (no transition out).
AUDIO SYNC: AU01 continuous, with the audio's final 1.407s fade (86.736s–88.143s) matched to the last held frames.
END STATE: F09.6.
FIDELITY LIMITATION: the exact scale curve for A20 is APPROXIMATE (modeled as a smooth continuous grow across ~13s from 1s-interval samples); caption-swap timings (A21–A24) are APPROXIMATE.

---

## Completion check
All 9 shots (S01–S09) have a build recipe above. All 24 motion events (A01–A24) are cited inline within their respective shot's KEYFRAMES/BUILD section.
