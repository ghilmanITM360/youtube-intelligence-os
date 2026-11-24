# 02 Duplicates, provenance and per-folder audit

Register: `02_WHAT_IF_RELATED_FILE_REGISTER.csv` (1,371 rows after removing 15.5k Python-environment hits). It matches by **path/name** (xkcd, what-if, whatif, Munroe, CH-000004, DS-000017, channel ID) and, for text files under 2 MB outside `YIOS-local-audits`, by **content**. A content match only means the words appear (many are generic prose), so the register is a *candidate* list, not proof of relevance. Hashes are included for non-video files under 30 MB; video hashes are in `media_probe_88.csv`.

## Duplicate and identity findings (exact bytes)

| Finding | Evidence |
|---|---|
| Same video, **different bytes** | 14 Brain MP4s in `~/GhilmanProjects/video data of what if/videos/` vs 88-file library: **0 of 14 hashes equal**. For example 8fADp43wJwU: Brain `1fb3c0f4…`, library hash differs. Treat as two encodes of one video, not two videos and not one evidence set. |
| Library vs census hashes | 88 of 88 equal; vs campaign hash list 64 of 64 equal. |
| Preserved Brain tables | `MASTER_AUDIO_EVENTS.jsonl` identical in the preservation folder and in the repo (sha256 `4b932b7d…`). Other 7 files not individually hashed in this pass. |
| Transcript duplicates | 0 exact duplicate transcripts (script study); 56 of 83 share 30% or more 8-grams with another (Shorts cut from longs). So 83 transcripts ≈ 45 content families. |
| Brain SRC01 / SRC02 unresolved YouTube IDs | The repo holds them as unresolved. Candidate resolution by title and duration: SRC01 "How long could you drive towards the sunset" 129.98 s vs rGZ6TsXvi8E 129.94 s; SRC02 "What if all visible light was a single beam" 123.99 s vs TIDHee_Q5Gk 123.92 s. Titles match and durations agree within 0.07 s. **Candidate only; the registry decision stays with the owner** (the Brain is 480x854 / 720x1280, the library 1080x1920). |

## Per-folder audit

| Folder | Files / size | What If-related content | Role |
|---|---|---|---|
| `YIOS-Visual-Forensics-Discovery-2026-10-28` | 22 / 26 MB | `WHAT_IF_VISUAL_RESEARCH_STATUS.md` (accurate on Brain: 14 sources, 200 shots, 581 states, 7.77 s median, SRC01/02 unresolved, PR #44), plus CSV inventories that mention xkcd | **Historical** discovery report (2026-10-28). Predates the Nov 4-6 campaign and the 88-file library. |
| `YIOS-handoffs` | 2 | none (Machine B release handoff) | historical |
| `YIOS-Creator-Intelligence-Audit-2026-10-26` | 104 / 3.9 MB | `S19_DS18` tabs mention What If in prose; master guide cites it. No xkcd video data | general creator-knowledge, not xkcd source |
| `YIOS-Algorithm-Audit-2026-10-26` | 25 / 0.6 MB | census/analysis JSON mention What If | general algorithm audit; no xkcd video data |
| `YIOS-local-audits` | 42,578 / 22 GB (mostly Python envs and restore copies) | **`2026-11-17-xkcd-83-script-intelligence`** (transcripts V001-V083 + audits), **`2026-11-17-xkcd-8fADp43wJwU`** (deep pass + audio stems, 592 MB), **`2026-11-18/WHATIF_COMPETITOR_CT`** (54 MB, 3 competitors); recovery/restore folders hold repo copies | **Live and authoritative** for the three items above; the rest is preservation |
| `yios-worktree-preservation-2026-10-21` | 718 / 141 MB | Brain staging v1.0.0: 8 JSONL (MASTER_WORDS 5.4 MB, AUDIO_VISUAL_SYNC 1.2 MB, ...) | historical; duplicate of repo copy |
| `YIOS-Media-Library` | 463 / 4.7 GB | **88 xkcd MP4**, 3 competitor MP4, other channels | **Live source media** (hash-verified) |
| `YIOS-recovery-2026-10-19-finance-short-experiment-01` | 1,100 / 35 MB | none | unrelated (Finance Short) |
| `yios-local-preservation-2026-10-12` | 2,281 / 821 MB | repo reconciliation JSON; thumbnail-forensics JSON mention the term | historical |
| `youtube-intelligence-os` | repo | strategy, 83-script study, campaign, Brain package | **canonical** |
| not in screenshot: `~/GhilmanProjects/video data of what if` | 664 MB | original Brain root: 14 MP4, `video_forensics_output/`, `production_intelligence_brain/`, `generalization_tests/`, 3 PNGs, tracker xlsx | historical source of Brain; media encodes differ from the library |

**Unique to local (not on GitHub):** the 88-file library, the 14-MP4 Brain root, competitor CT evidence, 8fADp43wJwU deep pass, book OCR.
**Newer than the Nov 18 strategy:** nothing here is newer than the strategy except the strategy's own later commits (2026-11-19) and the 2026-11-23 outputs of this audit.
**Needed for the forensic study:** the 88-file library (primary), the campaign tables on `main`, the Brain staging tables (for the audio-event and AV-sync schema), `YIOS-local-audits/2026-11-17-xkcd-8fADp43wJwU` (audio method), the 83 transcripts.
