# 08 — Analysis workflow and acceptance gates (for the future one-video audits)

Applies to exactly ONE video per authorized run. No batch, no mass-completion claims. This run did none of it.

## Preconditions per run
1. Resource gate: read five-hour %, weekly %, context %, then paid credits; stop new expensive work near 90 % / 95 % / serious context pressure. Check free disk (>= 6 GB before starting).
2. Ownership gate: confirm `FINANCE_WRITER_OWNERSHIP.md` still `MACHINE_A_SOLE_WRITER_ACCEPTED`; work only in an approved **external** folder (new timestamped folder under `/Users/ghilmankhan/YIOS-local-audits/`); no repo writes, no branch/worktree, no commit/push.
3. Load `SKILL.md` + 14 references + 7 templates from the preserved candidate (read-only). Declare the mode (`CT_SCAN`, DEEP built first, RECONSTRUCTION where viewable).
4. Source gate: re-hash the file (compare with file 02), ffprobe, confirm Video ID/channel against file 03; any HIGH_CONFIDENCE_NEEDS_REVIEW identity needs owner acceptance first.

## Execution phases
SOURCE → COVERAGE → SHOTS → VISUAL STATES → OBJECT LIFECYCLES → MOTION → ART DIRECTION → TEXT/GRAPHICS → CAMERA → AUDIO ALIGNMENT → ATTENTION HYPOTHESES → RECONSTRUCTION BLUEPRINT → VALIDATION (CHANNEL_DNA only after several validated videos).
- Overview: 1 fps contact sheets = `STRUCTURAL`, never CT_SCAN.
- Candidates: ffmpeg `scdet`/frame-diff with `-fps_mode passthrough`; every boundary manually confirmed from native frames; hard cuts, internal state changes, camera moves and typography events logged separately.
- Dense windows: native-frame extraction (PTS + frame index) around fleeting captions, gestures, transitions; unseen gaps declared; resolution floor stated.
- Audio: ffmpeg loudness/silence + local whisper ASR (`ASR_UNCERTIFIED`); no invented wording or beats.
- Labels everywhere: MEASURED / OBSERVED / ESTIMATED / INFERRED / UNAVAILABLE / NOT_APPLICABLE. No claimed retention, CTR, gaze, dopamine or creator intent.

## Mandatory outputs (per skill)
`source_manifest.json`, `coverage.json`, `shot_ledger.csv`, `visual_event_ledger.csv`, `visual_ct_scan_report.md`, `audio_visual_alignment.csv` (or UNAVAILABLE record), `reconstruction_blueprint.md`, `quality_gate.json`, `continuation_handoff.md` — files named by channel + Video ID + source-hash prefix; SHA-256 of every output recorded.

## Acceptance gates (verdict = lowest gate that fails)
| Gate | PASS requires | Typical expected result for a first video |
|---|---|---|
| Source identity | Channel ID + Video ID verified; sha256/bytes/duration/streams recorded; duplicates resolved | PASS after owner accepts non-embedded ID |
| Temporal | Whole video covered; every meaningful state verified; dense/native windows documented; no stepped zoom counted as cut; 1 fps alone fails | PARTIAL until windows done |
| Creative/reconstruction | art, type, colour, motion, story hypotheses with timestamps; prompts for each distinct state; editor blueprint; original recommendations | PASS/PARTIAL |
| Audio | A human actually listened start to end for `FULL_AV_SIGNOFF_COMPLETE`; ASR otherwise `ASR_UNCERTIFIED` | **PENDING (human)** |
| Independent QA | second reviewer or sampled QA recorded | PARTIAL (single reviewer) |
| Integrity | Source MP4/ZIP, JSONL, workbook, receipts, Git unchanged (hash re-check) | PASS |

Truthful verdicts allowed per video: `NOT_STARTED`, `STRUCTURAL_SAMPLED`, `VISUAL_PARTIAL`, `VISUAL_COMPLETE_WITH_EVIDENCE`, `CT_SCAN_COMPLETE_WITH_EVIDENCE`, `RECONSTRUCTION_COMPLETE`, `AUDIO_LISTENING_PENDING`, `FULL_AV_SIGNOFF_COMPLETE`, `HISTORICAL_COMPLETION_UNVERIFIED`, `BLOCKED`. Existing ledgers keep their statuses; this standard never overwrites them. Most realistic first-video outcome: `CT_SCAN_COMPLETE_WITH_EVIDENCE` within declared coverage **plus** `AUDIO_LISTENING_PENDING`.

## Disk and safety plan
- ~11–12 GB free: cap scratch ≈ 2 GB per video, extract only needed windows (JPEG ≤ ~720 px for review; native PNG only for targeted frames), compress/delete after hashing evidence, never write to `/tmp`.
- Never rename/move/re-encode/delete originals; never touch the ZIPs, Finance JSONL/workbook, 966 baseline, NICK receipts, or the preserved kit candidate.
- At threshold or interruption: finish the current atomic step, save checksums and a handoff naming the next frame interval.
