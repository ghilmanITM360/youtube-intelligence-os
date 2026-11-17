# Visual forensics (Visual CT Scan) research

Completed per-video visual CT scans, stored so any Mac can read the research. Scope is **separate** from the Finance 1,612-video audit population; nothing here changes Finance audit statuses.

| Video ID | Channel | Title | Contract | Entry |
|---|---|---|---|---|
| o3FQcd91MIs | Casual Finance | Why The Dumbest Investors Win (it's not why you think) | CT_SCAN_COMPLETE_WITH_EVIDENCE - VISUAL_ONLY | [manifest](channels/casual-finance/o3FQcd91MIs/PORTABLE_MANIFEST.json) |
| Uumnx2Fo6cE | Casual Finance | The New American Housing Crisis Has Landed | CT_SCAN_COMPLETE_WITH_EVIDENCE - VISUAL_ONLY | [manifest](channels/casual-finance/Uumnx2Fo6cE/PORTABLE_MANIFEST.json) |

Both: `HUMAN_LISTENING_NOT_COMPLETED`, `FULL_AV_SIGNOFF_BLOCKED`. ASR is provisional; shot counts are inferred; small on-screen text partly unverified.

## Start here
- o3FQcd91MIs: `channels/casual-finance/o3FQcd91MIs/research/v2/visual_ct_scan_report_v2.md`, `.../v2/OWNER_ACCEPTANCE_RECORD.md`, `.../v2/original_prompts.md`. v1 files in `research/` are retained history.
- Uumnx2Fo6cE: `channels/casual-finance/Uumnx2Fo6cE/research/OWNER_SUMMARY_ROMAN_URDU.md`, `STATE_BY_STATE_VISUAL_FORENSICS.md`, `ORIGINAL_RECONSTRUCTION_BLUEPRINT.md`, `PER_STATE_RECONSTRUCTION_SPECIFICATIONS.json`.
- Method: [methodology/](methodology/README.md). Machine lookup by ID: [INDEX.csv](INDEX.csv).

## What is in Git vs external
Git: reports, CSV ledgers, JSON specs/gates/manifests, scripts, logs, checksums (byte-identical to the external originals). **Not in Git (`EXTERNAL_EVIDENCE_REQUIRED`):** evidence JPG/PNG frames and sheets, 16 kHz audio, numpy arrays, and the source MP4s. Each video's `EXTERNAL_EVIDENCE_MANIFEST.json` lists every external file with size and SHA-256.

## Recovering external evidence on another Mac
No shared storage is configured. Copy the Machine A folder `/Users/ghilmankhan/YIOS-local-audits/2026-10-24-<VideoID>-deep-ct-scan/` (about 13 MB and 111 MB total; Git holds about 11.5 MB of it) via AirDrop, external drive or approved cloud drive, then verify each file against `EXTERNAL_EVIDENCE_MANIFEST.json` with `shasum -a 256`. Source MP4s are not in Git (never transport raw video via GitHub): obtain them from your own media library and verify against `source_sha256` in the manifest. Machine B availability of any of this is unverified.

Full evidence portability is therefore **not** claimed.
