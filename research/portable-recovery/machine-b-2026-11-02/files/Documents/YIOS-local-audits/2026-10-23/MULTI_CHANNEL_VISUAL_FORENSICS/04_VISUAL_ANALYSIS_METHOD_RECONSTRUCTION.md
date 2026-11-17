# 04 — Visual-analysis method reconstruction

Legend: **A** = proven by existing scripts and receipts. **B** = documented but not executed. **C** = improvement applied or proposed now.

## Historical pipeline (Casually Finance editing forensics, `origin/research/casually-finance-editing-forensics@090f84b3`)

| Step | Existing implementation | Script/file | Inputs | Outputs | Verified use | Limitations |
|---|---|---|---|---|---|---|
| 1 Identify sources | Scan source dir, ffprobe, hash | `scripts/build_source_inventory.py` | `~/Downloads/CasuallyFinance` | `SOURCE_MEDIA_INVENTORY.csv` (SHA256, ffprobe fields) | A (54 rows) | Machine-A paths |
| 2 Map Video IDs | Normalised title prefix + duration vs public inventory | same + `origin/research/casually-finance-video-inventory@1adfdeb9` | filenames (SnapYT truncated titles) | `Video_ID`, `ID_Match_Method=TITLE_PREFIX+DURATION`, confidence "NOT_CRYPTOGRAPHIC" | A | Title matching; this run confirms the mapping by exact SHA256 identity of the same files on B |
| 3 Hash verify | SHA256 per file; re-verify on new machine | inventory + RESUME rule 3 | MP4 | SHA256 column | A | — |
| 4 Probe | ffprobe JSON | `evidence/ffprobe_raw.jsonl` | MP4 | streams/format | A | — |
| 5 Decode / features | ffmpeg `-fps_mode passthrough` to gray arrays; per-frame features; optional Whisper ASR | `forensic_features.py --asr`, `prep_full.sh`, `prep_banded.sh` | MP4 | `auto/` per-frame features | A (decode fix 2026-10-20) | Needs numpy, PIL, torch/whisper (`python3 -E`) |
| 6 Scene / event segmentation | Pixel-delta events; layout bands (row-activity profile) | `layout_profile.py`, `segment_events.py`, `segment_full.py` | features, `bands.json` | event candidates, scene list | A | — |
| 7 Frame extraction & sheets | Event-centred sheets, contact sheets | `event_sheets.py`, `make_sheet.py` | events | JPG sheets (outside Git) | A | Frames on Machine A only |
| 8 Motion measurement | Camera/blob/extent fits, easing curves (scale fits filtered to net change ≥ 5 %) | `measure_motion.py`, `measure_color_area.py` | frames | motion tables | A | Easing tallies were corrected once (2026-10-20) |
| 9 Human-style review | Agent reads sheets, authors scenes/events/assets per video | `videos/<id>/review/author_review.py` + `author_lib.py` | sheets | `scenes.json`, `events.json`, `assets.json` | A | Single reviewer |
| 10 Tables & report | Build per-video tables, `FORENSIC_REVIEW.md`, `STORY_STRUCTURE.md` | `build_video_tables.py`, `write_review.py` | review JSON | per-video tables | A | — |
| 11 Aggregation | Channel DNA, audio aggregate, cross-video reuse, registers | `aggregate_channel.py`, `aggregate_audio.py`, `cross_video_reuse.py`, `update_registers.py` | per-video tables | `CHANNEL_EDITING_DNA.md` and the other chat docs | A (refreshed at n=38) | — |
| 12 Completion rule | QA.json per video: every frame belongs to a segment; every event authored or marked `UNRESOLVED_CHANGE`; depth label A/B/C | `QA.json`, `VALIDATION.json` | — | status `VISUAL_FORENSICS_COMPLETE_AUDIO_LISTENING_BLOCKED` | A | "Do not claim 100 %" |
| 13 Audio | Measured loudness / voiced share / pauses + Whisper small.en ASR; **no listening** | `aggregate_audio.py` | audio | `audio_aggregate.json` | A | Listening blocked by design |
| 14 Long-form procedure | Full automated pass + seeded sampling windows (first/last 60 s + density-ranked + random 45 s windows), label `LF-SAMPLED` | `STATUS.json → longform_procedure` | — | — | **B** (written, not started) | Untested |

Answers to the specific method questions:
- **Opening/middle/ending:** covered for Shorts by full per-frame segmentation. For long-form, it is only planned (B).
- **Transitions/motion:** measured by `measure_motion.py`, plus authored events.
- **Contact sheets:** yes.
- **Real-time playback:** no evidence of actual playback; review used extracted frames.
- **Audio listening:** no.
- **Script alignment:** via ASR timing.
- **Full coverage proven:** yes for the 38 Shorts (QA). Not for long-form.

Other historical methods:
- **Casual Economics (Codex):**
  - candidate-state segmentation for the 6 historical videos;
  - 4 s point samples plus 160 temporal sequences for the other 5;
  - scripts `prep_video.py` and `temporal_video.py`, validated by `validate_sampled_package.py` (A).
  - Its own register admits that sampling missed short states.
- **What If brain:** Swift frame extraction, OCR and speech scripts (`extract_video_frames.swift`, `ocr_images.swift`, `transcribe_video_speech.swift` under `data/raw/forensic-analysis/DS-000012/...`), plus dense change-peak analysis (`dense_metrics.csv`, `motion_energy_250ms.csv`, `change_triplets_*.jpg` in DS-000013) (A).

## Why the Machine A pipeline was NOT re-run on Machine B

Machine B's `python3` has **no numpy, PIL, torch or whisper** (`ModuleNotFoundError`). A whisper.cpp model *was* found late in the run at `~/.cache/hyperframes/whisper/models/ggml-small.en.bin` and used via `whisper-cli` for uncertified ASR on the 4 pilots (step 6 below). Installing them would add dependencies, which needs owner approval under the owner's rules. Running the CF pipeline here would also fork a second writer onto Machine A's branch. Machine A owns that branch.

## Method used in this run (C — bounded, ffmpeg/ffprobe only, external tooling)

`tools/pilot_extract.sh` + `tools/dense_window.sh` (hashes recorded in 08):
1. SHA-256 re-check against the inventory; ffprobe; `-count_frames` full decode count.
2. **Full-frame pass:** ffmpeg `select='gte(scene,0)',metadata=print` gives a scene score for every decoded frame (`scene_scores.txt`). Frames with a score ≥ 0.30 go to `cuts_0.30.tsv`.
3. **Uniform full-timeline coverage:** 1 fps sheets (tile k = second k), every second of every pilot viewed.
4. **Dense windows** (2–30 fps) on the opening, on clusters of cut candidates, on fades, and (for the 30 s Short) on the whole video at 2 fps.
5. Audio signal: EBU R128 loudness and silencedetect (−35 dB, 0.4 s).
6. Uncertified ASR: whisper.cpp 1.9.5 + `ggml-small.en` on 16 kHz mono PCM. Used for narration-to-visual spot checks only, never as a transcript of record. No listening.

Measured weakness of the scene-score detector (new finding, documented with evidence):
- **Overcounts stepped zooms.** Primate `DZG89lilGr0` 23.53–24.60 s has 8 "cut candidates", but the dense 30 fps window shows one stepped push-in that changes scale every ~4 frames.
- **Undercounts pose swaps on white backgrounds.** Primitive `HERcUJ6fIlw` has only 5 candidates, while the 2 fps window shows about 15 distinct visual states (pose swaps, word reveals).
- **Misses slow fades.** The b-roll fade-in at Primate 85–87 s and the background darkening at 205–208 s produce no candidate.

Conclusion: cut-candidate counts are **not** comparable editing-cadence statistics across styles. This report does not quote cuts/min as a channel metric.

## Proposed improvements (C, not yet applied)

1. Owner decision: either run CF long-form and `turJ6VMfUjI` on Machine A, or approve pinned `numpy`/`Pillow` on Machine B. Machine A's pipeline uses Python whisper. The existing whisper.cpp model could replace it on B, but only with an explicit method note.
2. For non-CF channels, a state-change detector on downscaled grayscale differences: `ffmpeg … -vf "scale=160:-1,format=gray,tblend=all_mode=difference,signalstats"` → YAVG per frame. It is ffmpeg-only, catches low-amplitude pose/text changes, and needs no new dependency.
3. Promote a pilot from PARTIAL to COMPLETE only after every changed-state interval is authored at frame accuracy, matching the CF Shorts contract.
