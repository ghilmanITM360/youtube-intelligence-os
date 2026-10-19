# Casually Finance Editing Forensics — Source Discovery Report (Phase 1 gate)

Generated 2026-10-20 on branch `research/casually-finance-editing-forensics` (worktree `../yio-cf-editing-forensics`, cut from `main` `08e71926`). Everything here was produced read-only against the source media and against Git refs (`git show` / `git ls-tree`); no source file was moved, renamed, rewritten or re-downloaded.

Channel identity: **Casual Finance** `@CasuallyFinance` (`UCrNfRFWnLC3tCy1TnyhVQ7g`). It is **not** Casual Economics and not Casually Explained. The Casual Economics branch exists in the repository and is listed below as excluded evidence.

Evidence labels used throughout: `DIRECTLY_OBSERVED`, `MEASURED`, `REFERENCE_SUPPORTED`, `ART_DIRECTION_INFERENCE`, `PLAUSIBLE_HYPOTHESIS`, `UNKNOWN`, `NOT_VERIFIED`.

## 1. Source verification (MEASURED)

| Check | Result |
|---|---|
| `/Users/ghilmankhan/Downloads/CasuallyFinance` exists, readable | yes |
| `/Users/ghilmankhan/workprojects/youtube-intelligence-os` exists | yes (checkout stays untouched; research lives in a separate worktree) |
| Files in source dir | 54 regular files, 393,588,505 bytes. All `.mp4`; no ZIPs, audio-only files, transcripts, thumbnails or sidecars inside the directory |
| Actual container (ffprobe, not extension) | 54/54 `mov,mp4,m4a,3gp,3g2,mj2`; extension matches container for all |
| Streams | 54/54 have one H.264 video and one AAC audio stream (`yuv420p`; 44.1 kHz stereo ×30, 48 kHz stereo ×24) |
| Decode | 54/54 full ffmpeg decode of all streams with zero error lines; 275,141 video frames counted across all files |
| Total runtime (all 54 files) | 2.927 h |
| Byte-identical files | 1 pair (`rSa2aziEsAI`, two "Why Japan's Economy Is Awful - Casual Finance (720p, h264)" copies) |
| Adjacent archives (outside the dir, same family) | `~/Downloads/CasuallyFinance.zip` (17 mp4 entries) and `~/Downloads/CasuallyFinance (1).zip` (54 mp4 entries): every entry CRC32+size-matches a loose file, 0 unmatched. Archives add no new media |

### Unique videos and the canonical analysis set
- 54 files resolve to **48 unique YouTube videos** (10 long-form, 38 Shorts). Six extra files are variants: 4 lower-resolution SnapYT 360x640 re-encodes of 720p originals, 1 byte-identical duplicate, 1 same-resolution file with different bytes but matching content (5-frame average-hash distance 0.0). Variant content hashes sit at 5.6–10.6/256 bits from their canonical copy; no cross-video near-duplicates (all canonical pairs ≥ 12/256) were found.
- **Variants are one piece of evidence, not independent samples** (AGENTS.md rule 9). Analysis uses one canonical file per video (prior-verified hash first, then highest resolution/bitrate).
- Canonical set: **48 videos, 2.818 h, 264,982 native frames**. Long-form 10 videos / 2.085 h (1280x720 ×8, 1920x1080 ×2; 24 fps ×6, 30 fps ×4). Shorts 38 videos / 0.733 h (720x1280 ×18, **360x640 ×20**; 24 fps ×13, 30 fps ×25).
- 20 canonical Shorts exist locally only as 360x640 SnapYT re-encodes. Fine linework, text weight and sub-10-pixel motion are resolution-limited for those (GAP-009); timing, cut and layout evidence is unaffected.

### Identity method and caveat
Local filenames contain no YouTube ID. The ID map comes from the 2026-10-19 inventory branch (`origin/research/casually-finance-video-inventory` @ `1adfdeb9`, `LOCAL_MEDIA_SCAN.csv`): normalized title (exact or SnapYT-truncated prefix ≥ 8 chars) **and** ffprobe duration ±2 s. I re-checked it: all 54 SHA256 values in that scan equal the SHA256 values I computed independently, and 17 hashes also equal ID-verified hashes in the Oct-12 forensic branch. Identity is strong but not cryptographic for the other 32 videos (`ID_Confidence` column). Public metadata (title, date, views, duration) is the Oct-19 snapshot; views are historical snapshot values.

The inventory branch also enumerates the whole channel: 210 public videos (34 regular, 176 Shorts). Only 48 (10 + 38) are local, so every population statistic this research produces must carry the denominator "48 local videos of 210 public" and cannot be called channel-wide.

## 2. Repository discovery

Searched: 60 local+remote refs (names, `git ls-tree` filename patterns), the checkout's untracked files, `~/Downloads`, `~/workprojects`, and Spotlight. Existence of historical filenames was not assumed.

| Material | Where | Status for this task |
|---|---|---|
| Oct-12 Casual Finance forensic corpus: per-video `SHOTS/STATES/MOTIONS/ASSETS/AUDIO_EVENTS/AUDIO_VISUAL_SYNC/SEMANTIC_BEATS/SENTENCES/TRANSCRIPT/FINANCE_CLAIMS`, `QA.json`, contact sheets; master tables (1,446 shots, 4,508 states, 4,484 motions, 1,992 audio events); `VISUAL/MOTION/EDITING/AUDIO/SHORTS/SCRIPT/PACKAGING_DNA.md`; `ORIGINAL_CONTENT_PRODUCTION_BLUEPRINT.md`; 664-candidate motion disposition register; completion matrix | ref `codex/casually-finance-forensic-research` @ `043b85bf` (PR #21 open), root `data/extracted/forensic-analysis/casually-finance/2026-10-12/` | **Reused as baseline** for 16 videos. Structural PASS only; see §3 |
| Success playbook: Word/Excel analysis, `VISUAL_MOTION_PRODUCTION_DNA.md`, `ORIGINAL_CHANNEL_PRODUCTION_SOP.md`, asset-factory notes, 42-s original Remotion pilot with `QUALITY_REVIEW.md` (acting 2.5/5, illustration 3.0/5 vs reference) | ref `origin/research/casually-finance-success-playbook` @ `fb1e56d0` (PR #28 open) | **Reused as design reference and as a record of known quality gaps** |
| Oct-19 channel inventory: 210-video metadata, `LOCAL_MEDIA_SCAN.csv`, ID map | ref `origin/research/casually-finance-video-inventory` @ `1adfdeb9` (PR #37 open) | **Reused for identity and metadata** |
| `CASUALLY_FINANCE_VISUAL_SPEC.md` (×4) and original HIIT/Running/Swimming animation, scene states, QA sequences | ref `production/senior-health-casually-finance-three-videos` @ `65caa889` (PR #34 open); worktree `../yio-pr34` | **Reference only**: these are production attempts (successor work), not evidence about the originals |
| Finance Short 01/02 keyframe and asset production, plus untracked `finance-short-02-visual-calibration/` (reference-vs-original comparison PNG, article crops) in the main checkout | refs `production/finance-short-01-keyframe`, `production/finance-short-02-assets`; untracked files in main checkout | **Reference only** (production lessons). Not read in depth yet |
| Older working dir with decoded audio, spectrograms, feature arrays and extracted frames for two videos (`-X6YzlY_8tM`, `0ll9rEtoRrs`), plus contact sheets and copies of the corpus (1.2 GB) | `~/Downloads/CasuallyFinance-Forensic-Research/` (the Oct-19 report said this dir was absent; it is present now) | **Available local evidence** for the two videos; not modified, not committed |
| What If (xkcd's What If?) "production intelligence brain" v1.0.0: 14 videos, same table schema (words/sentences/shots/states/motions/assets/audio/sync), `CAPCUT_PRODUCTION_SYSTEM.md`, `IMAGE_TO_VIDEO_SYSTEM.md`, `DECISION_RULES.md`, reconstruction and blueprint docs; repo contract in `docs/WHAT_IF_FORENSIC_SOURCE_CONTRACT.md` | `~/workprojects/video data of what if/` (also in `~/Downloads/`), refs `origin/codex/what-if-*` (merged PRs #8–#16) | **Different channel. Method and schema precedent only** (Phase 9 recipe/decision-rule format). Never mixed into Casually Finance evidence |
| Casual Economics deep dive (`MOTION_SEQUENCES.csv`, 154-row master sequences, `CHANNEL_PRODUCTION_DNA.md`, `ORIGINAL_PRODUCTION_BLUEPRINT.md`) | ref `codex/casual-economics-forensic-research` @ `fce81670` (PR #25) | **Excluded**: different channel. Its motion-sequence record format is a possible template only |
| Finance & Economics 966-video audit (Nick Invests and others) | branch `research/finance-economics-intelligence`, PR #36 | **Excluded and untouched.** The current checkout's uncommitted edits belong to it; I did not switch branches there |
| "27-sequence investigations" and a Casually Finance DOCX report | literal search for "27 sequence/27-sequence/27 sequences" across 5 relevant refs and the What If brain; `~/Downloads` DOCX names | **NOT_FOUND.** The nearest records are 9 source-confirmed sequences (playbook DNA), 3 reference sequences (`reference-sequences.json`) and the 664-candidate disposition register. A Word/Excel deliverable exists on the playbook branch (`research/casually-finance-success-playbook/OFFICE/`) and was not opened |
| `CHANNEL_PRODUCTION_DNA.md`, `ORIGINAL_PRODUCTION_BLUEPRINT.md`, `VISUAL_DNA.md`, `MOTION_DNA.md`, `CASUALLY_FINANCE_VISUAL_SPEC.md` | the first two are Casual Economics names; the others exist for Casually Finance under the paths above | Names located; contents read only where cited |

## 3. Prior research coverage (summary of `PRIOR_RESEARCH_COVERAGE.csv`)

| Group | Videos | Meaning |
|---|---:|---|
| `PARTIAL_STRUCTURAL_ONLY` | 16 (10 long-form, 6 Shorts) | Oct-12 corpus exists; every source SHA256 equals today's canonical file |
| `NONE` | 32 (all Shorts) | No per-video research in any inspected ref. Includes `Qof71Ef-3EU`, a prior-selected Short that was `MISSING_LOCAL` then and is local now (360x640) |
| `BLOCKED_SOURCE_MISSING` | 1 (`turJ6VMfUjI`, "Why You (Mathematically) Need Inflation") | Prior-selected, no local media; row kept so the gap stays visible |

Nothing is graded `VERIFIED_COMPLETE` except source identity and metadata. For the 16 prior videos the corpus is real and structurally consistent (QA `PASS_STRUCTURAL`: state timeline covers the full duration, every inter-state gap is explained by a motion row, IDs unique and resolving), and it is the right baseline to extend. It is **not** complete animation research by the standard of this task:

- Visual method (`QA.json`, MEASURED): every frame decoded at low resolution for change detection; **one representative full-resolution frame per stable state** reviewed on contact sheets. The completion matrix records `full_duration_continuous_visual_review = NOT_STARTED` for all 16.
- Motion: only pixel-flagged candidates were reviewed (e.g. 24/24 in `6S3PzAUFnXQ`); unflagged micro-changes are not tabulated (49 un-tabulated episodes in that one Short); easing is `NOT_ASSESSED`.
- Assets are per-appearance analyst labels. The master's 2,196 asset rows are not 2,196 unique illustrations.
- No typography measurements, no pose/variant/crop de-duplication, no duration-weighted keyframe-versus-generated classification.
- Audio: loudness/pause/transient measurement plus Whisper-base ASR, never auditory listening. Names and numbers are uncertified.

## 4. What can be reused versus what is genuinely incomplete

Reuse as inputs (cite, do not recompute): identity map and metadata; the 16 videos' ASR word timings, shot/state boundaries, motion candidate ranges, asset labels and finance-claim records; the DNA/blueprint prose as hypotheses to test; the playbook's rig/SOP design and pilot quality review; the What If schema and decision-rule formats as templates.

Genuinely incomplete and now tracked in `RESEARCH_GAP_REGISTER.csv` (14 gaps): 32 videos with no forensics (GAP-001); no whole-duration chronological review of the 16 (002); no measured easing or tracked geometry (003); no typography (004); no asset-uniqueness/reuse accounting (005); no auditory listening, which this environment cannot do (006, `BLOCKED`); uncertified ASR names/numbers (007); no ASR for the 32 new Shorts (008); 20 resolution-limited sources (009); one missing source (010); keyframe/generated-motion ratio untested (012); unflagged motion uncertified (013); no per-recipe production specs (014).

## 5. Environment limits that shape later phases

- I receive images and text only. **Direct audio listening is `BLOCKED`** for me; Phase 7 can only report measured signal (loudness, silence, transients, spectrograms) and ASR. This is stated, not worked around.
- Local Python 3.9 has `numpy`, `PIL`, `openpyxl`, `python-docx` and `openai-whisper` (cached `base.pt` and `small.en.pt`). No `cv2`, `scenedetect`, `scipy` or `matplotlib`. Candidate cut detection will use `ffmpeg` filters and `numpy` on decoded gray frames; the prior pipeline did the same.
- Disk: 43 GB free of 460 GB (90 % used). Extracted frames go to a sibling directory outside Git and are bounded per video.
- Live usage at start of this checkpoint: 5-hour 3 %, weekly 56 %. Expensive work stops near 90 % 5-hour or 95 % weekly.

## 6. Selection of the first video

Criteria: no prior forensic record, source present, highest public significance, preferably cheap enough to establish a repeatable per-video procedure. **First video: `Qof71Ef-3EU` "The Cheap Money Era Is Coming to an End"** (Short, 68.352 s, 360x640, 30 fps; 375,765 snapshot views, 3× the next uncovered video). The prior team selected it and then blocked on a missing file; it is now local as `The-Cheap-Money-SnapYT.App.mp4` (`CFSRC-037`). Its 360p limit is disclosed and does not change timing, cut, layout or caption evidence.

Planned queue after it (`STATUS.json`): remaining uncovered Shorts by public views, then the 16 prior videos' continuous review, Shorts first because they cost a fraction of long-form review.

## 7. Phase 1 gate

| File | Purpose |
|---|---|
| `SOURCE_MEDIA_INVENTORY.csv` | 56 rows: 54 media files + 2 adjacent archives; ffprobe facts, SHA256, decode status, ID, variant role, archive copies |
| `PRIOR_RESEARCH_COVERAGE.csv` | 49 rows: 48 local videos + 1 blocked prior-selected video; 12 dimensions graded; rows, refs, hashes, timestamps |
| `RESEARCH_GAP_REGISTER.csv` | 14 class-level gaps with affected IDs |
| `evidence/ffprobe_raw.jsonl`, `evidence/phase1_facts.json` | raw probe output and reconciliation facts |
| `scripts/build_source_inventory.py`, `scripts/build_phase1_discovery.py` | reproducible builders |

Reproduce:
```
python3 -I scripts/build_source_inventory.py /Users/ghilmankhan/Downloads/CasuallyFinance .
python3 -I scripts/build_phase1_discovery.py /Users/ghilmankhan/Downloads/CasuallyFinance /Users/ghilmankhan/workprojects/youtube-intelligence-os .
```
(run from `research/casually-finance-editing-forensics/`; the second script reads prior research through `git show`, so it needs the refs fetched locally).

**Gate decision:** source population is verified and reconciled; what is reusable and what is incomplete is established. Proceeding to per-video forensics.
