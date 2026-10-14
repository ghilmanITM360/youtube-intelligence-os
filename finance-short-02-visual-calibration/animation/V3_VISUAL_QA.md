# V3 visual QA — Finance Short 02

Date 2026-10-14, Laptop B. Machine results: `V3_VIDEO_QA.json` (final, preview, narration-only, deterministic seek) and `V3_STATE_IDENTITY_QA.json`. Edit register: `V3_EDIT_DECISIONS.csv`.

**Verdict:** technically validated; owner viewing, listening and artistic sign-off are still required.

V3 is a targeted polish of the V2 animation:
- **Same:** artwork, characters, layouts, assets and narration.
- **Changed:** cue timing, one lettering morph, three registered expression overlays, a 1.3 s end hold, and a soundtrack.

V2 is preserved unchanged: `Finance_Short_02_FINAL.mp4` (`e606f9d1…`) and `Finance_Short_02_PREVIEW.mp4` (`7ef37f53…`). V2's timeline and tools are at commit `9d0a93a`.

## Outputs

| File | SHA256 | Bytes | Stream |
|---|---|---:|---|
| `Finance_Short_02_FINAL_v3.mp4` | `1536625d33207a914bd7bee3ac1d47f489c0f8df5258659635e00908eecc6be5` | 11,536,034 | H.264 High yuv420p BT.709, 1080×1920, 30 fps, 1530 frames, 51.00 s; AAC 48 kHz mono, V3 mix |
| `Finance_Short_02_PREVIEW_v3.mp4` | `78637483a26c63f6297c3a1952f6f34326fc6ab55a789dece852255b301f2f54` | 5,411,985 | 540×960 lanczos downscale **of the final**; audio stream-copied |
| `Finance_Short_02_FINAL_v3_NARRATION_ONLY.mp4` | `a87e307abd9a6084cecbb08cc4f6615fce2b30fa47347739c1f9cf143d8bb41a` | 11,501,980 | Video stream-copied from the final; untouched narration only (−0.4 dBTP) |

## Technical checks (encoded files)

| Check | Final | Preview | Narration-only |
|---|---|---|---|
| Full decode | No errors; 1530/1530 frames | Same | Same |
| Black / blank frames | 0 / 0 | 0 / 0 | 0 / 0 |
| Frozen runs, single-frame flicker | 0, 0 | 0, 0 | 0, 0 |
| Hard cuts vs timeline (10) | 0–1 frame | 0–1 frame | 0–1 frame |
| Narration lag / fitted gain | 0 samples / −1.35 dB | 0 / −1.35 dB | 0 / 0.00 dB |
| True peak | −1.5 dBTP | −1.5 dBTP | −0.4 dBTP |

- **Deterministic seeking:** frames 462, 525 and 1488 were rendered twice, the second time in reverse order. The PNGs are byte-identical.

## Readable holds (fully revealed until exit)

The figures below come from `KEYFRAME_TIMELINE.json`. The holds measure each layer from full reveal to its exit.

| Layer | V2 | V3 | |
|---|---:|---:|---|
| 0.25% (S03) | 0.11 s, then an empty frame | Glides into "0.25% = 0.0025" and stays to 21.5 s | E01 |
| BEFORE NORMAL PAYMENTS RESUME | 0.14 | 0.62 | E05 |
| COVER THE DEFERRED BALANCE FIRST | 0.51 | 0.95 | E05 |
| TARGET: 3.75–4.00% | 0.72 | 0.94 | E06 |
| +0.25 PERCENTAGE POINT | 1.01 | 1.51 | E06 |
| FOMC highlight box | 0.90 | 1.11 | E06 |
| BOTH CAN BE TRUE (payoff) | 0.68 | 1.98 | E07 |
| FED INTEREST BILL | 0.40 | 0.50 | E09 |
| DIFFERENT SPEEDS | 0.79 | 0.72 | E04, traded for the S05 pause |

Unchanged evidence and caveat holds:

| Layer | Hold (s) |
|---|---:|
| ¼-point crop | 2.05 |
| Reserves 3,022,066 | 1.63 |
| IORB 3.90 % | 1.17 |
| H.4.1 −233,587 | 2.99 |
| 2021 $107.4 billion | 1.82 |
| IF RESERVES STAY THE SAME | 1.27 |
| ILLUSTRATION, NOT A FORECAST | 1.10 |
| CUMULATIVE | 1.55 |
| NOT CREATED BY THIS HIKE ALONE | 1.13 |
| NEGATIVE LINE | 1.62 |
| NO NEGATIVE CASH PAYMENT | 1.05 |
| 2021 PRELIMINARY | 1.05 |

## Review of the encoded video

- **Before editing:** I reviewed V2's encoded final, not the storyboard, using frame montages of 4.4–9.0 s, 2.4–5.4 s, 14.5–20.5 s, 26.6–29.8 s and 34.6–37.6 s, plus the end frames of the evidence states.
- **After editing:** I checked V3 with strips at −3, 0, +3, +8, +15 and +24 frames around all 10 cuts (6 scene changes and 4 internal cuts), plus 0–3.8 s and 47.7–51.0 s.
- **Only confirmed defects were changed.** The list is in `V3_EDIT_DECISIONS.csv`: E01–E12 changed, K01–K03 reviewed and kept.
- **S04_01 cut:** the header-only gap of about 0.55 s was found in this review and fixed (E08).
- **Remaining short header-only openings, accepted:**
  - S06_01: about 0.3 s, while "Until" is spoken.
  - S07_01: about 0.5 s, the header "HIGHER RATES" while "Higher rates" is spoken.
- **Treasury across the S06_05 cut:** it still glides into its new place. This is V2 behaviour, kept as a deliberate continuity link.

## Continuity, identity and accuracy

- **Authored layouts.** I rendered each state's last frame with the camera off and compared it with the authored state SVG.
  - 21 of 36 states are ≤ 0.01 % different.
  - The other 15 states fall into two groups:
    - 12 have an entrance still finishing at the state's last frame; the layer is exact in the next state.
    - 3 carry an intentional face overlay (S03_04, S03_05, S07_04).
  - No placement, scale or z-order changed.
- **Morph (E01).** `TX_DELTA` and `TX_DECIMAL` draw "0.25%" with identical glyph paths. The glide ends exactly on the authored `TX_DECIMAL` placement, and the wipe then reveals only "= 0.0025". No new lettering was drawn.
- **Expression overlays (E10).**
  - `FACE_WOW`, `FACE_THINK` and `FACE_RESOLVE` are existing registered assets.
  - Each is placed at host-local (100,65) at the host's scale, as `CHARACTER_BIBLE.md` specifies.
  - The host's own eyes, brows and mouth are hidden only while an overlay shows.
  - The build script asserts the host pose is static under each overlay. Full-resolution crops were checked for alignment.
- **Unchanged since V2:**
  - Held props: the shield and wrench pop with their grips about the host's foot pivot.
  - Money flows: wipes run Fed → banks and Fed → Treasury, and the `$` note travels with them.
  - Character identity.
  - Camera pushes, at most 1.06×.
- **Financial content.** No figure, source crop or caveat changed.
  - `tools/verify_assets.py --complete` PASS: 114 assets, 24 exact source-pixel crops, 8 contact anchors.
  - No file under `assets/` was modified.
- **Assets.** 107 of 114 are used: V2's 104 plus 3 face overlays. The 7 unused assets and the reasons are in E11.
- **Text and UI zone.** No new text, and no layout moved. Content still ends at y ≈ 1590, as in V2. Nothing new enters the bottom Shorts UI zone.
- **Captions.** The decision is unchanged: lettering appears on the spoken words, plus an `.srt` sidecar for CC. Narration timing is unchanged, so the SRT is still valid.

## Remaining for the owner

1. Watch and listen to `Finance_Short_02_FINAL_v3.mp4` on a phone. In particular, check:
   - the music bed level;
   - whether the 10 effects help or distract;
   - the three face reactions.
2. Some holds remain short because the narration is fixed and dense, and only the end could be extended:
   - IORB 1.17 s
   - DIFFERENT SPEEDS 0.72 s
   - BEFORE … 0.62 s
   - FED INTEREST BILL 0.50 s

   They can be retimed in `tools/build_timeline.py` `CUES`, but only by taking time from a neighbour.
3. Small attribution lines, unchanged from V2 and the asset phase, are small on a phone:
   - the full FOMC sentence
   - H.4.1 RELEASE 8 OCT 2026
   - FED · EFFECTIVE 17 SEP 2026

   The key figures are large, boxed and held, so these lines are context.
4. Re-check the H.4.1 figure before publishing (dated 7 Oct 2026 on screen).
