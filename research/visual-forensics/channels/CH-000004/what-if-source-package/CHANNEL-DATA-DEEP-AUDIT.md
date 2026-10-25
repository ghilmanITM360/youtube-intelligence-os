# Channel Data Deep Audit
Repository audit, 2026-09-21. Scope: checked-in local files only. Counts are evidence counts, not estimates of YouTube channel ownership.

## 1. Executive Summary
**Verified canonical YouTube channels: 0.** Repository identifies **14 distinct source videos** in one “what if” production corpus, but stores no channel ID, handle, canonical channel URL, or video-to-channel relation. Visual reports suggest an xkcd “What If?” series; that is a production attribution, not verified YouTube channel identity. Therefore true unique channel count is **unresolved**, with 14 unassigned videos. These videos have 14 real transcripts, 14 source MP4s, and 14 forensic folders. Public performance and first-party Analytics are absent.

## 2. Exact Channel Count
| Measure | Verified count | Basis |
|---|---:|---|
| Channel references with verified identity | 0 | No channel ID/handle/channel URL in repository |
| Canonical unique channels | 0 verified; actual total unresolved | No video-to-channel mapping |
| Duplicate/alias references reconciled | 0 | No channel identities to reconcile |
| Target / historical / outside-target / identity-only channels | 0 classified | No channel registry or target list |
| Distinct source videos | 14 | SOURCE_VIDEO_INDEX.csv and SOURCE_TO_FORENSIC_MAP.csv |
| Videos with transcripts / forensic video / visual evidence | 14 / 14 / 14 | 14 semantic transcript files and forensic folders |
| Channels with extracted packages / intelligence / transcripts / visuals / Analytics | UNRESOLVED / UNRESOLVED / UNRESOLVED / UNRESOLVED / 0 verified | Video artifacts cannot be allocated to verified channel |
Search covered all tracked directories plus file traversal for SQLite, XLSX, ZIP, JSON, URLs, channel IDs, and handles. No `data/raw`, `data/extracted`, `data/normalized`, `data/manifests`, `data/intelligence`, registry, SQLite, or XLSX tracker exists here. Release copy and ZIP are duplicate distribution of same brain. Generalization coffee/heart test is a proposed new script, not a source channel or video.

## 3. Master Channel Inventory
| # | Canonical Channel | Channel ID | Handle | URL | Dataset IDs | Source Group | Package Status | Videos | Descriptions | Real Transcripts | Transcript Placeholders | Thumbnail Metadata | Downloaded Visuals | Forensic Video | Topic Intelligence | Packaging Intelligence | Hook/Script Intelligence | Editing Intelligence | Strategy Intelligence | First-Party Analytics | Main Storage Paths | Missing Data |
|---|---|---|---|---|---|---|---|---:|---:|---:|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | UNRESOLVED “What If?” source group; **not a verified canonical channel** | NONE / NOT AVAILABLE | NONE / NOT AVAILABLE | NONE / NOT AVAILABLE | SRC01–SRC14 | Shared production corpus; owner unverified | Video-level complete | 14 unassigned | 0 | 14 | 0 current | NONE / NOT AVAILABLE | 2,006 forensic evidence images, not thumbnails | 14 MP4s | PARTIAL: video subjects | UNAVAILABLE | PARTIAL: timed transcript/structure | READY: measured shots/motions | PARTIAL: corpus production DNA | NONE / NOT AVAILABLE | `videos/`; `video_forensics_output/`; `production_intelligence_brain/` | Channel identity, public metadata, thumbnails, Analytics |
**Counting rule:** Row above is an unresolved holding group, not one counted channel. No channel card can truthfully assign these 14 videos to a unique YouTube channel.

## 4. Channel Groups
Verified channel groups A–E: **0 each**. Video-level holding group: 14 forensic-ready source videos, all 14 transcript-ready and visual-ready for editing analysis. No metadata-only or identity-only channel records.

## 5. Dataset → Channel Map
| Dataset ID | Dataset Name | Channel(s) | Raw Source | Package | Videos | Transcripts | Purpose | Status |
|---|---|---|---|---|---:|---:|---|---|
| SRC01 | How long could you drive towards the sunset_ | UNRESOLVED | `videos/How long could you drive towards the sunset_.mp4` | `video_forensics_output/how_long_could_you_drive_towards_the_sunset/` | 1 | 1 | Forensic production study | Analyzed |
| SRC02 | What if all visible light was a single beam | UNRESOLVED | `videos/What if all visible light was a single beam.mp4` | `video_forensics_output/what_if_all_visible_light_was_a_single_beam/` | 1 | 1 | Forensic production study | Analyzed |
| SRC03 | YTDown.com_Shorts_Could-you-power-your-computer- | UNRESOLVED | `videos/YTDown.com_Shorts_Could-you-power-your-computer-by-typing_Media_X97DDWvxaqQ_001_1080p.mp4` | `video_forensics_output/Could you power your computer by typing?/` | 1 | 1 | Forensic production study | Analyzed |
| SRC04 | YTDown.com_Shorts_How-high-could-the-magnitude-o | UNRESOLVED | `videos/YTDown.com_Shorts_How-high-could-the-magnitude-of-Earthqua_Media_wBLVmEZV2Oc_001_1080p.mp4` | `video_forensics_output/earthquake-magnitude-shorts-wBLVmEZV2Oc/` | 1 | 1 | Forensic production study | Analyzed |
| SRC05 | YTDown.com_Shorts_Weird-and-worrying-questions_M | UNRESOLVED | `videos/YTDown.com_Shorts_Weird-and-worrying-questions_Media_SLd4hnmeW_g_001_1080p.mp4` | `video_forensics_output/weird_and_worrying_questions/` | 1 | 1 | Forensic production study | Analyzed |
| SRC06 | YTDown.com_Shorts_What-if-the-Moon-were-made-of- | UNRESOLVED | `videos/YTDown.com_Shorts_What-if-the-Moon-were-made-of-Protons_Media_mEUqVgGf4e0_002_720p.mp4` | `video_forensics_output/what_if_the_moon_were_made_of_protons/` | 1 | 1 | Forensic production study | Analyzed |
| SRC07 | YTDown.com_Shorts_What-if-you-drained-the-oceans | UNRESOLVED | `videos/YTDown.com_Shorts_What-if-you-drained-the-oceans_Media_aMshLs0YCTQ_001_1080p.mp4` | `video_forensics_output/drained_oceans/` | 1 | 1 | Forensic production study | Analyzed |
| SRC08 | YTDown.com_Shorts_What-would-the-world-s-largest | UNRESOLVED | `videos/YTDown.com_Shorts_What-would-the-world-s-largest-cities-be_Media_GgEGcxJRDik_001_1080p.mp4` | `video_forensics_output/worlds-largest-cities-what-if/` | 1 | 1 | Forensic production study | Analyzed |
| SRC09 | YTDown.com_YouTube_Could-you-survive-a-nanosecon | UNRESOLVED | `videos/YTDown.com_YouTube_Could-you-survive-a-nanosecond-on-the-Su_Media_UXA-Af-JeCE_001_1080p.mp4` | `video_forensics_output/could_you_survive_nanosecond_sun/` | 1 | 1 | Forensic production study | Analyzed |
| SRC10 | YTDown.com_YouTube_If-all-humans-died-when-would | UNRESOLVED | `videos/YTDown.com_YouTube_If-all-humans-died-when-would-the-last-l_Media_8fADp43wJwU_001_1080p.mp4` | `video_forensics_output/if_all_humans_died/` | 1 | 1 | Forensic production study | Analyzed |
| SRC11 | YTDown.com_YouTube_If-you-put-a-toaster-in-a-fre | UNRESOLVED | `videos/YTDown.com_YouTube_If-you-put-a-toaster-in-a-freezer-which-_Media_9VG0yqq_PHM_001_1080p.mp4` | `video_forensics_output/if_toaster_in_freezer/` | 1 | 1 | Forensic production study | Analyzed |
| SRC12 | YTDown.com_YouTube_What-if-Earth-grew-1cm-every- | UNRESOLVED | `videos/YTDown.com_YouTube_What-if-Earth-grew-1cm-every-second_Media_-1-ldW4kpLM_001_1080p.mp4` | `video_forensics_output/what-if-earth-grew-1cm-every-second/` | 1 | 1 | Forensic production study | Analyzed |
| SRC13 | YTDown.com_YouTube_What-if-Earth-s-Water-Suddenl | UNRESOLVED | `videos/YTDown.com_YouTube_What-if-Earth-s-Water-Suddenly-Disappear_Media_4ZVtHknKuvg_001_1080p.mp4` | `video_forensics_output/what_if_earths_water_suddenly_disappear/` | 1 | 1 | Forensic production study | Analyzed |
| SRC14 | YTDown.com_YouTube_What-would-a-magnitude-15-ear | UNRESOLVED | `videos/YTDown.com_YouTube_What-would-a-magnitude-15-earthquake-be-_Media_e3uk7jU3RHo_002_720p.mp4` | `video_forensics_output/what_would_a_magnitude_15_earthquake_be/` | 1 | 1 | Forensic production study | Analyzed |
| BRAIN-v1.0.0 | Aggregate master tables and DNA | UNRESOLVED | SRC01–SRC14 | `production_intelligence_brain/` | 14 derived | 14 derived | Cross-video production patterns | Validated |
| RELEASE-v1.0.0 | Frozen copy and ZIP | Same unresolved sources | Same 14 MP4s | `releases/production_intelligence_brain-v1.0.0/` and ZIP | 14 duplicate | 14 duplicate | Distribution | Duplicate, not new evidence |
| TEST-A | Coffee/heart visual translation | NONE / NOT AVAILABLE | Proposed script | `generalization_tests/` | 0 source videos | 0 source transcripts | Generalization test | Excluded from source corpus |

## 6. Channel → Dataset Map
No verified channel-to-dataset join. Unresolved source group maps to SRC01–SRC14; BRAIN is their derived aggregate; RELEASE is duplicate package; TEST-A is downstream test, not acquired channel evidence.

## 7. Data Architecture
`videos/*.mp4` and source index SHA-256/ffprobe fields feed 14 `video_forensics_output/<slug>/` folders. Each holds source manifest, evidence frames/contact sheets, timed transcript, timeline, motions/assets, audio analysis, and reconstruction notes. `SOURCE_TO_FORENSIC_MAP.csv` joins source IDs to slugs. Eight master CSVs aggregate per-video observations; DNA/patterns/blueprints derive from them. `RELEASE_MANIFEST.json` hashes frozen copy. No channel table, raw YouTube API export, SQLite catalog, normalized registry, or separate channel intelligence layer.

## 8. Available Fields/Data Types
Identity: source video ID and 12 video IDs embedded in downloader filenames; no channel identity. Channel metadata: none. Video metadata: filename, local SHA-256, duration, dimensions, aspect, FPS, codec, audio presence; YouTube title text is filename-derived. Content: transcribed words/sentences with Whisper word timing, 14 semantic transcript files. Packaging: no thumbnail URLs/images or title-feature table. Classification: source video subjects and portrait/landscape format only. Intelligence: 200 shots, 581 states, 438 motions, 448 assets, 1,421 A/V sync events, seven production DNA docs, patterns and blueprints. Public metrics and first-party metrics: none.

## 9. Video Metadata Coverage
| Field | Video count | Note |
|---|---:|---|
| Local title/filename | 14 | Downloader-derived; not authoritative YouTube title |
| YouTube video ID | 12 | Two plain MP4 names have no ID |
| Watch URL | 0 | Can be constructed for 12 IDs, not stored |
| Published date | 0 | Local creation timestamps are not publication dates |
| Duration | 14 | ffprobe index |
| Views / likes / comments | 0 | No public performance capture |
| Description | 0 | No YouTube descriptions |
| Thumbnail URL | 0 | No thumbnail metadata |

## 10. Description Coverage
0/14 source videos have YouTube descriptions. Reconstruction notes and visual descriptions are different data.

## 11. Transcript Coverage
At video level, 14/14 = 100% **present**, 0 current placeholders. Word-level Whisper alignment exists for all 14; 7,864 word rows and 604 sentence rows. Timing is automated alignment, with 26 documented 10 ms overlaps; do not label as exact human-verified caption timing. Channel-level coverage cannot be calculated without channel mapping.
| Source | Videos | Real transcripts | Placeholder/missing | Coverage | Timing | Words |
|---|---:|---:|---:|---:|---|---:|
| SRC01 `how_long_could_you_drive_towards_the_sunset` | 1 | 1 | 0 | 100% | Whisper word timing | 510 |
| SRC02 `what_if_all_visible_light_was_a_single_beam` | 1 | 1 | 0 | 100% | Whisper word timing | 523 |
| SRC03 `Could you power your computer by typing?` | 1 | 1 | 0 | 100% | Whisper word timing | 407 |
| SRC04 `earthquake-magnitude-shorts-wBLVmEZV2Oc` | 1 | 1 | 0 | 100% | Whisper word timing | 265 |
| SRC05 `weird_and_worrying_questions` | 1 | 1 | 0 | 100% | Whisper word timing | 156 |
| SRC06 `what_if_the_moon_were_made_of_protons` | 1 | 1 | 0 | 100% | Whisper word timing | 333 |
| SRC07 `drained_oceans` | 1 | 1 | 0 | 100% | Whisper word timing | 430 |
| SRC08 `worlds-largest-cities-what-if` | 1 | 1 | 0 | 100% | Whisper word timing | 290 |
| SRC09 `could_you_survive_nanosecond_sun` | 1 | 1 | 0 | 100% | Whisper word timing | 793 |
| SRC10 `if_all_humans_died` | 1 | 1 | 0 | 100% | Whisper word timing | 1115 |
| SRC11 `if_toaster_in_freezer` | 1 | 1 | 0 | 100% | Whisper word timing | 607 |
| SRC12 `what-if-earth-grew-1cm-every-second` | 1 | 1 | 0 | 100% | Whisper word timing | 1094 |
| SRC13 `what_if_earths_water_suddenly_disappear` | 1 | 1 | 0 | 100% | Whisper word timing | 677 |
| SRC14 `what_would_a_magnitude_15_earthquake_be` | 1 | 1 | 0 | 100% | Whisper word timing | 664 |

## 12. Thumbnail/Visual Coverage
Thumbnail URL: 0/14. Downloaded YouTube thumbnail: 0/14. Forensic frame/contact sheet/cut/zoom images: 2,006 files across 14 folders, all visual observations from videos; **not thumbnail evidence**. Asset manifest rows describe visible/reconstruction elements, not downloaded thumbnails.

## 13. Forensic Video Coverage
14/14 source MP4s. Per-video evidence and timelines exist for 14/14. Master has 200 shots, 581 states, 438 motions. Editing claims can be made for sampled corpus, not for whole channel upload history.

## 14. Intelligence Coverage
| Holding | Topic | Packaging | Hook/Script | Editing | Strategy | Unified Plan |
|---|---|---|---|---|---|---|
| SRC01–SRC14 video corpus | PARTIAL: subjects, no topic opportunity study | UNAVAILABLE: no thumbnails/public title dataset | PARTIAL: timed words, no explicit hook taxonomy | READY: measured per-video and master visual/audio data | PARTIAL: production DNA/blueprints, no channel strategy | PARTIAL: generic reconstruction blueprint, no channel-specific content plan |
No channel-level intelligence status is assignable until provenance maps videos to channel identity.

## 15. First-Party Analytics Coverage
0 videos and 0 verified channels. No impressions, CTR, watch time, average view duration, retention, subscribers gained/lost, or traffic source. Public views/likes/comments also absent.

## 16. Channel × Capability Matrix
| Channel | Topic Research | Title Research | Transcript Research | Hook Research | Script Research | Thumbnail Research | Editing Research | Public Performance | Private Analytics | Content Blueprint |
|---|---|---|---|---|---|---|---|---|---|---|
| UNRESOLVED source group (not a channel) | PARTIAL | PARTIAL: filenames | YES: 14 videos | PARTIAL | YES: 14 scripts | NO | YES: 14 videos | NO | NO | YES: corpus production blueprint |

## 17. Data Gaps
Channel-level missing counts are **unresolvable** because denominator is unknown. Video-level gaps: descriptions 14, thumbnails 14, public metrics 14, channel assignment 14, transcripts 0, forensic video 0. There are 0 recorded identity-only channel records. Missing intelligence: no explicit topic-opportunity, packaging, hook taxonomy, or channel strategy artifact. No first-party Analytics.

## 18. Duplicate/Alias Analysis
14 unique SRC IDs, 14 distinct mapped slugs, 14 source MP4 rows. No channel aliases can be reconciled. `releases/` is frozen duplicate of brain, not independent channel/video evidence; `production_intelligence_brain/legacy/` holds superseded/duplicate artifacts. `generalization_tests/` reuses release and is not a fifteenth source video. Visual “xkcd’s what if?” attribution does not prove uploader identity.

## 19. Storage Locations
For each SRC row in §5: raw `videos/<filename>`; forensic `video_forensics_output/<slug>/` with `00_source`, `01_evidence`, `02_analysis`, `03_capcut`, `04_image_to_video`, `05_audio/semantic`; aggregate `production_intelligence_brain/01_master_data/MASTER_*.csv`; manifests/indexes at brain root. No extracted/normalized/channel registry paths. Source index contains stale absolute paths under `/Users/ghilmankhan/workprojects/...`; use current relative paths.

## 20. Source-of-Truth Rules
Use actual files and `SOURCE_VIDEO_INDEX.csv` for video existence; `SOURCE_TO_FORENSIC_MAP.csv` for joins; eight master CSVs for aggregate counts; `video_forensics_output/<slug>/` for per-video evidence. `BRAIN_MANIFEST.json` and validator corroborate counts. `releases/` freezes same brain; `legacy/` is historical only. Never infer channel identity from series branding or title similarity. One metadata conflict: older `MASTER_SHOTS.SCRIPT_OR_AUDIO_CONTEXT` still says “No audio available” for SRC03, while current map, 407 word rows, and transcript prove audio/transcription recovered; current map/master words authoritative for coverage. Test-A manifest describes older release status while current brain says FROZEN; irrelevant to channel count.

## 21. What Each Data Type Can Be Used For
| Data available | What we can learn/do |
|---|---|
| Video IDs where present | Join future YouTube acquisitions; construct candidate watch URLs |
| Local metadata and filenames | Runtime, aspect, format, basic title wording; no upload cadence or performance |
| Descriptions | Unavailable; no CTA/keyword/product analysis |
| Timed transcripts | Hooks, script structure, tone, claims, narration pacing, repeated language |
| Thumbnail URLs / downloaded thumbnails | Unavailable; no thumbnail style claims |
| Actual video/frames | Cuts, pacing, visual rhythm, on-screen elements, motion, camera/edit patterns |
| Master production DNA | Corpus-level visual grammar and reconstruction blueprint |
| Public metrics | Unavailable; no outlier or relative performance analysis |
| First-party Analytics | Unavailable; no CTR, retention, watch-time, impressions, or traffic diagnosis |

## 22. What We Can Do With Each Channel Today
No verified channel has a defensible capability profile. For **each SRC01–SRC14 video**, available labels: SCRIPT RESEARCH, HOOK RESEARCH (manual from timed text), EDITING RESEARCH, video-level TOPIC RESEARCH, limited TITLE RESEARCH from filename, CONTENT BLUEPRINT from corpus patterns. Unavailable for all: FULL COMPETITOR RESEARCH, THUMBNAIL RESEARCH, PERFORMANCE BENCHMARKING, FIRST-PARTY DIAGNOSIS. Source-specific locations and counts in §5 and §11.

## 23. Cross-Channel Research Possibilities
| Use case | Possible now | Required data / current limit |
|---|---|---|
| Topic opportunities across competitors | NO | Channel mapping and broader topic/performance sample absent |
| Competitor comparison / cross-niche strategy | NO | No verified distinct channels |
| Title pattern research | PARTIAL | 14 filenames; exact titles and larger corpus absent |
| Hook and script library | YES, video level | 14 timed transcripts; no channel comparison |
| Thumbnail pattern library | NO | No thumbnail images |
| Editing pattern library | YES, video level | 14 MP4s and 200 measured shots |
| Channel strategy | NO | No verified channel, publication history, or performance |
| Content blueprint generation / new video planning | YES, production style | Existing reconstruction blueprints; no market validation |

## 24. Current Limitations
Repository is a focused production-forensics project, not a multi-channel YouTube research warehouse. Source clips may all belong to same series, but uploader/channel provenance is not captured. The 14-video sample cannot establish channel upload patterns. No descriptions, thumbnails, public engagement, or private Analytics. Some timing is approximate/automated. Release and legacy copies inflate file counts if treated as independent data.

## 25. Highest-Value Next Data To Acquire
1. **Video-to-channel provenance for 14 videos:** channel ID and canonical URL per video; resolves central count and joins all existing intelligence. 2. **Verified public video metadata for same 14:** exact title, publish date, description, views/likes/comments, thumbnail URL; unlocks limited topic/title/performance work across all ready videos. 3. **Actual thumbnails for same 14:** unlocks packaging comparison with already analyzed visual/script corpus. 4. **Broader per-channel upload catalogs** only after IDs confirmed; needed for reliable competitor trends and outliers. 5. **First-party Analytics** only if these channels are owned and access exists; no basis to seek it for third-party competitors.

## 26. Final Mental Model
Pick a **video source ID**, not channel: find MP4 via `SOURCE_VIDEO_INDEX.csv`, slug via `SOURCE_TO_FORENSIC_MAP.csv`, timed transcript/frames/timeline in matching forensic folder, aggregate rows in master CSVs, and production rules in DNA/blueprints. Use it today for script, hook, editing, and style reconstruction. Picking an actual YouTube channel is impossible from current repository because verified channel identities and joins are absent.

### Required Summary Table
**Channel denominator unknown; counts below are video-level coverage of 14 sources, not channel counts.**
| Data Layer | Channels Covered | Missing | Practical Use |
|---|---:|---:|---|
| Identity | 0 verified | 14 video assignments | Join and tracking blocked |
| Video Metadata | 0; 14 local | 14 public records | Technical video analysis |
| Descriptions | 0 | 14 | Unavailable |
| Transcripts | 0; 14 videos | 0 videos | Script and hook study |
| Thumbnail Metadata | 0 | 14 | Unavailable |
| Actual Visual Evidence | 0; 14 videos | 0 videos | Video visual study, not thumbnail |
| Forensic Video | 0; 14 videos | 0 videos | Editing study |
| Topic Intelligence | 0; partial video subjects | 14 channel studies | Limited subjects |
| Packaging Intelligence | 0 | 14 | Unavailable |
| Hook/Script Intelligence | 0; partial video level | 14 channel studies | Timed script study |
| Editing Intelligence | 0; 14 videos | 0 videos | Measured production grammar |
| Strategy Intelligence | 0; corpus production DNA | 14 channel studies | Style blueprint |
| First-Party Analytics | 0 | 14 videos | Unavailable |
