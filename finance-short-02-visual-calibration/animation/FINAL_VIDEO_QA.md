# Finance Short 02 — final video QA (V2)

> V2 record, kept unchanged. The current deliverable is V3: see `V3_VISUAL_QA.md` and `V3_AUDIO_MIX_QA.md`.

Date 2026-10-14, Laptop B. Machine results are in `FINAL_VIDEO_QA.json` (`tools/qa.py video`) and `STATE_IDENTITY_QA.json` (`tools/qa.py states`). **Verdict: technically validated; human viewing, listening and artistic sign-off are still required.**

## Output

| | Final | Preview |
|---|---|---|
| File | `Finance_Short_02_FINAL.mp4` | `Finance_Short_02_PREVIEW.mp4` |
| SHA256 | `e606f9d14029f60f42618edc31d4cd4711b58e6b719a6285e9c9e77f21b146a9` | `7ef37f5395bf979ea205696bd6e1702ab618a84e27e871dc6e17d3bfaf6f7bff` |
| Size | 11,134,899 B | 4,754,403 B |
| Video | H.264 High, yuv420p, BT.709 (matrix/primaries/transfer tagged), 1080×1920, 30/1 fps, 1491 frames, 49.70 s, CRF 16 | Same, 540×960 lanczos downscale of the final, CRF 20 |
| Audio | AAC-LC 48 kHz mono 192 kb/s, 49.68 s | Stream-copied from the final |

## Technical checks (all on the encoded file)

| Check | Result |
|---|---|
| Full decode (`ffmpeg -f null`) | **No errors**. 1491/1491 frames decoded |
| Black frames (mean luma < 16) | **0** |
| Blank white frames (< 0.2 % ink) | **0**. Four near-empty in-between frames found in review v1 were fixed by turning two layout replacements into cuts |
| Frozen segments (identical consecutive frames) | **0**. A gentle per-shot camera push keeps every hold alive |
| Single-frame flicker | **0** |
| Audio truncation / offset | Sample count equals the WAV's at 48 kHz (2,384,640). Zero-lag SNR vs WAV **47.3 dB**. Video ends 0.02 s after the audio |
| Clipping | Sample peak −0.45 dBFS, true peak −0.4 dBTP. The narration is not altered (see `AUDIO_PROVENANCE.md`) |
| Cut sync | The encoded file's 10 hard cuts land within **0–1 frame** of the timeline's cut frames (the offset comes from rounding cue times to the 30 fps grid) |
| Deterministic seeking | With `--num-raster-threads=1`, repeated renders of the same frames are **byte-identical** (3 frames × 3 runs). Without that flag, ≤84 anti-aliasing pixels varied, so the flag is now fixed in `render.cjs`. Encoded frames vs direct renders: PSNR 40.4–41.2 dB (H.264 loss only) |
| Watermark | None. The renderer adds nothing; no third-party or tool overlay |

## Artwork identity (the existing package, no redesign)

- **36/36 states and 7/7 scene groups** are animated from `SCENE_ASSET_MAP.csv`. 104 of the 114 registered assets appear as 117 layer tracks; the canvas is the page background. Unused: the 6 optional `FACE_*` overlays, `HAND_OPEN`, `HAND_POINT` and `HOST_NEUTRAL`, none of which is referenced by any state. **No new artwork was created**, and no asset file was modified (`tools/verify_assets.py --complete` PASS: 114 assets, 24 exact source crops, 8 contact anchors).
- **Pixel identity.** Each state's last frame (camera off) was compared with the authored state SVG rendered by the same browser:
  - 25 states differ in ≤0.01 % of pixels (anti-aliasing only).
  - 11 differ only because an entrance is still finishing or was deliberately delayed. Examples: the cash bundle waits for "$7.5" (S03_01–03), and S05_01 is a 0.2 s build step. Each of those layers matches exactly in the following state.
- Layer order, anchors, scale and placement are the authored values. Motion is applied around them as keyframe offsets.

## Motion (simple keyframes only)

Keys: 621 across 117 tracks, plus 28 camera keys. Operations:

| Operation | Count |
|---|---:|
| Trace reveal of lettering ("write-on") | 42 |
| Arrow and diagram trace reveals | 14 |
| Source-highlight wipes | 4 |
| Pop-ins | 31 |
| Group pop-ins about a shared pivot | 6 |
| Documentary entrances | 8 |
| Cut-then-push first layers | 12 |
| Prop glides | 2 |
| Pose switch on the spot | 1 |
| Pose switch with relocation | 2 |
| Note travel along a money flow | 2 |
| Soft exits | 14 |
| Hard-cut exits | 94 |

Scene 06 is not over-built: it has 6 states in 9.7 s. All 11 cuts sit on spoken phrase boundaries or stressed words.

- **Money flows never reverse.** Wipes follow the drawn direction:
  - Interest flow right → left (Fed → bank)
  - Remittance route left → right (Fed → Treasury)
  - Reserve link bank → Fed
  
  The `$` note travels in the same direction as each arrow.
- **Held props stay attached.** The shield with its grip, and the wrench with its grip, pop about the host's foot pivot as one group, so the static contact (< 2.5 px, asset phase) holds through scaling. This was checked on 6 rendered pop frames.
- **The bill sheet** is part of `HOST_BILL` and swaps on the spot (S01_03), easing a 40 px / 5 % authored offset over 8 frames.
- **No character slides.** The large host relocations are a 5-frame fade then a pop (S05_05) or a cut (S05_01, S07_03).
- **Props move only when intended.** The ledger (S05_05) and Treasury (S06_05) glide over 15 frames. No rotation is used anywhere.
- **The slow vs fast contrast is told by motion.** The bond-income arrow writes on over 36 frames; the reserve-expense arrow shoots up in 7.

## Sync with the original WAV

Every cue references a word of `AUDIO_ALIGNMENT.json` (whisper base, phrase onsets snapped to measured silences). Each cue is checked against the word text, so a re-alignment cannot silently drift.

- Visuals land about 2 frames before the word.
- The paradox ("RATES UP." / "BILL UP, TOO." with the host holding the bill) is on screen by 2.9 s.
- Every frame from frame 0 has artwork.
- The last state ("BOTH CAN BE TRUE") arrives on "harder to repair", and the video ends 0.4 s after the final word, with no outro.

Whisper word onsets can drift by ~0.1–0.2 s inside a phrase. Phrase starts are tied to measured silences, so they are tighter.

## Documentary evidence and financial accuracy

- Only the 8 verified documentary assets are used: FOMC statement line, date and ¼-point crop; reserves; IORB; H.4.1 row label and total; 2021 remittance. Source pixels are untouched, and the red highlight boxes are separate layers.
- Readable holds (fully revealed until exit):

  | Source | Hold |
  |---|---:|
  | FOMC line | 2.05 s |
  | ¼-point crop | 1.84 s |
  | Reserves 3,022,066 | 1.80 s |
  | IORB 3.90 percent | 1.17 s |
  | H.4.1 −233,587 | 2.99 s |
  | 2021 $107.4 billion | 1.82 s |

  Attention pushes (1.05–1.07×) run on the reserve, H.4.1 and 2021 states.
- Caveats are kept and held:

  | Caveat | Hold |
  |---|---:|
  | IF RESERVES STAY THE SAME | 1.27 s |
  | ILLUSTRATION, NOT A FORECAST | 1.10 s |
  | CUMULATIVE LOSSES | 1.71 s |
  | NOT CREATED BY THIS HIKE ALONE | 1.30 s |
  | NEGATIVE LINE = DEFERRED BALANCE | 1.62 s |
  | NO NEGATIVE CASH PAYMENT | 1.05 s |
  | 2021 PRELIMINARY | 1.05 s |
  | TARGET: 3.75–4.00% (not narrated) | 0.72 s, the shortest |

- No figure was changed:
  - The $7.5B is shown only as the conditional calculation $3T × 0.0025 at constant reserves.
  - IORB 3.90 % is kept distinct from the 3.75–4.00 % target.
  - −233,587 million is labelled cumulative and dated 7 Oct 2026 (release 8 Oct 2026).
  - 2021 $107.4B is labelled preliminary.
- The narration's "roughly $234 billion" rounds the on-screen 233,587 million, and "more than $107 billion" agrees with $107.4B.

## Captions, music, SFX

- **Captions.** The Shorts DNA shows caption chunks in 5/6 reference Shorts. In this artwork, the hand-lettered labels already carry the spoken phrase chunks and are revealed on the spoken words. A separate subtitle band would cover evidence: content reaches y≈1590, and a band would sit in the bottom Shorts UI zone. So none was burned in.
  - `Finance_Short_02.en.srt` (approved wording) is provided for YouTube CC.
  - This is an editorial decision the owner may reverse.
- **No music or SFX.** Narration only, so there are no rights questions.

## Limitations (not certified)

- **No human listening or viewing sign-off.** Claude judged sync from ASR, waveform and frames, not by watching with sound.
- **Number realisation is inferred.** How the numbers were spoken is inferred from ASR (see `AUDIO_PROVENANCE.md`).
- **Short states.** Some states are very short (S05_01 0.20 s; S03_01–03 0.42–0.66 s), and the target-range label is readable for 0.72 s. These are fast additive builds, in line with the corpus's 42–79 states/min. A viewer may still want slightly longer holds; retime in `CUES` and re-render a window.
- **Small text on phones.** Fine attribution and documentary context inherited from the artwork are small on a phone. Examples: the full FOMC sentence, "FED H.4.1 . RELEASE 8 OCT 2026", "MILLIONS . 7 OCT 2026". This is unchanged from `ASSET_QA.md`.
- **Lettering style.** It is cleaner and more orderly than the reference creator's ink, as recorded in the asset phase. No equivalence to Casually Finance is claimed, and no competitor pixels are used.
- **Cross-machine pixel identity.** It is only promised for the same Chrome and ffmpeg versions (this render: Google Chrome 155.0.8059.40 on macOS, ffmpeg 9.0.1).
