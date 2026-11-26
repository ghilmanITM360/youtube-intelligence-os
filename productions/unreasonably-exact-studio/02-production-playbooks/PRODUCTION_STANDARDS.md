# Unreasonably Exact production standards (quick reference)

**Version 1.0 · 2026-11-26.** This file collects the numbers from both finished films. Each standard is marked:
- **[V02] / [V07]**: used and measured in Slot 02 V15 / Slot 07 V3;
- **[P]**: proposed, not yet run end to end.

The detail is in the master playbook (§6–§13, §18, §21).

## Format

| Item | Standard |
|---|---|
| Canvas | 1080×1920 vertical; design units 1080×1920 [V07] (V15 designed at 360×640 and rendered ×3 [V02]) |
| Frame rate | 30 fps [V07] or 24 fps [V02]. State it in the brief; never mix within a film |
| Safe area for key subjects | x 60–1020, y 150–1440 design units [V07 `tokens.SAFE`] |
| Caption band | y 1480–1730 [V07]; V15 box bottom at 1,626 px [V02]. The Shorts UI overlap is **untested** |
| Minimum on-screen type | 34 design units (about 12 pt on a 390-pt-wide phone) [V07]; phone legibility **untested** |
| Codec | H.264 yuv420p, AAC 192–256 kbps, `+faststart` [V02, V07] |

## Picture

| Item | Standard |
|---|---|
| Opening | No visually inactive period in 0–7 s. Run a frame-difference check, with no unmotivated hold over 0.5 s [V07 measured; the 0.5 s limit is P] |
| Disclosures | One table per film. Each note appears once, small and in sentence case, when its model begins, attached to the object it qualifies. No pills or badges [V07] |
| Typography | One licensed caption face for captions **and** labels (Comic Neue, OFL) [V07]. Mono for numbers; a geometric maths face for formulas [V07] |
| Lighting | One sun direction per film [V07 `tokens.SUN`] |
| Science beats | Show the relationship (miss/hit, ratio, cause). Every number is asserted in code against `SCIENTIFIC_CLAIMS_LEDGER.csv` [V07] |

## Sound

| Item | Standard |
|---|---|
| Loudness | −16 LUFS integrated, true peak ≤ −1 dBTP (V07: −2.0) [V02, V07] |
| Voice separation | Measured voice-minus-background in voiced windows: SFX bed median ≥ 20 dB [V02: 20.7]; music 18–24 dB under the voice [V07: 21.0] |
| Ducking | Music −6 dB plus −4 dB at 1–4 kHz while speaking [V07]; ambience −12 dB, effects −9 dB, plus a 1–4.5 kHz −6 dB carve [V02] |
| Cues | A cue sheet with one reason per cue. Tonal cues tuned to the music's key. No rapid repeated cues [V07] |
| Rights | Every publication master is rights-clear. Unlicensed music or SFX go in a review mix only [V02, V07] |

## Assets and Codex

Follow [`CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md`](CLAUDE_CODEX_ASSET_PRODUCTION_PROTOCOL.md):
- bundled CLI 0.171 and effort `high`;
- `-i` references, with `view_image` verified in the log;
- master first; one deliverable per run;
- native sizes 1254², 1536×1024 or 1024×1536;
- Claude measures everything.

Acceptance thresholds:
- layer IoU ≥ 0.97;
- angles within ±3°;
- corners alpha 0, one large component;
- rig ±25° moving test [V07].

## Naming

| Kind | Pattern | Example |
|---|---|---|
| Final video | `UE_SLOT<NN>_<TOPIC>_V<NN>_<FINAL|CAPTIONS>[_RIGHTS_CLEAR|_MUSIC_REVIEW].mp4` | `UE_SLOT07_LUNAR_LASER_RANGING_V03_CAPTIONS_RIGHTS_CLEAR.mp4` |
| Shared asset | `UE_<FAMILY>_<NAME>_<NNN>.png` | `UE_OBSERVATORY_BUILDING_SLIT_OPEN_001.png` |
| Codex run | `B<batch><M|L|P|C>` (master, layers, plate or pose, component); `R<n><x>` repair; suffix `2` = one-defect correction | `B4L2` |
| Status words | `PLANNED`, `CANDIDATE`, `REJECTED`, `APPROVED_IN_FILM`; human steps `NOT PERFORMED` until done | |
| Forbidden | `final_final`, `new_file`, `test2`, `latest` | |

**Existing in-project names are kept,** because code loads them (for example `assets/rigs/observatory/obs_telescope.png`). Standard names are added as hard links (`FINAL_MASTERS/`) or library clones (`04-shared-assets/`).

## Review

- **Three independent reviews before the owner sees a cut:** decoded-frame visual review, science asserts, and technical checks (ffprobe, loudness, frame count) [V07].
- **Human gates** are listening, real-time viewing, the muted-viewer test, licence evidence and owner acceptance. Only a human closes them [V02, V07].
