# Casually Finance — hub (`@CasuallyFinance`, `UCrNfRFWnLC3tCy1TnyhVQ7g`)

Single entry point for everything the project holds about this channel. **This hub indexes; it does not move evidence.** Original folders keep their paths so hashes, PR diffs and provenance stay valid (AGENTS.md rules 4, 7). Built locally on branch `research/casually-finance-consolidated`, 2026-11-09. Not pushed.

Casual Economics and Senior Health Hub are **not** part of this hub.

## Numbers (from `INDEX.csv`, 206-video catalog snapshot 2026-10-11; 33 long-form, 173 Shorts)

| Measure | Count | Status |
|---|---:|---|
| Catalog videos indexed | 206 | MEASURED |
| Text in repo (git transcripts, Whisper base, earlier run) | 16 | ASR_UNCERTIFIED |
| Text from the 2026-11-09 local Whisper base run | 199 | ASR_UNCERTIFIED, QC 0 flagged |
| Overlap (same video in both) | 9 | same model, not independent evidence |
| Videos with any text | 206 / 206 | |
| Local source media verified (ID / title + duration check) | 206 / 206 | MEASURED |
| Visual forensics dirs (`research/visual-forensics/channels/casual-finance/`) | 19 | visual only |
| Editing-forensics video dirs | 35 | visual only |

Audio listening and AV sign-off are **BLOCKED** for every video. Nothing here is `CT_SCAN_COMPLETE` or `FULL_AV_SIGNOFF_COMPLETE`. Whisper `base` mangles proper nouns (for example "Drunken Miller" for Druckenmiller): verify names and numbers before reuse.

## Map

| Need | Go to |
|---|---|
| Per-video lookup (ID, format, text, media, forensics paths) | [INDEX.csv](INDEX.csv) |
| Catalog metadata (206 videos) | `data/extracted/forensic-analysis/casually-finance/2026-10-12/01_CHANNEL_METADATA/all-videos-metadata.csv` |
| Download inventory (PR #37/#47 content) | `research/casually-finance-video-inventory/` |
| Forensic corpus, production DNA, patterns | `data/extracted/forensic-analysis/casually-finance/2026-10-12/` (00_MANIFEST … 07_VALIDATION), `docs/CASUALLY-FINANCE-FORENSIC-RESEARCH-2026-10-12.md` |
| Source videos committed in git (PR #21) | `data/raw/forensic-analysis/casually-finance/source-videos/` |
| Success and production playbook | `research/casually-finance-success-playbook/` |
| Editing forensics (motion, typography, asset families) | `research/casually-finance-editing-forensics/` (start at `RESUME_HERE.md`) |
| Per-video visual CT scans | `research/visual-forensics/channels/casual-finance/<id>/` |
| Knowledge navigation across Macs | `research/visual-forensics/channels/UCrNfRFWnLC3tCy1TnyhVQ7g/START_HERE.md`, `docs/intelligence/CASUALLY_FINANCE_STORYBOARD_TEST.md` |
| Script, title and topic intelligence | [script-intelligence/](script-intelligence/) (`TRANSCRIPT_COVERAGE.md` has a 2026-11-09 update at the top) |
| Whisper base transcripts, 199 videos, with manifest, QC, SHA256SUMS | [transcripts_asr_base_20261109/](transcripts_asr_base_20261109/) |
| Tools used for the ASR run and the index | [tools/](tools/) |
| Media and frame library (not in git) | [LOCAL_ONLY.md](LOCAL_ONLY.md) |

## Pull requests that use this material (all open, none merged)

| PR | What | Relation |
|---|---|---|
| [#21](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/21) | Complete CF corpus and production DNA (2,257 files) | Base corpus |
| [#28](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/28) | Success and production playbook, draft, stacked on #21 | Must stay on #21, do not retarget to main |
| [#37](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/37) | Video download inventory (880 files, checks FAILURE) | Superset; also carries Finance and Economics files |
| [#47](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/47) | Scoped inventory (10 files, checks SUCCESS) | Alternative to #37; its files are identical to #37's |
| [#34](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/34) | Senior-health illustration packages | Reads #21/#28 by pinned reference only |
| [#30](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/30) | Finance Short 02 original asset package | Reference-led, competitor frames excluded |
| [#36](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/36) | 966-video Finance and Economics audit, in progress | Wider scope, includes the CF channel |
| [#41](https://github.com/ghilmanITM360/youtube-intelligence-os/pull/41) | Checksummed local channel media library | Describes local media handling |

The editing-forensics and knowledge-navigation branches have no PR yet.

## Known gaps

- 3 duplicate local files for `2EZzwupIa80`, `PxgCsLSf-w4`, `rSa2aziEsAI`; 7 local files are not in the catalog (`9eBM5IF_bco` is a new video, the rest are duplicates or unmatched). See `transcripts_asr_base_20261109/manifest.csv`.
- Catalog is 206; a live check on 2026-10-14 saw 207 (`9eBM5IF_bco`). The inventory CSV counts 210.
- CF 20/20 (`gG239LrksH4`) is not done. Next milestone after 15 is 20, then 25.
