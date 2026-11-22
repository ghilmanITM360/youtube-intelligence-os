# Casually Finance: hub (`@CasuallyFinance`, `UCrNfRFWnLC3tCy1TnyhVQ7g`)

Index for everything the project holds about this channel. **It indexes; it does not move evidence.** Original folders keep their paths so hashes, PR diffs and provenance stay valid (AGENTS.md rules 4 and 7). Casual Economics and Senior Health are **not** part of this hub. Top-level entry: docs/START_HERE.md (retained target `../../docs/START_HERE.md`).

Most evidence lives on the branch `research/casually-finance-consolidated` @ `9a4023af358ad15eec24a11cc5c2818a9d0994c6` (no PR). Links below marked *pinned* open that commit on GitHub; paths in [INDEX.csv](INDEX.csv) are relative to that commit.

## Numbers (from [INDEX.csv](INDEX.csv), 206-video catalog snapshot 2026-10-11; 33 long-form, 173 Shorts)

| Measure | Count | Status |
|---|---:|---|
| Catalog videos indexed | 206 | MEASURED |
| Word-level transcripts committed on the pinned branch | 16 | Whisper `base`, `ASR_UNCERTIFIED` |
| Local Whisper `base` transcripts, 2026-11-09 | 199 | `ASR_UNCERTIFIED`, QC 0 flagged |
| In both | 9 | same model, not independent |
| Videos with any text | 206 / 206 (190 + 9 + 7) | no human-verified or official-caption text |
| Local source media verified (ID or title plus duration) | 206 / 206 | MEASURED |
| Visual-forensics folders (pinned branch) | 19 | visual only |
| Editing-forensics video folders (pinned branch) | 35 | visual only |

Audio listening and AV sign-off are **BLOCKED** for every video. Nothing here is `CT_SCAN_COMPLETE` or `FULL_AV_SIGNOFF_COMPLETE`.

## In this tree

| File | What |
|---|---|
| [INDEX.csv](INDEX.csv) | Per-video lookup: ID, title, format, transcript and forensics paths (paths are on the pinned commit, not here) |
| transcripts_asr_base_20261109/ (retained target `transcripts_asr_base_20261109/`) | Manifest (media hashes and match checks), QC and SHA-256 list for the 2026-11-09 run. The 398 transcript bodies are not in this tree |
| [ASR_NAME_CHECK.md](ASR_NAME_CHECK.md) | Proper-noun pilot (n = 3), not a rerun |
| [LOCAL_ONLY.md](LOCAL_ONLY.md) | What exists only on the owner's Mac |
| [tools/](tools/) | Scripts used for the manifest, the ASR run and the index; they read local media and the pinned checkout |

## On the pinned commit (*pinned*)

| Need | Go to |
|---|---|
| Transcript bodies (199) | [transcripts_asr_base_20261109/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/casually-finance/transcripts_asr_base_20261109) |
| Script, title and topic intelligence | [script-intelligence/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/casually-finance/script-intelligence) |
| Forensic corpus and production DNA | [data/extracted/forensic-analysis/casually-finance/2026-10-12/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/data/extracted/forensic-analysis/casually-finance/2026-10-12) |
| Editing forensics (start at `RESUME_HERE.md`) | [research/casually-finance-editing-forensics/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/casually-finance-editing-forensics) |
| Per-video visual CT scans | [research/visual-forensics/channels/casual-finance/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/visual-forensics/channels/casual-finance) |
| Knowledge navigation across Macs | [visual index START_HERE.md](https://github.com/ghilmanITM360/youtube-intelligence-os/blob/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md) |
| Download inventory (PR #37 / #47 content) | [research/casually-finance-video-inventory/](https://github.com/ghilmanITM360/youtube-intelligence-os/tree/9a4023af358ad15eec24a11cc5c2818a9d0994c6/research/casually-finance-video-inventory) |

## Pull requests that use this material (all open when checked, none merged by this work)

[#21](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/21) base corpus and production DNA; [#28](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/28) success playbook, draft, stacked on #21 (do not retarget to main); [#37](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/37) download inventory (superset); [#47](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/47) scoped inventory (its 10 files are identical to #37's); [#34](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34) senior-health illustration packages; [#30](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30) Finance Short 02 asset package; [#36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36) 966-video Finance audit; [#41](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/41) local media library. Editing forensics and knowledge navigation have no PR yet.

## Known gaps

- 3 videos have two local encodes (`2EZzwupIa80`, `PxgCsLSf-w4`, `rSa2aziEsAI`); 7 local files are not in the catalog (`9eBM5IF_bco` is a new video). See manifest.csv (retained target `transcripts_asr_base_20261109/manifest.csv`).
- Catalog is 206; a live check on 2026-10-14 saw 207 (`9eBM5IF_bco`). The inventory CSV counts 210.
- CF 20/20 (`gG239LrksH4`) is not done. Next milestones: 20, then 25.


Publication note. Retained targets named here are outside this scoped export. See the [folder and file map](../../CHANNEL_VISUAL_AUDIT/CHANNEL_001/COMPLETE_FOLDER_AND_FILE_MAP.md) for disposition.
