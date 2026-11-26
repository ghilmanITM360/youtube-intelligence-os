# V15 final production QA

**Status: OWNER_APPROVED_FINAL** (2026-11-25). The owner approved V15 as the canonical production master. The publication audio is the rights-clear master `audio/V15_mix.wav`. Nothing is uploaded until the owner instructs it separately.

**Verdict before approval:** every automated and visual check passed, and the full film played through at normal speed in a browser. Claude has no audio output and did not listen to the mix. The listening gate was the owner's, and the owner then gave approval.

## 1. V14 → V15 defect and improvement audit

Timestamps are film time; V14 and V15 share the same timing map.

| # | Time | Area | V14 defect | Cause | V15 correction | Verification |
|---|---|---|---|---|---|---|
| 1 | whole film | Audio intelligibility | Bed competed with the voice (owner report) | Wind −5 dB; ducking only −7 / −4.5 dB; bed covered the consonant band | Bed −10 dB; ducking −12 / −9 dB; 1–4.5 kHz carve −6 dB; gentle voice levelling | Voiced-window separation median 10.5 → 20.7 dB, p10 5.2 → 17.1 dB (`qa/audio_qa.json`). **Not listened to.** |
| 2 | whole film | Sound design | Reveal sound on almost every arrow (11) | Cue list | 5 accents kept; distant aircraft engine, cloth, strap, instrument, transitions kept | `SOUND_DESIGN_CUE_SHEET.csv` (24 generated cues) |
| 3 | whole film | Captions | Too close to the bottom (box bottom at 1,752 px) | Baseline 578 units | Baseline 536: box bottom 1,626 px, so 294 px clear of the bottom edge | `qa/caption_qa.csv`: 138 samples, all at 1,626 px |
| 4 | 64.9–65.9 s | Captions | Caption over the enlarged bar tops | Screen-wide push onto the bars | Push removed; bars raised (base 470); in-scene ×8 lens instead | Caption collision check: 0 flags on 46 cues |
| 5 | ≈90 s | Captions | "you have stopped falling." could show alone, saying the opposite of the point | Phrase splitter | Sentence kept whole; two balanced lines (≤ 27 chars) | `qa/stills` 89.5 s; SRT cue 39 |
| 6 | 93–97 s | Motion graphics | Second screen-wide push covering the face and bars | Same as #4 | Same lens treatment | Frame strip `cut_Q2`, sheet review |
| 7 | 56–67 s, 93–99 s | Science | Net force shown only as a violet sliver on a bar; magnification not labelled | No net vector; push-in unlabelled | Violet net-force arrow on the body at ×8 with a label, plus a ×8 lens whose rim badge discloses the scale. One magnification everywhere. | Strips `net_arrow_on_body`, `lens_opens` |
| 8 | 56–74 s | Science | Weight was rust brown | Palette | Warm orange `#DB7224`. Teal drag, dashed blue velocity, violet net force. | Sheets |
| 9 | 35–46 s | Science | Airflow not tied to the growing drag | Streamlines only in I2 | Streamlines draw in during H1 with the model load; airflow intensity = drag/weight | Sheet 39 s, 43 s |
| 10 | all tracking shots | Science / parallax | Air marks equally dense at every altitude | Fixed count | Count follows model density (8 + 30·ρ/1.226) | Code + sheets (sparser high up) |
| 11 | all side shots | Character | Legs, boots, hands and clothing never moved; a figure pasted over moving scenery | Rigid sprite | Mesh deformation: independent knees/boots and wrists; travelling cloth ripples driven by drag/weight; pack rigid | `CHARACTER_ANIMATION_QA.md`; `qa/rig_v15/warp_states.png`; 35 frame strips |
| 12 | 41.5–46 s | Science / character | Denser-air comparison showed only dots | — | Same speed, two figures: the one in denser air flutters more (load 0.48 vs 1.33) | Sheet 43 s |
| 13 | 56–67 s, 93–99 s | Composition | Bar panel covered the hands | Bars at x 270+ | Figure framed smaller/left in force shots; narrower panel | `qa/stills` 60.2 / 65.6 / 96 s |
| 14 | 49–56 s | Composition | Speed arrow drawn over the boots | Lane position | Lane moved left | Rig close-up sheet |
| 15 | 68–74 s | Composition (V15 regression, caught by QA) | Trail's speed/net arrows slid under the caption | Camera lag + arrow length | Camera frames the newest mark higher; arrows shortened | Caption check: 0 flags |
| 16 | 0–4.7 s | Visual continuity | Stray grey fragment floating under the aircraft tail | Detached 2,754 px blob in the Codex aircraft art | Cleaned copy `assets/codex/aircraft_side_v15.png` (only that blob removed) | Pixel diff = blob size exactly; still at 0 s |
| 17 | 7–28 s, 79–87 s | Environment | Terrain had fields, roads, river and flat tree discs; no buildings | — | Farmsteads and villages along roads; shaded canopies; clumps resolve into crowns at close range | Sheets 7 s, 80–86 s |
| 18 | tracking shots | Parallax | No layer in front of the faller | — | Soft foreground air motes (speed and opacity from load) | Sheets |
| 19 | 59 s | Labels | "side by side, one scale" clipped at the frame edge | Text length | "one scale" | Sheet 60 s |

## 2. Acceptance gates

| Gate | Result | Evidence |
|---|---|---|
| Character | Pass (with the limits listed in CHARACTER_ANIMATION_QA.md: no finger articulation, no new facial art, rear views not meshed) | Frame strips, rig sheet |
| Motion graphics | Pass: lens, net arrow, trail and bars all serve one idea each; no full-screen push-ins left | Sheets |
| Scientific explanation | Pass: all 10 ideas shown; colour grammar consistent; magnification disclosed | SCIENTIFIC_VISUAL_QA.md |
| Parallax | Pass: sky, haze, far/mid clouds, wisps, faller, foreground motes and terrain move at depth-correct rates (pinhole camera) | Sheets |
| Narration clear and dominant | Pass by measurement; **listening not done** | AUDIO_MIX_QA.md |
| Sound design | Pass: 5 stems; fewer cues; rights-clear master | Cue sheet, licence manifest |
| Captions | Pass: raised, two lines max, 46 cues synced to word timings, 0 collisions | `qa/caption_qa.csv` |
| Mobile composition | Pass: reviewed at 375×812 in the browser and in 216–360 px sheets | Browser screenshot, sheets |
| Opening | Pass: aircraft and faller readable from frame 0 | Browser screenshot at phone size |
| Ending | Pass: slow push, wind fades to 0, picture and sound end together at 110.042 s | Strip `end_card` |
| Visual continuity | Pass: 0 freezes; every cut checked frame by frame | `qa/frames_critical/` (35 strips) |
| Render stability | Pass: 0 decode errors on all three MP4s | `qa/decode_check.txt` |
| A/V sync | Pass: 3 ms; sync map 34/34 events on time | `NARRATION_VISUAL_SYNC_MAP.csv`, `qa/sync_map.log` |
| Rebuild | Pass: isolated rebuild with no access to V13/V14 is byte-identical on 8 files | `qa/isolated_rebuild.txt` |

## 3. Playback review: what was and was not done

| Review | Done? | How |
|---|---|---|
| Real-time playback in a browser | **Yes** | Built-in browser via `qa/review/` on localhost. The captioned film played start to end at normal speed: 110.04 s, 0 dropped frames, 0 stalls. I sampled its state during playback, not by watching continuously. |
| Google Chrome | No | The built-in browser (Chromium) was used instead |
| Listening | **No** | No audio output available. Replaced by measurements; owner check required. |
| Frame-by-frame critical review | Yes | 35 six-frame strips at every cut and key animation (`qa/frames_critical/`) |
| Mobile-size preview | Yes | 375×812 viewport, plus phone-size contact sheets |
| Muted comprehension | Yes | Clean MP4, one frame every 2 s (`qa/muted_sheet_*.png`): the force story reads without sound or captions |
| Caption overlap | Yes | Automated, every cue × 3 times |
| Opening and ending | Yes | Frames 0–24 and the last 2 s |

## 4. Output files

| File | Video | Audio | Frames | Duration |
|---|---|---|---|---|
| `SKYDIVER_SLOWDOWN_FINAL_V15.mp4` | H.264 1080×1920 24 fps | AAC 192k 48 kHz | 2,641 | 110.042 s |
| `SKYDIVER_SLOWDOWN_FINAL_V15_CAPTIONS.mp4` | same + burned captions | same | 2,641 | 110.042 s |
| `qa/review/review_library_mix.mp4` | captioned | library-review mix | 2,641 | 110.042 s |

SHA-256: `qa/checksums_v15.txt`.
